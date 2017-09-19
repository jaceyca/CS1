# Jeongyoon Jessica Choi PS2
import random

# D.1
def make_random_code():
    ''' Takes no args and returns a string of 4 characters made of R, G, B, Y, O, or W. Duplicates are allowed. '''
    choices = ['R', 'G', 'B', 'Y', 'O', 'W']
    string = ''
    for x in range(0 , 4):
        string += random.choice(choices)
    return string

# D.2
def count_exact_matches(str1, str2):
    ''' Given two strings, counts the number of places where both strings have the exact same letter in the same exact location. '''
    matches = 0
    for i in range(0 , 4):
        if str1[i] == str2[i]:
            matches += 1
    return matches

# D.3
def count_letter_matches(str1, str2):
    ''' Given two strings, counts the number of letters that the two strings share, regardless of order '''
    lst1 = list(str1)
    lst2 = list(str2)
    counter = 0
    for x in lst2:
        for y in lst1:
            if x == y:
                counter += 1
                lst1.remove(y)
    return counter

# D.4
def compare_codes(code, guess):
    ''' Takes two strings of length 4 and compares how many exact and letter matches are. Based on the matches, it returns a string of 4 letters made of b, w, and - that explains how closely the two strings matched '''
    black = count_exact_matches(code, guess)
    white = count_letter_matches(code, guess) - black
    blank = 4 - black - white
    string = black * 'b' + white * 'w' + blank * '-'
    return string

# D.5
def run_game():
    ''' Runs the game Mastermind using the different functions written previously. Doesn't take any args, and asks for user input at times. '''
    print 'New game.'
    secret_code = make_random_code()
    counter = 0
    result = ''
    while result != 'bbbb':
        guess = raw_input('Enter your guess: ')
        print guess
        result = compare_codes(secret_code, guess)
        print 'Result: %s' % result
        counter += 1
    print 'Congratulations! You cracked the code in %d moves!' % counter
    
# D.6
# Tested with lab2b_tests.py