ip = '192.168.100.200'

octets = ip.split('.')
octets_bin = []

for i in octets:
	octets_bin.append(bin(int(i)))

print('\nfirst_octet\tsecond_octet\tthird_octet\tfourth_octet')
print('{0}\t{1}\t{2}\t{3}'.format(octets_bin[0], octets_bin[1], octets_bin[2], octets_bin[3]))