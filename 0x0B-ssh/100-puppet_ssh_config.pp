# Puppet manifest to make changes to the ssh config file
file_line { 'Disable Password Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
  match  => '#    PasswordAuthentication yes'
}

file_line { 'Declare IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
