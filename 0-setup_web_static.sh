#!/usr/bin/env bash
# Web Servers Setup

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
html_content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
echo -e "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "s|server_name _;|$nginx_config|" /etc/nginx/sites-available/default

# Restart Nginx Service
sudo service nginx restart
