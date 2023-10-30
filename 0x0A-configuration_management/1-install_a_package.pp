# Puppet Manifest to Install Flask from pip3
class { 'python': }
python::pip { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
