#Increase the amount of traffic an Nginx server can handle

file { '/etc/default/nginx':
  ensure  => file,
  content => template('your_module/nginx_default.erb'),
  notify  => Exec['nginx-restart'],
}
#restarts Nginx
exec { 'nginx-restart':
  command     => 'service nginx restart',
  refreshonly => true,
}
