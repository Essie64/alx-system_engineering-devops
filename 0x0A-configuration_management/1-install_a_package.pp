# install package
package { 'python3-pip':
  ensure => present,
}

exec { 'install_flask':
  command => 'pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => 'pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
