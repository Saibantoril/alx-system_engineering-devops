# This manifest kills a process named killmenow using pkill

exec { 'kill_killmenow':
  command => '/usr/bin/pkill killmenow',
  onlyif  => '/usr/bin/pgrep killmenow',
}
