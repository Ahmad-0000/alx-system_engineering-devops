# A manifest to configure "ssh_config" file on the client side

$file_content = "\
Host 54.160.124.48
    HostName 54.160.124.48
    User ubuntu
    IdentityFile ~/.ssh/school
    IdentitiesOnly yes
"

file { 'optional_task':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  content => $file_content
}
