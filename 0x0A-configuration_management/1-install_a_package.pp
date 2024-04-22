# A manifest to install "flask" package and "werkzeug" package
# with the specified attributes

package { 'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
