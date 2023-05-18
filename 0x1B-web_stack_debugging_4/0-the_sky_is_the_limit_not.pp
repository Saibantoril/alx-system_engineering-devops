#Increase the amount of traffic an Nginx server can handle
# Restarts Ngninx

file { '/etc/default/nginx':
  ensure  => file,
  content => template('your_module/nginx_default.erb'),
  notify  => Exec['nginx-restart'],
}

exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,
}
