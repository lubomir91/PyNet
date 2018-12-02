import sys
from pprint import pprint 

#sys.path.append('C:\projects\pynet\8\show_version')

#import version
#import uptime
#import model

import show_version






if __name__ == '__main__':
    with open('C:\\projects\\pynet\\8\\show_version.txt') as f:
        show_data = f.read()

        values = {}

        values['version'] = show_version.version.version_check(show_data)
        values['model'] = show_version.model.model_check(show_data)
        values['uptime'] = show_version.uptime.uptime_check(show_data)
        show_version.nprint.nice_print(values)
