# A puppet manifest that kills a process named killmenoe
exec { 'killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true
}

