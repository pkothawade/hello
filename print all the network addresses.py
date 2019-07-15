# print all the network addresses for 192.168.2.0/28 using python
import ipaddress
v4nets = list(ipaddress.ip_network('192.168.2.0/24').subnets(new_prefix=28))
for x in v4nets:
    print (x.with_prefixlen)
