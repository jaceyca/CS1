# Jeongyoon "Jessica" Choi PS 1

# C.1.1: 9 - 3 -> 6
# C.1.2: 8 * 2.5 -> 20.0
# C.1.3: 9 / 2 -> 4
# C.1.4: 9 / -2 -> -5
# C.1.5: 9 % 2 -> 1
# C.1.6: 9 % -2 -> -1
# C.1.7: -9 % 2 -> 1
# C.1.8: 9 / -2.0 -> -4.5
# C.1.9: 4 + 3 * 5 -> 19
# C.1.10: (4 + 3) * 5 -> 35
# C.2.1: x = 100 -> x = 100
# C.2.2: x = x + 10 -> x = 110
# C.2.3: x += 20 -> x = 130
# C.2.4: x = x - 40 -> x = 90
# C.2.5: x -= 50 -> x = 40
# C.2.6: x *= 3 -> x = 120
# C.2.7: x /= 5 -> x = 24
# C.2.8: x %= 3 -> x = 0

'''
C.3
Python evaluates x - x to be 0 first, and then adds that to x and
sets x to the new value of x. x is still 3 after evaluation of the statement.
'''

#C.4.1: 1j + 2.4j -> 3.4j
#C.4.2: 4j * 4j -> -16
#C.4.3: (1 + 2j) / (3 + 4j) -> .44 + .08j
#C.4.4: (1 + 2j) * (1 + 2j) -> -3 + 4j
#C.4.5: 1 + 2j * 1 + 2j -> 1 + 4j

'''
They're different because Python evaluated the parentheses (addition) and then multiplication for C.4.4,
but evaluated multiplication and then addition for line C.4.5.
Python seems to treat complex numbers as regular integers.
'''

# C.5.1: cmath.sin(-1.0 + 2.0j) -> (-3.165778513216168+1.959601041421606j)
# C.5.2: cmath.log(-1.0 + 3.4j) -> (1.2652585805200263+1.856847768512215j)
# C.5.3: cmath.exp(-cmath.pi * 1.0j) -> (-1-1.2246467991473532e-16j)
# It can cause name clashes if you import using *

# C.6.1: "foo" + 'bar' -> foobar
# C.6.2: "foo" 'bar' -> foobar


'''
C.6.3:
a = 'foo'
b = "bar"
a + b -> foobar       '''

'''
C.6.4:
a = 'foo'
b = "bar"
a b  ->  error, invalid syntax'''

'''
C.7:
print '\'A \nB \nC\''
'''

# C.8: 80 * ' - '

# C.9: print "first line \nsecond line \nthird line"

'''
x = 3
y = 12.5
C.10.1: print "The rabbit is %d" % x
C.10.2: print "The rabbit is %d years old" % x
C.10.3: print "%g is average." % y
C.10.4: print "%g * %d " % (y, x)
C.10.5: print " %g * %d is %g" % (y, x, x * y)
'''

# C.11:
num = float(raw_input("Enter a number: "))
print num

# C.12:
def quadratic(a, b, c, x):
    quadratic = a * x**2 + b * x + c
    print quadratic
    
# Could use x * x for x^2


def GC_content(DNA):
    ''' GC_content calculates which proportion of bases in a string
    representing a DNA sequence are either G or C.
    The input argument should be a DNA sequence made of only A, C, G, or T bases.'''
    A_content = float (DNA.count('A'))    
    C_content = float (DNA.count('C'))    
    G_content = float (DNA.count('G'))
    T_content = float (DNA.count('T'))    
    fraction = (G_content + C_content)/(A_content + C_content + G_content + T_content)
    return fraction


