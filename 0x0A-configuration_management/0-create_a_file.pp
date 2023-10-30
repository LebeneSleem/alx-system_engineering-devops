# Puppet Manifest to Create a File in /tmp
file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
