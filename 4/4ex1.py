import sys

# IP address validation #

while True:
    in_ip = input('Enter IP: ')
    octets = in_ip.split('.')
    
    if len(octets) != 4:
        print('Not valid IP address. it must contain 4 octets')
        continue
        
    elif (octets[3] == ''):
        print('Not valid IP address. it must contain 4 octets')
        continue
    
    elif (int(octets[0]) < 1) or (int(octets[0]) > 223):
        print('Not valid 1st octet. It must between 1-223')
        continue

    elif (int(octets[1]) < 1) or (int(octets[1]) > 255):
        print('Not valid 2nd octet. It must between 1-255')
        continue

    elif (int(octets[2]) < 1) or (int(octets[2]) > 255):
        print('Not valid 3rd octet. It must between 1-255')
        continue

    elif (int(octets[3]) < 1) or (int(octets[3]) > 255):
        print('Not valid 4th octet. It must between 1-255')
        continue

    else:
        print('You have passed in IP address:{0}\n'.format(in_ip))
        break

sys.exit()
