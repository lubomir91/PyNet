import pprint
network_devices = {}

with open('C:\\projects\\pynet\\7\\CDP_DATA\\r1_cdp.txt') as f:


    #loop #1 to fulfil a dict 
    for line in f.readlines():
        
        lines = line.split('\n')
    
        for i in lines:
            
            #device ID - name
            if('Device ID:') in i:
                a = i.split('Device ID: ')[1]
                if ('(') in a:
                    a = a.split('(')[0]
                elif ('.') in a:
                    a = a.split('.')[0]
                network_devices[a] = {}

            #IP address
            if('IP address:') in i:
                b = i.split('IP address: ')[1]
                network_devices[a]['ip'] = b
                
            #model
            if('Platform: ') in i:
                 b = (i.split('Platform: ')[1]).split(' Capabilities:')[0]
                 if (',') in b:
                     b = b.split(',')[0]
                 network_devices[a]['model'] = b

            #vendor
            if('Cisco') in i:
                network_devices[a]['vendor'] = 'Cisco'

            #device_type
            if('Capabilities:') in i:
                if ('Router') in i:
                    network_devices[a]['device_type'] = 'Router'
                elif ('Switch') in i:
                    network_devices[a]['device_type'] = 'Switch'
                else:
                    network_devices[a]['device_type'] = 'unknown'
    

pprint.pprint(network_devices)
