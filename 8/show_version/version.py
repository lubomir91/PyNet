import re

def version_check(data):
    re_data = re.search(r', Version (.+?),', data)
    if re_data:
        return_val = re_data.group(1)
        return return_val

    else:
        return None

    



if __name__ == '__main__':
    with open('C:\\projects\\pynet\\8\\show_version.txt') as f:
        show_version_data = f.read()

        version = version_check(show_version_data)
        print(version)
        
        
#        re_data = re.search(r', Version (.+?),', show_version_data)

#        if re_data:
#            return_val = re_data.group(1)
#            print(return_val)
#
#       else:
#            return_val = None
#            print('None')
#



    
