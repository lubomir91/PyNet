'''
2. In the following directory there is a file 'ospf_single_interface.txt':
Open this file and extract the interface, IP address, area, type, cost, hello timer, and dead timer.
Use regular expressions to accomplish your extraction.
Your output should look similar to the following:

Int:        GigabitEthernet0/1
IP:        172.16.13.150/29
Area:    30395
Type:    BROADCAST
Cost:    1
Hello:   10
Dead:   40
'''

import re
import pprint

def ospf_parser(pattern,f_data):

    re_output = re.search(pattern,f_data)

    if re_output:
        return_val = re_output.group(1)
        return return_val
    return ''


if __name__ == '__main__':

    with open('C:\\projects\\pynet\\7\\OSPF_DATA\\ospf_single_interface.txt') as f:

        ospf_data = f.read()

        data = {}

        data['Int'] = ospf_parser(r'^(.+?) is ', ospf_data)
        data['Area'] = ospf_parser(r'Area (.+),', ospf_data)
        data['Type'] = ospf_parser(r'Network Type (.+?),', ospf_data)
        data['Cost'] = ospf_parser(r'Cost: (.+)', ospf_data)
        data['Hello'] = ospf_parser(r'Hello (.+?),', ospf_data)
        data['Dead'] = ospf_parser(r'Dead (.+?),', ospf_data)
        
        pprint.pprint(data)
        

        
        
