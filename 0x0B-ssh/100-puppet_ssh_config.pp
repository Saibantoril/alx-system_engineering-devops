file { '/home/<username>/.ssh/config':
  mode => '0600',
  owner => '<username>',
  group => '<username>',
  content => "
    Host <remote_host>
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
