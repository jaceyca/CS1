'''
lab3d.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 

def update(lsys, s):
    ''' Takes a dictionary and a string, and generates the next version of the
    string by applying the rules to each character in the string'''
    string = ''
    for char in string:
        if char in lsys:
            string += lsys[char] 
        else:
            string += char
    return string
    
    
def iterate(lsys, n):
    ''' Takes a dictionary and an integer, and returns the string that results
    from being updated n times'''
    start = lsys['start']
    for i in range(n):
        s = update(lsys, start)
        i += 1
    return s


def lsystemToDrawingCommands(draw, string):
    ''' Given a dictionary and string, this function returns the list of 
    drawing commands required to draw the figure corresponding to the string'''
    lst = []
    for char in string:
        if char in draw:
            lst.append(draw[char])
    return lst

def bounds(cmds):
    ''' Takes a list of commands and computes the bounding coordinates of the 
    resulting drawing, returning a tuple of (xmin, xmax, ymin, ymax), where 
    each coordinate is a float '''
    x = 0
    y = 0
    xmax = 0
    ymax = 0
    xmin = 0
    ymin = 0
    angle = 0
    new_tup = (xmin, xmax, ymin, ymax)    
    for i in range(len(cmds)):
        tup = nextLocation(x, y, angle, cmds)
        if x > xmax:
            xmax = tup[1]
        if x < xmin:
            xmin = tup[1]
        if y > ymax:
            ymax = tup[2]
        if y < ymin:
            ymin = tup[2]
        i += 1
    return new_tup

def nextLocation(x, y, angle, cmds):
    ''' Generates the next location and direction of the turtle after the 
    drawing command has been executed, returning a tuple (x coordinate, 
    y coordinate, angle) '''
    lst = cmds.split( )
    angle_in_radians = angle * math.pi/180
    if lst[0] == 'L':
        new_x = x
        new_y = y
        new_angle = angle_in_radians % 360 + 90
    elif lst[0] == 'R':
        new_x = x
        new_y = y
        new_angle = angle_in_radians % 360 - 90        
    elif lst[0] == 'F':
        if angle == 0:
            x += lst
        elif angle == 180:
            x -= lst
    else:
        new_x = x + lst[1] * float(cos(angle_in_radians))
        new_y = y + lst[1] * float(sin(angle_in_radians))
    tup = (new_x, new_y, new_angle)
    return tup

def saveDrawing(filename, bounds, cmds):
    '''Given a filename to write to, the bounds of the resulting drawing as a 
    tuple, and a list of drawing commands, this function will save the drawing'''
    f = open(filename, 'w')
    f.write(str(bounds))
    for line in cmds:
        f.write(line + '\n')
    f.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

