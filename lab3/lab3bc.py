# Jeongyoon Jessica Choi PS 3

# B.1
def list_reverse(lst):
    ''' Takes a list and returns the reverse of the list without modifying the original '''
    lst2 = lst[:]
    lst2.reverse()
    return lst2

# B.2
def list_reverse2(lst):  
    ''' Takes a list and returns the reverse of the list without modifying the original '''
    lst2 = []
    x = len(lst)
    for i in range(1, x+1):
        lst2.insert(0, lst[i-1])
    return lst2


# B.3
def file_info(text_file):
    ''' Takes a text file and returns the number of lines, words, and characters in the file as a tuple (lines, words, characters) '''
    line_counter = 0
    word_counter = 0
    character_counter = 0
    f = open(text_file, 'r')
    while True:
        line = f.readline()
        if line != '':
            line_counter += 1
            word_counter += len(line.split())
            character_counter += len(line)
    f.close()
    tuple1 = (line_counter, word_counter, character_counter)
    return tuple1

# B.4
def file_info2(text_file):
    ''' Takes a text file and returns the number of lines, words, and characters in the file as a dictionary (lines, words, characters) '''
    tup = file_info(text_file)
    (line_counter, word_counter, character_counter) = tup
    new_dict = { 'lines' : line_counter,
              'words' : word_counter,
              'characters' : character_counter}
    return new_dict


# B.5
def longest_line(text_file):
    ''' Takes the name of a text file and returns a tuple (length, line) of the longest line '''
    f = open(text_file, 'r')  
    line = f.readline()
    length = 0
    line2 = ''
    for line in text_file:
        if len(line) > length:
            length = len(line)
            line2 = line
        elif line == '':
            break
    new_tup = (length, line2)
    f.close()
    return new_tup


# B.6
def sort_words(string):
    ''' Takes a string and returns the sorted list of words in the string'''
    lst = string.split( )
    sorted_list = lst.sort
    return sorted_list
    
    
# B.7
# 0 * 2^0 + 1 * 2^1 + 0 * 2^2 + 1 * 2^3 + 1 * 2^4 + 0 * 2^5 + 1 * 2^6 + 1 * 2^7 = 218
# The largest 8 digit binary number is 11111111.
# Its value in decimal is 2^8 - 1 = 255

# B.8
def binaryToDecimal(lst):
    x = len(lst)
    total = 0
    lst2 = list_reverse(lst)
    for i in range(1, x+1):
        y = lst2[i-1] * 2 ** (i-1)
        total += y
    return total


# C.2.1
# Bad name because it isn't clear what sc means.
# No operator space
# Should calculate the sum before returning it
def sum_of_cubes(a, b, c):
    total = a * a * a + b * b * b + c * c * c
    return sum_of_cubes

# C.2.2
# Bad names because they are too wordy
# The calculation shouldn't occur in the return
# Comment should be after the function, not before
# Spacing and spelling should be consistent even in comments
# Should limit lines to 80 characters
# For multiple word names, should make it clear where the boundaries are
def sum_of_cubes(a, b, c, d):
    total = a * a * a + b * b * b + c * c * c + d * d * d
    return total

# C.2.3
# Indentation is incorrect for the return in both functions.
# Functions should be separated by blank lines.
def sum_of_squares(x, y):
    return x * x + y * y

def sum_of_three_cubes(x, y, z):
    return x * x * x + y * y * y + z * z * z