import re

def model_check(data):
    lines = []
    lines = data.split('\n')

    for i in lines:
        if 'bytes of memory.' in i:
            re_data = re.search(r'Cisco (.+?) ', i)
            if re_data:
                return_val = re_data.group(1)
                return return_val

            else:
                return None

    



if __name__ == '__main__':
    with open('C:\\projects\\pynet\\8\\show_version.txt') as f:
        show_version_data = f.read()

        model = model_check(show_version_data)
        print(model)
        
        
#        re_data = re.search(r', Version (.+?),', show_version_data)

#        if re_data:
#            return_val = re_data.group(1)
#            print(return_val)
#
#       else:
#            return_val = None
#            print('None')
#



    
