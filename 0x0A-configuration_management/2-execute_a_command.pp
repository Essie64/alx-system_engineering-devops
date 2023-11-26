# Kill process
exec {'kill-killmenow':
  command => 'pkill killmenow',
  path    => '/usr/bin';
}
