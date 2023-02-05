#import the necessary modules
import os
import socket

#input the network and subnet mask
network = input('Enter the network address: ')
subnet_mask = input('Enter the subnet mask: ')

#generate the network address
net = socket.inet_aton(network)
mask = socket.inet_aton(subnet_mask)
net_addr = socket.inet_ntoa(net & mask)

#generate the list of hosts
host_list = []
for i in range(1,256):
    addr = socket.inet_ntoa(net | ~mask & 0xffffffff | i)
    host_list.append(addr)

#ping each host
for host in host_list:
    response = os.system('ping -c 1 ' + host + ' > /dev/null')
    if response == 0:
        print(host + ' is up!')
    else:
        print(host + ' is down!')