"""
def maximum(x,y):
    if x> y:
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y
    
print(maximum(2,3)) 

"""
#return None

def some_function():
    pass
print(some_function())

#DocString, 설명문자열
"""
def print_max(x,y):
    '''Prints the maximum of two numbers.
    
    The two values must be integers.'''
    x = int(x)
    y = int(y)
    
    if x>y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3,5)
print(print_max.__doc__)
help(print_max)
"""
