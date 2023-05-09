# A puppet that debugs and corrects why Apache returns 500 error

file { '/etc/httpd/conf/httpd.conf':
  ensure => present,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => template('my_module/httpd.conf.erb'),
  require => Package['httpd'],
  notify  => Service['httpd'],
}
