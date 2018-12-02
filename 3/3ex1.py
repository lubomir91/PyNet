import sys
try:
    if len(sys.argv) > 2:
        print('To many argument')
    else:
        print('You have passed in IP address:{0}'.format(sys.argv[1]))
except IndexError:
    print('Missing argument')
    sys.exit()


octets = sys.argv[1].split('.')
octets_bin = []
octets_hex = []

for i in octets:
    o = bin(int(i))[2: ]
    h = hex(int(i))[2: ]
    octets_bin.append(o)
    octets_hex.append(h)

print('\n\tfirst_octet\tsecond_octet\tthird_octet\tfourth_octet')
print('dec\t{0}\t\t{1}\t\t{2}\t\t{3}'.format(octets[0], octets[1], octets[2], octets[3]))
print('bin\t{0}\t{1}\t{2}\t{3}'.format(octets_bin[0], octets_bin[1], octets_bin[2], octets_bin[3]))
print('hex\t{0}\t\t{1}\t\t{2}\t\t{3}'.format(octets_hex[0], octets_hex[1], octets_hex[2], octets_hex[3]))
