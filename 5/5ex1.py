import pprint

network_devices = {}
from cdp_data import *
cdp_data = [sw1_show_cdp_neighbors_detail, r1_show_cdp_neighbors_detail, r2_show_cdp_neighbors_detail, r3_show_cdp_neighbors_detail, r4_show_cdp_neighbors_detail, r5_show_cdp_neighbors_detail]

#from ixi_cdp_data import *
#cdp_data = [ixi_asr1_show_cdp_neighbors_detail, ixi_asr2_show_cdp_neighbors_detail]

#loop #1 to fulfil a dict 
for data in cdp_data:
    
    lines = data.split('\n')

    for i in lines:
        if('Device ID:') in i:
            a = i.split('Device ID: ')[1]
            if ('(') in a:
                a = a.split('(')[0]
            elif ('.') in a:
                a = a.split('.')[0]
            network_devices[a] = {}

        if('IP address:') in i:
            b = i.split('IP address: ')[1]
            network_devices[a]['ip'] = b

        if('Platform: ') in i:
             b = (i.split('Platform: ')[1]).split(' Capabilities:')[0]
             if (',') in b:
                 b = b.split(',')[0]
             network_devices[a]['model'] = b

        if('Cisco') in i:
            network_devices[a]['vendor'] = 'Cisco'

        if('Capabilities:') in i:
            if ('Router') in i:
                network_devices[a]['device_type'] = 'Router'
            elif ('Switch') in i:
                network_devices[a]['device_type'] = 'Switch'
            else:
                network_devices[a]['device_type'] = 'unknown'

# loop #2 fulfil adjacent_devices list for each device in dict
for data in cdp_data:
    
    lines = data.split('\n')
    adjacent_devices = []
    
    if('show cdp neighbors detail') in data:
        device = (data.split('>')[0]).strip()

    

    for i in lines:
            if('Device ID:') in i:
                a = i.split('Device ID: ')[1]
                if ('(') in a:
                    a = a.split('(')[0]
                elif ('.') in a:
                    a = a.split('.')[0]
                adjacent_devices.append(a)
        

# add key:value adjacent_devices to device in dictionary
# if device key still does not exist create a key:value for a device with empty value and then add adj. devices entry
    try:
        network_devices[device]['adjacent_devices'] = adjacent_devices
    except KeyError:
        network_devices[device] = {}
        network_devices[device]['adjacent_devices'] = adjacent_devices

        
pprint.pprint(network_devices)


