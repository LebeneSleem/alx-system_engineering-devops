# Puppet Manifest to Kill a Process Named "killmenow"

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
