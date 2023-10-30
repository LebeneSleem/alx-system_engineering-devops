# Puppet Manifest to Kill a Process Named "killmenow"
exec { 'kill_killmenow':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Exec['start_my_process'],
}
