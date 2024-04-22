# A manifest to create file named 'school' if not present, it
# will posess the following attributes

file { 'first_task':
  ensure  => 'present',
  path    => '/tmp/school',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet"
}
