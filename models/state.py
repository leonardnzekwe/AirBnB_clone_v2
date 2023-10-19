#!/usr/bin/python3
"""State Module for HBNB project"""
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class that inherits from BaseModel"""
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='state',
            cascade='all, delete-orphan'
        )
    else:
        name = ""

        @property
        def cities(self):
            """
            Getter attribute cities that returns
            the list of City instances
            linked to the current State.
            """
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
