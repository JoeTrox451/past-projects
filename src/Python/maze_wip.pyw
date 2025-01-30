# File: maze.pyw
# Simulates a similar display to a TI-99
# Randomly generates a maze using the '#' symbol as the default wall
# 2025 note: uses an algorithm found in the book __
# work in progress

import tkinter as tk
from random import randrange

class maze:
    def __init__(self, wall="#", path=" "):
        root = tk.Tk()
        TI = tk.Canvas(root, width=540, height=540)
        TI.pack()
        direc = 0
        for y in range(0, 540, 20):
            for x in range(0, 540, 20):
                coordsTag = str(x) + "," + str(y)
                if (y < 60 or y >= 480) or (x < 48 or x >= 480):
                    TI.create_text(x, y, text=path, tag=(coordsTag,path), anchor="nw", font=("Courier New","16"))
                else:
                    TI.create_text(x, y, text=wall, tag=(coordsTag,wall,direc), anchor="nw", font=("Courier New","16"))
        self.TI=TI
        for i in range(3):
            a = randrange(80,480,20)
            b = randrange(80,480,20)
            loc = str(a) + "," + str(b)
            self.TI.itemconfigure(loc, text=" ")
            

        

##    def generate(self, start=None):
##        if not start:
##            self.x = randrange(80,480,40)
##            self.y = randrange(80,480,40)
##            start = str(self.x) + "," + str(self.y)
##        ax = self.x
##        ay = self.y
##        while:
##            d = randrange(0,3)
##            dd = d
##            # 0 is right, 1 is up, 2 is left, 3 is down
##            if d == 0:
##                dx = 40
##                dy = 0
##            elif d == 1:
##                dx = 0
##                dy = 40
##            elif d == 2:
##                dx = -40
##                dy = 0
##            elif d == 3:
##                dx = 0
##                dy = -40
##            bx = ax + dx
##            by = ay + dy
##            loc = str(bx) + "," + str(by)
##            char = self.TI.itemcget(loc, text)
##            if char == " ":
##                
##            if char == "#":
##                self.TI.itemconfigure(loc, text=" ")
##
##                
##
##    def 


            
        
            



if __name__ == "__main__":
    Maze = maze()
#    Maze.generate()
    
