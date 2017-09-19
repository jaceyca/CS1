# Jessica Choi, CS 1
from math import *

class Point:
    ''' This class will represent a point in 3D space, and will contain a method
    to calculate distances between points'''
    def __init__(self, x, y, z):
        ''' This constructor takes the x, y, z coordinates and stores them in
        the object '''
        self.x = x
        self.y = y
        self.z = z
    
    def distanceTo(self, p2):
        ''' Calculates the distance between p2 and point being acted on (p1),
        using the distance formula '''
        distance = sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2 + \
                        (p2.z - self.z) ** 2)
        return distance
    
class Triangle:
    ''' This class will take three Points and compute the area '''
    def __init__(self, p1, p2, p3):
        ''' This constructor method will take three points and store them '''
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def area(self):
        ''' This method will compute the area of the triangle using Heron's
        formula '''
        a = Point.distanceTo(self.p1, self.p2)
        b = Point.distanceTo(self.p1, self.p3)
        c = Point.distanceTo(self.p2, self.p3)
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
class Averager:
    ''' This class stores a list of numbers and performs various operations '''
    def __init__(self):
        ''' This constructor stores the list of numbers (nums), sum of all the
        numbers (total), and length of nums (n) '''
        self.nums = []
        self.total = 0.0
        self.n = 0
        
    def getNums(self):
        ''' Returns the list of numbers stored so far in list nums '''
        num2 = self.nums[:]
        return num2
    
    def append(self, new):
        ''' Appends a new number to nums '''
        self.nums.append(new)
        self.total += new
        self.n += 1
        
    def extend(self, lst):
        ''' Appends a list of numbers to the existing nums '''
        self.nums.extend(lst)
        for i in lst:
            self.total += i
            self.n += 1
        
    def average(self):
        ''' Computes average of nums '''
        average = 0.0
        if self.n > 0:
            average = self.total / self.n
        return average
    
    def limits(self):
        ''' Computes minimum and maximum of nums '''
        minimum = 0
        maxiumum = 0
        if len(self.nums) != 0:        
            minimum = min(self.nums)
            maxiumum = max(self.nums)
            extremes = (minimum, maximum)
        return extremes
    
    
# C.1
# It would be much easier to just use assertion than an if statement.
def is_positive(x):
    ''' Test if x is positive. '''
    assert x > 0

# C.2
# The found is unnecessary and overcomplicates the function and can be removed.
# The function can be simplified by removing the else statement since location
# is set to -1 at the beginning anyways.
def find(x, lst):
    '''Returns the index into a list where x is found, or -1 otherwise.
    Assume that x is found at most once in the list.'''
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# C.3
# It is unnecessary to check all the conditions if one is fulfilled.
# So, it is more efficient for the function to return a string once x is
# categorized in any of the if statements.
def categorize(x):
    '''Return a string categorizing the number 'x', which should be
    an integer.'''
    if x < 0:
        return 'negative'
    if x == 0:
        return 'zero'
    if x > 0 and x < 10:
        return 'small'
    if x >= 10:
        return 'large'

# C.4
# It is much easier to use a for loop than summing a bunch of different cases.
def sum_list(lst):
    '''Returns the sum of the elements of a list of numbers.'''
    answer = 0
    for item in lst:
        answer += item
    return answer