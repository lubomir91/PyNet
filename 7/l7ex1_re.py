import re
import pprint
from glob import glob


def cdp_parser(search_pattern,data):

    re_output = re.search(search_pattern,data)

    if re_output:
        return_val = re_output.group(1)
        return return_val
    
    return ''


if __name__ == '__main__':
    
    cdp_files = glob('C:\\projects\\pynet\\7\\CDP_DATA\\*cdp.txt')
    
    for file in cdp_files:
        cdp_file_location = file

        #savetly open a file
        with open(cdp_file_location) as f:
            #open a file as one string
            cdp_data = f.read()
        
            network_devices = {}

            network_devices['hostname'] =  cdp_parser(r'Device ID: (.+)', cdp_data)
            network_devices['IP address'] =  cdp_parser(r'IP address: (.+)', cdp_data)
            network_devices['Vendor'] =  cdp_parser(r'Platform: (.+?) ', cdp_data)
            network_devices['Model'] = cdp_parser(r'Platform: \w+ (.+),', cdp_data)
            network_devices['Device_type'] = cdp_parser(r'Platform: .+Capabilities: (.+?) ',cdp_data)


            pprint.pprint(network_devices)
            print('\n')
