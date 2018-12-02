'''
3a. Convert the IP address validation code (Class4, exercise1) into
a function, take one variable 'ip_address' and return either True
or False (depending on whether 'ip_address' is a valid IP).  Only
include IP address checking in the function--no prompting for
input, no printing to standard output.

3b. Import this IP address validation function into the Python
interpreter shell and test it (use both 'import x' and 'from x
import y').
'''

# IP address validation #
in_ip = '192.165.1.500'

def ip_checker(in_ip):
    octets = in_ip.split('.')
    
    if len(octets) != 4:
        print('Not valid IP address. it must contain 4 octets')
        return False
        
    elif (octets[3] == ''):
        print('Not valid IP address. it must contain 4 octets')
        return False
    
    elif (int(octets[0]) < 1) or (int(octets[0]) > 223):
        print('Not valid 1st octet. It must between 1-223')
        return False

    elif (int(octets[1]) < 1) or (int(octets[1]) > 255):
        print('Not valid 2nd octet. It must between 1-255')
        return False

    elif (int(octets[2]) < 1) or (int(octets[2]) > 255):
        print('Not valid 3rd octet. It must between 1-255')
        return False
    
    elif (int(octets[3]) < 1) or (int(octets[3]) > 255):
        print('Not valid 4th octet. It must between 1-255')
        return False

    else:
        return True


