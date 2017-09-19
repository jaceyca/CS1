# Jessica Choi, CS 1
import Tkinter
import random

def random_size(x, y):
    ''' Takes 2 non-negative even integers x and y, where x is less than y and
    returns a random even integer between the 2 numbers '''
    assert x >= 0 and x % 2 == 0
    assert y >= 0 and y % 2 == 0
    assert x < y
    output = random.randrange(x, y + 2, 2)
    assert output % 2 == 0
    return output


def random_position(max_x, max_y):
    ''' Takes two non-negative integers max_x and max_y and returns a (x, y)
    tuple where x and y are both non-negative integers '''
    assert max_x >= 0
    assert max_y >= 0
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    assert x >= 0 and x <= max_x
    assert y >= 0 and y <= max_y
    return (x, y)

def random_color():
    ''' Generates random color values in the format of #RRGGBB (hexadecimal
    digits), where the RR represents degree of red, GG represents degree of
    green, and BB represents degree of blue '''
    choices = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
               'd', 'e', 'f')
    string = '#'
    for i in range(6):
        string += random.choice(choices)
    return string

def count_values(dictionary):
    ''' Given a dictionary, this returns the number of distinct values the
    dictionary contains '''
    lst = dictionary.values()
    for x in lst:
        if lst.count(x) > 1:
            lst.remove(x)
    return len(lst)

def remove_value(dictionary, value):
    ''' Given a dictionary and an value, this removes all key/values pairs 
    that have the value. If the value is not in the dictionary, nothing 
    happens '''
    d = []
    lst = dictionary.values()
    for i, j in dictionary.items():
        if j == value:
            d.append(i)
    for key in d:
        del dictionary[key]

def split_dict(dictionary):
    ''' Takes a dictionary which uses strings as keys and returns a tuple of 
    two dictionaries whose keys start with letters a-m and n-z '''
    dicti = {}
    onary = {}
    item = dictionary.items()
    keytest1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm')
    keytest2 = ('n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    for i, j in item:
        if i[0].lower() in keytest1:
            dicti[i] = j
        if i[0].lower() in keytest2:
            onary[i] = j
    return (dicti, onary)


def count_duplicates(dictionary):
    ''' Given a dictionary, it returns the number of values that appear more 
    than once '''
    lst = dictionary.values()
    counter = 0
    values = []
    for x in lst:
        if lst.count(x) > 1 and x not in values:
            counter += 1
            values.append(x)
    return counter
