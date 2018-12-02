'''
II. Parse the below 'show version' data and obtain the following items (vendor, model, os_version, uptime, and serial_number).
Try to make your string parsing generic i.e. it would work for other Cisco IOS devices. 
Store these variables (vendor, model, os_version, uptime, and serial_number) in a dictionary.  Print the dictionary to standard output when done.

The following are reasonable strings to look for:

'Cisco IOS Software' for vendor and os_version
'bytes of memory' for model
'Processor board ID' for serial_number
' uptime is ' for uptime
'''

import pprint

data = '''
>>>>> show version data <<<<<
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: 
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes
System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102
>>>>> end <<<<<
'''
# define empty list is enough
devices = {}
#devices = {'vendor':'', 'model':'', 'os_version':'', 'uptime':'','serial_number':''}

# split show version output into lines
lines = data.split('\n')

# Iterate over the show version data line by line
for i in lines:

    if 'Cisco IOS Software' in i:
        devices['vendor']='Cisco'
        devices['os_version']=(i.split('Version')[1]).split(',')[0]

    if 'bytes of memory' in i:
        devices['model']=(i.split()[0]) + (i.split()[1])

    if 'Processor board ID' in i:
        devices['serial_number']=i.split('Processor board ID ')[1]

    if 'uptime is' in i:
        devices['uptime']=i.split(' uptime is ')[1]

pprint.pprint(devices)
        
