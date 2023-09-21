#!/usr/bin/python3
"""Place Module for HBNB project"""
import os
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.review import Review


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id', String(60), ForeignKey('places.id'),
        primary_key=True, nullable=False
    ),
    Column(
        'amenity_id', String(60), ForeignKey('amenities.id'),
        primary_key=True, nullable=False
    )
)


class Place(BaseModel, Base):
    """Place class that inherits from BaseModel"""
    __tablename__ = 'places'

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship(
            'Review', backref='place', cascade='all, delete-orphan'
        )
        amenities = relationship(
            'Amenity', secondary=place_amenity,
            viewonly=False, backref='place_amenities'
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """
            Getter attribute reviews that returns
            the list of Review instances
            """
            from models import storage
            review_list = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """
            Getter attribute amenities that
            returns the list of Amenity instances
            based on the attribute amenity_ids that
            contains all Amenity.id linked to the Place
            """
            from models import storage
            amenity_instances = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    amenity_instances.append(amenity)
            return amenity_instances

        @amenities.setter
        def amenities(self, amenity_obj):
            """
            Setter attribute amenities that handles append method
            for adding an Amenity.id to the attribute amenity_ids
            This method should accept only Amenity object,
            otherwise, do nothing.
            """
            if isinstance(amenity_obj, Amenity):
                self.amenity_ids.append(amenity_obj.id)
