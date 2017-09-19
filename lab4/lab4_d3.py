# Jessica Choi
from Tkinter import *
from lab4_b import *
from lab4_d2 import *
import random

                
def quit_program(a):
    ''' Quits the program if "q" key is pressed.'''
    key = a.keysym
    if key == 'q':
        quit()
        
if __name__ == '__main__':
    root = Tk()
    root.geometry('800x800')
    canvas = Canvas(root, width = 800, height = 800)
    canvas.pack()    
    for x in range(50):
        y = random_size(20, 150)
        (max_x, max_y) = random_position(750, 750)
        color = random_color()
        draw_square(canvas, color, y, (max_x, max_y)) 
    root.bind('q', quit_program)    
    root.mainloop()