# B.1.1:
def union(set1, set2):
    '''Takes two sets and returns a set of their union'''
    union = set()
    for i in set1:
            union.add(i)
    for i in set2:
            union.add(i)
    return union

# B.1.2:
def intersection(set1, set2):
    '''Takes two sets and returns a set of their intersection.'''
    intersection = set()
    for i in set1:
        if i in set2:
            intersection.add(i)
    return intersection

# B.2:
def mySum(*ints):
    '''Takes an arbitrary number of arguments, all ints greater than zero,
    and returns their sum '''
    total = 0
    for i in ints:
        if i <= 0:
            raise ValueError('All arguments must be greater than 0.')   
        if type(i) is not int:
            raise TypeError('All arguments must be integers.')        
        total += i
    return total
    
# Ex B.3:
def myNewSum(*z):
    '''This function takes single list of positive integers and returns their
    sum.'''
    total = 0
    counter = 0
    for ele in z:
        counter += 1
    if counter == 1:
        if type(ele) is list:
            for ele2 in z[0]:                  
                if type(ele2) is not int:
                    raise TypeError('All arguments must be integers.')
                else:
                    if ele2 < 1:
                        raise ValueError('All arguments must be >= 1.')
                    else:
                        total += ele2
        elif type(ele) is int:
            if ele < 1:
                raise ValueError('All arguments must be >= 1.')
            else:
                total += ele             
    else:
        for ele in z:
            if type(ele) is not int:
                raise TypeError('Arguments must be single list of integers.')
            else:
                if ele < 1:
                    raise ValueError('All arguments must be >= 1.')
                else:
                    total += ele                    
    return total
# Ex B.4:
def myOpReduce(l1, **kw):
    '''This function takes one list of integers and one keyword argument 'op' of
    string type and return sum if op == '+' total value multiplied if op == '*'
    and max value of the list if op == 'max'.'''
    total = 0
    if len(kw) == 0:
        raise ValueError('No keyword arugment.')
    elif len(kw) > 1:
        raise ValueError('Too many keywork arguments.')    
    else:
        for ele in kw:
            if ele is not 'op':
                raise ValueError('Invalid keyword argument.')
            else:
                if kw[ele] is '+':
                    for ele in l1:
                        total += ele
                elif kw[ele] is '*':
                    total = 1
                    if len(l1) > 0:
                        for ele in l1:
                            total *= ele
                elif kw[ele] is 'max':
                    if len(l1) > 0:
                        total = l1[0]
                        for ele in l1:
                            if ele > total:
                                total = ele
                else:
                    if type(kw[ele]) is str:
                        raise ValueError('Ialid keyword argument.')
                    else:
                        raise TypeError('Value for keyword argument "op"' \
                        'must be a string.')
    return total
                    
                
    
# Ex C.1:
# Quitting the system when the KeyError occurs will cause error because
# there are no ongoing system to quit in this case. SystemExit type is None.
import sys
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        return dict[key1] + dict[key2]
    except KeyError:   
        print 'Invalid key input.'

# Ex C.2:
# If the keys are not in the dictionary than the error should be raised.
# Not handled with try, except and print in sys.stderr
import sys
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    if key1 or key2 not in dict.keys():
        raise KeyError('key not found!')
    return dict[key1] + dict[key2]

# Ex C.3:
# There is no reason to raise key error when the exception was already found.
# Instead we can just do the same thing as C.2.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    if key1 or key2 not in dict.keys():
        raise KeyError('key not found!')
    return dict[key1] + dict[key2]

# Ex C.4:
# There are no needs to have try and except statement twice. Also, there is no
# reason to store the keys into separate values and return the sum of those
# values.
def sum_of_key_values(dict, key1, key2):
    '''Return the sum of the values in the dictionary stored at key1 and key2.'''
    try:
        dict[key1]
        dict[key2]
    except KeyError, e:   
        raise e
    return dict[key1] + dict[key2]

# Ex C.5:
# There is no reason to raise ValueError then print the error message in
# sys.stderr separately. Instead, you can just do it all at once.
import sys
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0.')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex C.6:
# Same as the previous question, there is no reason to print the error message
# than raise ValueError. You can easily do it like the previous question.
import sys
def fib(n):
    '''Return the nth fibonacci number.'''
    if n < 0:
        raise ValueError('n must be >= 0.')
    elif n < 2:
        return n  # base cases: fib(0) = 0, fib(1) = 1.
    else:
        return fib(n-1) + fib(n-2)

# Ex C.7
# It is better to name the type of the error as ValueError, not TypeError
# because it is still a type of number even though the value is not appropriate.
from math import exp
def exp_x_over_x(x):
    '''Return the value of e**x / x, for x > 0 and 
    e = 2.71828... (base of natural logarithms).'''
    if x < 0:
        raise ValueError('x must be >= 0.0')
    return (exp(x) / x)

# Ex C.8:
# The error type exception is not specific enough. It is possible to change the
# name of the error type to give better idea of the error.
from math import exp
def exp_x_over_x(x):
    '''Return the value of e**x / x, for x > 0 and
    e = 2.71828... (base of natural logarithms).'''
    if type(x) is not float:
        raise TypeError('x must be a float')
    elif x <= 0:
        raise ValueError('x must be > 0.0')
    return (exp(x) / x)