'''
1. Create a function that returns the multiplication product of
three parameters (x, y, z).  z should have a default value of 1.

    a. Call the function with all positional arguments.

    b. Call the function with all named arguments.

    c. Call the function with a mix of positional and named
arguments.

    d. Call the function with only two arguments and use the
default value for z.

'''


def a_product(x, y, z=1):
    '''
    Simple function that returns the product of three numbers
    '''
    return x*y*z


# 1a (positional args)
print (a_product(3, 4, 5))

# 1b (named args)
print (a_product(z=5, y=4, x=3))

# 1c (mix of positional and named)
print (a_product(3, z=5, y=4))

# 1d (call with only two args)
print (a_product(3, 4))
