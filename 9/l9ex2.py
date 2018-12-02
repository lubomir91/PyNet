'''
II. Create an Uptime class that takes in a Cisco IOS uptime string and parses the string into years, weeks, days, hours, minutes (assigning these as attributes of the object).  For example:

>>> test_obj = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes')
>>> test_obj.years
0
>>> test_obj.weeks
6
>>> test_obj.days
4
>>> test_obj.hours
2
>>> test_obj.minutes
25

'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'
'3750RJ uptime is 1 hour, 29 minutes'
'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'
'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'
'''
import re

class Uptime(object):
    def __init__(self, up_str):
        self.up_str = up_str

    def years(self):
        years = 0
        time = self.up_str.split('uptime is ')
        time_split = time[1].split(', ')
        for v in time_split:
            if 'year' in v:
                years = v.split(' year')[0]
              
        return years

    def weeks(self):
        weeks = 0
        time = self.up_str.split('uptime is ')
        time_split = time[1].split(', ')
        for v in time_split:
            if 'week' in v:
                weeks = v.split(' week')[0]
              
        return weeks

    def days(self):
        days = 0
        time = self.up_str.split('uptime is ')
        time_split = time[1].split(', ')
        for v in time_split:
            if 'day' in v:
                days = v.split(' day')[0]
              
        return days


    def hours(self):
        hours = 0
        time = self.up_str.split('uptime is ')
        time_split = time[1].split(', ')
        for v in time_split:
            if 'hour' in v:
                hours = v.split(' hour')[0]
              
        return hours

    def minutes(self):
        minutes = 0
        time = self.up_str.split('uptime is ')
        time_split = time[1].split(', ')
        for v in time_split:
            if 'minute' in v:
                minutes = v.split(' minute')[0]
              
        return minutes


test_obj = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 35 minutes')


print(test_obj.up_str)
print('Years: {}'.format(test_obj.years()))
print('Weeks: {}'.format(test_obj.weeks()))
print('Days: {}'.format(test_obj.days()))
print('Hours: {}'.format(test_obj.hours()))
print('Minutes: {}'.format(test_obj.minutes()))

        #a = re.search(r'(.) weeks,',self.up_str)
        #years = a.group(1)


