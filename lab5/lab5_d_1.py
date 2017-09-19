from Tkinter import *
import random

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

def draw_circle(upper_left, lower_right, color):
    ''' This function draws circles, given the upper left and lower right
    corners and color '''
    circle = canvas.create_oval(upper_left[0], upper_left[1], lower_right[0],\
                           lower_right[1], outline = color, fill = color, \
                           width = 1)
    return circle    

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
        for i in lst:
            lst.remove(i)
            
def button_handler(event):
    '''Handle left mouse button click events.'''
    coordinates = (event.x, event.y) 
    radius = random.randint(10, 50) / 2
    upper_left = (coordinates[0] - radius, coordinates[1] + radius)
    lower_right = (coordinates[0] + radius, coordinates[1] - radius)   
    circle = draw_circle(upper_left, lower_right, color)
    lst.append(circle)
    return circle

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width=800, height=800)
    canvas.pack()
    lst = []
    color = random_color()
    
    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    canvas.bind('<Button-1>', button_handler)

    # Start it up.
    root.mainloop()

