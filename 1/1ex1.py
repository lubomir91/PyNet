

ipv6 = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'

hex1 = ipv6.split(':')
print('Hex qroups are {0}'.format(hex1))

renew_ipv6 = ':'.join(hex1)
print('\nIpv6 address is: {0}'.format(renew_ipv6))

exit()