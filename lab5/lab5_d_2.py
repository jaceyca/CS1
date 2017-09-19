from Tkinter import *
import random
from math import *

# Graphics commands.

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
  
def draw_line(point1, point2, color):
    ''' This function draws a colored line from point1 to point2 '''
    line = canvas.create_line(point1[0], point1[1], point2[0], \
                              point2[1], fill = color)
    
def draw_star(N, radius, center):
    ''' This function draws an N-pointed star centered at a particular
    location '''
    global star
    points = []
    theta = 2 * pi / N
    for i in range(N):
        angle = i * theta + pi / 2
        x = center[0] + radius * cos(angle)
        y = center[1] - radius * sin(angle)
        points.append((x, y))
    for i, point in enumerate(points):
        point2 = points[(i + (N - 1) / 2) % N]
        line = draw_line(points[i], point2, color)
        star.append(line)
    return star
        
    
# Event handlers.

def key_handler(event):
    '''Handle key presses.'''
    key = event.keysym
    if key == 'q':
        quit()
    elif key == 'c':
        global color
        color = random_color()
    elif key == 'x':
        canvas.delete('all')
        global lst
        for i in lst:
            lst.remove(i)
    elif key == 'plus':
        global N
        N += 2
    elif key == 'minus':
        global N
        assert N >= 7        
        N -= 2
        # when N = 3, triangle appears
        # when N < 3, nothing appears
        # assertion statement prevents non-stars from being drawn
            
def button_handler(event):
    '''Handle left mouse button click events.'''
    coordinates = (event.x, event.y) 
    radius = random.randint(50, 100) / 2
    upper_left = (coordinates[0] - radius, coordinates[1] - radius)
    lower_right = (coordinates[0] + radius, coordinates[1] + radius)   
    star = draw_star(N, radius, coordinates)
    lst.append(star)
    
if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    lst = []
    star = []
    color = random_color()
    N = 5
    assert N % 2 == 1     
    
    # Bind events to handlers.
    root.bind('<q>', key_handler)
    root.bind('<c>', key_handler)
    root.bind('<x>', key_handler)
    root.bind('<plus>', key_handler)
    root.bind('<minus>', key_handler)    
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()
