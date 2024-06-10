# increaing the amount of requests to the server
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}


#restart Nginx server
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
