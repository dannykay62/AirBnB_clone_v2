#!/usr/bin/pup
# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Create necessary directories if they don't exist
file { '/data':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/shared':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => 'Hello, this is a test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create or update the symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  require => File['/data/web_static/releases/test/index.html'],
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
server {
  listen 80;
  listen [::]:80;

  server_name mydomainname.tech;

  location /hbnb_static/ {
    alias /data/web_static/current/;
  }
}
",
  require => Package['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
