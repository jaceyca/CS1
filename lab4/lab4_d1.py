# Jessica Choi
from Tkinter import *
''' Draws 4 differently colored squares of size 100x100 on a 800x800 canvas '''
root = Tk()
root.geometry('800x800')
c = Canvas(root, width = 800, height = 800)
c.pack()
r = c.create_rectangle(0, 0, 100, 100, \
 fill = 'red', outline = 'red') 
g = c.create_rectangle(700, 0, 800, 100, \
    fill = 'green', outline = 'green')
b = c.create_rectangle(0, 700, 100, 800, \
    fill = 'blue', outline = 'blue')
y = c.create_rectangle(700, 700, 800, 800, \
    fill = 'yellow', outline = 'yellow')

root.mainloop()