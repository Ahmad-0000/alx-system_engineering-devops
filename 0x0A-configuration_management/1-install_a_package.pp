# A manifest to install "flask" package with the version "2.1.0"
# using "pip3" as a provider.

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
