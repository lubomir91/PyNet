'''
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.
    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.

    For output, print the IP and whether it is valid or not.
'''

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

try:
    for p,v in enumerate(octets):
        
        print('To many argument')
    else:
        print('You have passed in IP address:{0}'.format(sys.argv[1]))
except ValueError:
    print('Missing argument')
    sys.exit()





if len(octets) != 4:
    print('Not valid IP address. it must contain 4 octets')
    sys.exit()

if (int(octets[1]) < 2) or (int(octets[0]) > 223):
    print('Not valid 1st octet. It must between 1-223')
    sys.exit()




    
