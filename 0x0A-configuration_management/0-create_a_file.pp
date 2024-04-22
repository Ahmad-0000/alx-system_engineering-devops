file { 'first_task':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-date',
  content => 'I Love Puppet'
}
