# File: triangle.py
# draws a Sierpinski triangle using the chaos algorithm
# utilizes the tkinter graphical package

import tkinter as tk
from random import randint
from math import *

def main(n):
    win = tk.Tk()
    canvas = tk.Canvas(win, width=1000, height=1000)
    canvas.pack()
    verts = [(50,700), (900,700), (500,10)]
    canvas.create_polygon([verts[0][0],verts[0][1], verts[1][0],verts[1][1], verts[2][0],verts[2][1]], fill = "white", outline = "black")
    win.update()
    gp = False
    while not gp:
        p = (randint(verts[0][0],verts[1][0]),randint(verts[2][1],verts[1][1]))
        if p[1] - verts[0][1] > ((verts[0][1]-verts[2][1])/(verts[0][0]-verts[2][0]))*(p[0]-verts[0][0]) and p[1] - verts[1][1] > ((verts[1][1]-verts[2][1])/(verts[1][0]-verts[2][0]))*(p[0]-verts[1][0]):
            gp = True
    for i in range(n):
        canvas.create_oval(p[0],p[1],p[0],p[1])
        win.update()
        v = verts[randint(0,2)]
        p = ((p[0]+v[0])/2,(p[1]+v[1])/2)
    win.mainloop()
    
    

main(100000)
    
    
