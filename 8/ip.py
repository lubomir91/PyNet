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

def ip_checker(in_ip):
    octets = in_ip.split('.')
    
    if len(octets) != 4:
        #print('Not valid IP address. it must contain 4 octets')
        return False
        
    elif (octets[3] == ''):
        #print('Not valid IP address. it must contain 4 octets')
        return False

    # convert octet from string to int
    for i, octet in enumerate(octets):

        try:
            octets[i] = int(octet)
        except ValueError:
            # couldn't convert octet to an integer
            return False
        
    if (int(octets[0]) < 1) or (int(octets[0]) > 223):
        #print('Not valid 1st octet. It must between 1-223')
        return False

    elif (int(octets[1]) < 1) or (int(octets[1]) > 255):
        #print('Not valid 2nd octet. It must between 1-255')
        return False

    elif (int(octets[2]) < 1) or (int(octets[2]) > 255):
        #print('Not valid 3rd octet. It must between 1-255')
        return False
    
    elif (int(octets[3]) < 1) or (int(octets[3]) > 255):
        #print('Not valid 4th octet. It must between 1-255')
        return False

    else:
        return True





# Technique to allow importable and executable code to coexist (will explain in class#8)
if __name__ == '__main__':

    # Create a bunch of test cases
    test_ip_addresses = {
        '192.168.1'     :   False,
        '10.1.1.'       :   False,
        '10.1.1.x'      :   False,
        '0.77.22.19'    :   False,
        '-1.88.99.17'   :   False,
        '241.17.17.9'   :   False,
        '127.0.0.1'     :   False,
        '169.254.1.9'   :   False,
        '192.256.7.7'   :   False,
        '192.168.-1.7'  :   False,
        '10.1.1.256'    :   False,
        '1.1.1.1'       :   True,
        '223.255.255.255':  True,
        '223.0.0.0'     :   True,
        '10.200.255.1'  :   True,
        '192.168.17.1'  :   True,
    }


    # Run the test cases
    for ip, expected_return in test_ip_addresses.items():
        #print(ip_checker(ip))

        # Make the output format nicer
        dots_to_print = (25 - len(ip)) * '.'

        if ip_checker(ip) is expected_return:
            if expected_return:
                #print "Testing %s %s %s" % (ip, dots_to_print, 'valid')
                print('testing {} {} valid'.format(ip, dots_to_print))
            else:
                #print "Testing %s %s %s" % (ip, dots_to_print, 'invalid')
                print('testing {} {} invalid'.format(ip, dots_to_print))
        else:
            #print "Testing %s %s %s" % (ip, dots_to_print, 'test failed')
            print('testing {} {} test failed'.format(ip, dots_to_print))
