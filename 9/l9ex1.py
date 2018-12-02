'''
I. Create a Python class representing an IPAddress.  
The class should have only one initialization variable--an IP address in dotted decimal formation.  
You should be able to do the following with your class:

>>> test_ip = IPAddress('192.168.1.1')
>>> test_ip.ip_addr
'192.168.1.1'

    A. Write a method for this class that returns the IP address in dotted binary format (each octet should be eight binary digits in length).

>>> test_ip.display_in_binary()
'11000000.10101000.00000001.00000001'

    B. Write a method for this class that returns the IP address in dotted hex format (each octet should be two hex digits in length).

>>> test_ip.display_in_hex()
'c0.a8.01.01'

    C. Re-using the IP address validation code from class8, exercise1--create an is_valid() method that returns either True or False depending on whether the IP address is valid.

>>> test_ip.is_valid()
True
'''


class IPAddress(object):
    #simple method to initialize a variable inside of class
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

    # method to return IP address in binary
    def display_in_binary(self):
        octets = []
        octets_bin = []
        octets = self.ip_addr.split('.')

        # funcion to delete '0b' and add '0' at the end
        for v in octets:
            octet = (bin(int(v))).split('0b')[1]
            if len(octet) < 8:
                octet = ('0' * (8 - len(octet))) + octet
                
            #append each bin octet at the end of list
            octets_bin.append(octet)

            #make from list one string bin IP
            ip_bin = ('.').join(octets_bin)
            
        #return final list of octets
        return ip_bin

    #method changing IP into HEX and return in as single strig
    def display_in_hex(self):
        octets = self.ip_addr.split('.')
        octets_hex = []
        for v in octets:
            octets_hex.append((hex(int(v))).split('0x')[1])
        ip_hex = ('.').join(octets_hex)
        return ip_hex


    def is_valid(self):
        octets = self.ip_addr.split('.')
    
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
        

if __name__ == '__main__':
    # I. Create a Python class representing an IPAddress. 
    test_ip = IPAddress('200.220.198.105')
    print('test_ip.ip_addr')
    print(test_ip.ip_addr)

    #A. Write a method for this class that returns the IP address in dotted binary format (each octet should be eight binary digits in length).
    print('\nIPAddress.display_in_binary')
    print(test_ip.display_in_binary())

    #B. Write a method for this class that returns the IP address in dotted hex format (each octet should be two hex digits in length).
    print('\nIPAddress.display_in_hex')
    print(test_ip.display_in_hex())

    #C. Re-using the IP address validation code from class8, exercise1--create an is_valid() method that returns either True or False depending on whether the IP address is valid.
    print('\ntest_ip.is_valid')
    print(test_ip.is_valid())

                    
