echo 'This is a script. Hello!'
echo  Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo HOME Dir: $HOME

a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo My IP is $a
