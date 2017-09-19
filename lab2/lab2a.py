# Jeongyoon Jessica Choi PS 2
import random


# B.1
def complement(DNA):
    ''' Takes a string made of only letters 'A', 'C', 'G', and 'T' and outputs the complement of the string '''
    
    string = ''
    for n in DNA:
        if n == 'A':
            string += 'T'
        if n == 'C':
            string += 'G'
        if n == 'G':
            string += 'C'
        if n == 'T':
            string += 'A'
        
    return string


# B.2
def list_complement(DNA):
    ''' Takes a list made of only letters 'A', 'C', 'G', and 'T' and outputs the complement of the list '''
    for m, n in enumerate(DNA):
        if n == 'A':
            DNA[m] == 'T'
            
        elif n == 'C':
            DNA[m] = 'G'
            
        elif n == 'G':
            DNA[m] = 'C'
            
        elif n == 'T':
            DNA[m] = 'A'
    return DNA


# B.3
def product(nums):
    ''' Takes a list of numbers and outputs the product of the elements in the list'''
    total = 1
    for n in nums:
        total *= n
    return total


# B.4
def factorial(i):
    ''' Takes a non-negative integer and computes its factorial '''
    if i < 0:
        print "Please enter a nonnegative integer."
    else:
        fact = 1
        for n in range (1, i):
            fact *= n
        return fact
        

# B.5
def dice (m, n):
    ''' Given n dice with m amount of sides, this function outputs the sum of all the random dice values'''
    total = 0
    for n in range (n):
        total += random.choice(range(1, m+1))
    return total


# B.6
def remove_all(lst, i):
    ''' Given a list and a value, this function removes all elements of that value from the list'''
    x = lst.count(i)
    while x > 0:
        lst.remove(i)
        x -= 1

# B.7
def remove_all2(lst, i):
    ''' Given a list and a value, this function removes all elements of that value from the list'''
    x = lst.count(i)
    for j in range(1, x+1):
        lst.remove(i)

def remove_all3(lst, i):
    ''' Given a list and a value, this function removes all elements of that value from the list'''
    while i in lst:
        lst.remove(i)
        
# B.8
def any_in(lst1, lst2):
    ''' Given 2 lists, check if any elements are shared by both lists. Outputs True if elements are shared, and False if none are shared '''
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            if lst1[i-1] == lst2[j-1]:
                return True
    return False


# C.1.a
# a = 0 sets a to the value of 0.
# The intended use is to check if a is equal to 0.
# So, the code has to be changed to a == 0.
# == checks for equality, while = sets values

# C.1.b
# Arguments should not have quotes. 
# To fix the code, remove the quotations around the s in the function.

# C.1.c
# The function will always return 's-Caltech'
# Remove the quotes around the s in the return statement
# Then, it will add the string s and '-Caltech'
# instead of adding the literal string 's' and '-Caltech'

# C.1.d
# Can't add string 'bam' to list.
# Fix by appending the list with 'bam'
# lst.append('bam')

# C.1.e
# Attempting to return lst2.append(0) results in nothing
# Have to return lst by itself
# lst.reverse()
# lst.append(0)
# return lst

# C.1.f
# Appending letters to the list will only append the first entry of letters.
# To append all of letters to the list, we need to iterate through letters and individually append them to list.
# Add this code instead of list.append(letters)
# ALSO, shouldn't have builtin functions as variable names.
# list = []
# for x in letters:
#     list.append(x)
# return list

# C.2
# Code is read in order, so c is calculated with a = 10 and not a = 30
# c is calculated before the value of a is changed, so 10 + 20 = 30

# C.3
# add_and_double_2 only prints the result instead of returning it, so it returns no value
# On the other hand, add_and_double_1 returns the result so its result can be used elsewhere in the program
# Printing a result prints something in the output
# Returning a result from a function lets the program know what the result is

# C.4
# sum_of_squares_2 doesn't take any arguments, so trying to put arguments in the function won't work
# sum_of_squares_1 takes 2 args, and does stuff with them successfully
# Passing a value as an arg to a function lets the function take the arguments and use them
# Using raw_input to get user input requires the function to be run without any arguments, because the user will input the arguments

# C.5
# Can't change individual letters in a string

# C.6
# Doesn't put the new item back into the list
# Creates a duplicate of the item but doesn't reference it back into the original list