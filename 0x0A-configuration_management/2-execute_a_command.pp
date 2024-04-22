# A manifest to execute "pkill" command on a specific procsess

exec { 'pkill':
  command => '/usr/bin/pkill sleep'
}
