'''
III. Create a program that converts the following uptime strings to a time in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device name as the key.
Print the dictionary to standard output.
'''


import pprint
uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
uptime2 = '3750RJ uptime is 1 hour, 29 minutes'
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

years = 0
device_db = {}

# outside loop for each strig processing
for i in [uptime1, uptime2, uptime3, uptime4]:
    (device_name, uptime) = i.split(' uptime is ')
    uptime_sec = uptime.split(',')
    #print(uptime_sec)

    #internal loop for converting time into pure seconds counter
    for m in uptime_sec:
        m = m.strip()
        if 'year' in m:
            years = m.split(' year')[0]
            #print(years)

        if 'week' in m:
            weeks = m.split(' week')[0]
            #print(weeks)

        if 'day' in m:
            days = m.split(' day')[0]
            #print(days)
        
        if 'hour' in m:
            hours = m.split(' hour')[0]
            #print(hours)

        if 'minute' in m:
            minutes = m.split(' minute')[0]
            #print(minutes)

    #except Value error in case str in not possible to convert into integer 
    try:
        uptime_final = int(years)*365*24*60*60 + int(weeks)*7*24*60*60 + int(days)*24*60*60 + int(hours)*60*60 + int(minutes)*60
        device_db[device_name] = uptime_final
    except ValueError:
        print('ValueError for converting str to int.')
   
pprint.pprint(device_db)
