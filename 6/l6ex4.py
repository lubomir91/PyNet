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
# funcion to for paddding '0' at the end until 8 char
def pad_binary_digits(octet):
    while True:
        if len(octet) >= 8:
            break
        
        octet = '0' + octet
    return octet

# main funcion for converting 
def converter(ip_addr):
    octets = ip_addr.split('.')
    octets_bin = []
    octets_hex = []

    for i in octets:
        o = bin(int(i))[2: ]
        o = pad_binary_digits(o)
        octets_bin.append(o)
        #h = hex(int(i))[2: ]
        #octets_hex.append(h)

    octets_bin = '.'.join(octets_bin)
    return octets_bin


   
# run a test
''' 
if __name__ == '__main__':
    # Create a bunch of test cases
    test_ip_addresses = [
        '1.1.1.1',
        '223.255.255.255',
        '223.255.254.252',
        '223.248.240.224',
        '192.128.3.7',
        '223.0.0.0',
        '10.200.255.1',
        '192.168.17.1',
    ]

for ip in test_ip_addresses:
    print(converter(ip))
'''


