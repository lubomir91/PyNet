'''
5. Write a program that prompts a user for an IP address, then
checks if the IP address is valid, and then converts the IP address
to binary (dotted decimal format).  Re-use the functions created in
exercises 3 and 4 ('import' the functions into your new program).

'''


import sys
import l6ex3
import l6ex4

user_ip = ''

#if l6ex3.ip_checker(user_ip):

while True:
    user_ip = input('Enter IP address to by converted: ')
    if l6ex3.ip_checker(user_ip):
        break
    else:
        print('Entered IP is not correct try again.')
        continue
    
        


user_output =l6ex4.converter(user_ip)
print('\nThis IP in binary is:\n{}'.format(user_output))






