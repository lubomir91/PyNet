'''
4. Create a function using your dotted decimal to binary conversion
code from Class3, exercise1.  In the function--do not prompt for
input and do not print to standard output.  The function should
take one variable 'ip_address' and should return the IP address in
dotted binary format always padded to eight binary digits (for
example, 00001010.01011000.00010001.00010111).  You might want to
create other functions as well (for example, the zero-padding to
eight binary digits).

'''
ip_addr = '12.15.10.166'
def converter(ip_addr):
    octets = ip_addr.split('.')
    octets_bin = []
    octets_hex = []

    for i in octets:
        o = bin(int(i))[2: ]
        h = hex(int(i))[2: ]
        octets_bin.append(o)
        octets_hex.append(h)

#print('\n\tfirst_octet\tsecond_octet\tthird_octet\tfourth_octet')
#print('dec\t{0}\t\t{1}\t\t{2}\t\t{3}'.format(octets[0], octets[1], octets[2], octets[3]))
#print('bin\t{0}\t{1}\t{2}\t{3}'.format(octets_bin[0], octets_bin[1], octets_bin[2], octets_bin[3]))
#print('hex\t{0}\t\t{1}\t\t{2}\t\t{3}'.format(octets_hex[0], octets_hex[1], octets_hex[2], octets_hex[3]))

    print(octets_bin)
    return octets_bin





