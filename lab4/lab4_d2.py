# Jessica Choi
from Tkinter import *

def draw_square(canvas, color, width, position):
    ''' Given the canvas (tuple), color (string), width (int), and position (tuple) of a square, this function draws the square on the canvas '''   
    left_upper_corner = (position[0] - width/2, position[1] - width/2)
    right_lower_corner = (position[0] + width/2, position[1] + width/2)
    square = canvas.create_rectangle(left_upper_corner, right_lower_corner, \
                                fill = color, outline = color)




if __name__ == '__main__':
    root = Tk()    
    root.geometry('800x800')         
    canvas = Canvas(root, width = 800, height = 800)  
    canvas.pack()        
    draw_square(canvas, 'red', 100, (50,50))
    draw_square(canvas, 'blue', 100, (50,750))
    draw_square(canvas, 'green', 100, (750,50))
    draw_square(canvas, 'yellow', 100, (750,750))
    root.mainloop()
