# A manifest to configure "ssh_config" file on the client side

$file_content = "\
Host school_server
	HostName 54.160.124.48
	User ubuntu
	IdentityFile ~/.ssh/school
	IdentiesOnly yes
"

file { 'optional_task':
  ensure  => present,
  path    => '/home/vagrant/.ssh/ssh_config',
  content => $file_content
}
