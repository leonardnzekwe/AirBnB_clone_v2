# Web Servers Setup Using Puppet

# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Create 'ubuntu' user
user { 'ubuntu':
  ensure => 'present',
}

# Create 'ubuntu' group
group { 'ubuntu':
  ensure => 'present',
}

# Create necessary directories
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file
file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => "Hello World!\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

file { '/var/www/html/custom_404.html':
  ensure  => 'file',
  content => "Ceci n'est pas une page\n\n",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>",
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Define the Nginx configuration content
$nginx_config_content = "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.nginx-debian.html;
    server_name _;

    location /hbnb_static/ {
       alias /data/web_static/current/;
    }

    add_header X-Served-By ${hostname};
    error_page 404 /custom_404.html;

    location /redirect_me {
       return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
      index index.html index.nginx-debian.html;
   }
}
"

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => $nginx_config_content,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  notify  => Service['nginx'],
}

# Restart Nginx Service
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
