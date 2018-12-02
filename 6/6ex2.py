'''
2. Write a function that converts a list to a dictionary where the
index of the list is used as the key to the new dictionary (the
function should return the new dictionary).

'''

def list_to_dict(x):
    new_dict = {}
    for k,v in enumerate(x):
        new_dict[k] = v

    return new_dict

#test list
test_list = range(0,11)


test_dict = list_to_dict(test_list)

print('\n{}'.format(test_list))
print('\n{}'.format(test_dict))
