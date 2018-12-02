
def nice_print(print_data):
    for name, value in print_data.items():
        aligment = (9- len(name))*(' ')
        print('{0}{1}: {2}'.format(name,aligment,value))
    print('\n')
    
    return 
