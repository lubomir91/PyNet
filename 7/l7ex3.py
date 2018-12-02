'''
3.  In the following directory there is a file 'ospf_data.txt':
This file contains the output from 'show ip ospf interface'.
Using functions and regular expressions parse this output to display the following (note, I ended up using re.split() as part of the solution to this problem):
Int:     Loopback0
IP:     10.90.3.38/32
Area: 30395
Type: LOOPBACK
Cost: 1

Int:     GigabitEthernet0/1
IP:      172.16.13.150/29
Area:  30395
Type:  BROADCAST
Cost:  1
Hello: 10
Dead: 40
'''

import re
import pprint

def ospf_parser(pattern,f_data):

    re_output = re.search(pattern,f_data)

    if re_output:
        return_val = re_output.group(1)
        return return_val
    return None


def separate_int_data(data_in):
    ospf_list = []
    parsed_data = re.split(r'(.+? is up, line protocol is up)', data_in)
    parsed_data.pop(0)
    while True:
        if len(parsed_data) >= 2:
            intf = parsed_data.pop(0)
            ospf_payload = parsed_data.pop(0)
            ospf_int = intf + ospf_payload
            ospf_list.append(ospf_int)
                
        else:
            break

    return ospf_list

def nice_print(print_data):
    for name, value in print_data.items():
        aligment = (6- len(name))*(' ')
        print('{0}{1}: {2}'.format(name,aligment,value))
    print('\n')
    
    return 


if __name__ == '__main__':

    with open('C:\\projects\\pynet\\7\\OSPF_DATA\\ospf_data.txt') as f:
        #read a file as a string
        ospf_data = f.read()

        data = {}
        #call a funcion and split ospf data per interface
        ospf_list = separate_int_data(ospf_data)

        # definy dic with name:search pattern
        ospf_intf_patterns = {
            'Int'   : r'(.+?) is up',
            'Area'  : r'Area (.+),',
            'Type'  : r'Network Type (.+?),',
            'Cost'  : r'Cost: (.+)',
            'Hello' : r'Hello (.+?),',
            'Dead'  : r'Dead (.+?),',
            'IP'  : r'Internet Address (.+?),',
            
            }

        # outside loop - iterate each interface data in ospf_list 
        for i in ospf_list:
            #inside loop, interate search for each regex pattern 
            for name, pattern in ospf_intf_patterns.items():
                return_value = ospf_parser(pattern, i)
                # if regex did not found a match, funcion return None
                if return_value is not None:
                    #otherwise save data as value to key-name
                    data[name] = return_value

            nice_print(data)
            
        

            

        

        
