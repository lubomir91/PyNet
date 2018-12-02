'''
From this output, create a list where each element in the list is a tuple consisting of (interface_name, ip_address, status, protocol).  Only include interfaces that are in the up/up state.
Print this list to standard output.
'''

import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10          YES     NVRAM       up          up
NVI0                  6.9.4.10          YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

# create emply list so it can be used for .append()
show_ip_list = []

# split string on new lines
each_string = show_ip_int_brief.split('\n')

# Iterate over each of the lines in the 'show ip int brief'
for line in each_string:

    # Skip the header line
    if 'Interface' in line:
        continue
    
    # Break line into words
    line_split = line.split()

    # Filter out lines that don't have the correct number of fields
    if len(line_split) == 6:
        
        # map these variables to the fields in the line_split list        
        if_name, ip_addr, discard1, discard2, line_status, line_proto = line_split

        # here if you append more than 1 variable appened stuff become tuple
        if(line_status == 'up') and (line_proto == 'up'):
            show_ip_list.append((if_name, ip_addr, line_status, line_proto))


print('\n')
pprint.pprint(show_ip_list)         

        
