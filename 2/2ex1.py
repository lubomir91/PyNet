

in1 = input('Zadaj IP address:')

in1 = in1.split('.')
print(type(in1))
octets = list(in1)

if len(octets) == 3:
	octets.append('0')
elif len(octets) == 4:
	octets[3] = '0'


bin_octet = bin(int(octets[0]))
hex_octet = hex(int(octets[0]))

print('\nOctets are {0}\n'.format(octets))

print('NETWORK_NUMBER\tFIRST_OCTET_BINARY\tFIRST_OCTET_HEX')
print('{0}\t{1}\t\t{2}'.format('.'.join(octets), bin_octet, hex_octet))
