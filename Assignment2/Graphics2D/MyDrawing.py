'''
filename: MyDrawing.py
Created on Oct 15, 2014

@author: pramesh bhandari
description: this programs tests the functions defined in the module GraphicsAndPatternLibrary
'''            

import turtle
from GraphicsAndPatternLibrary import*
def main():
    circle(100,0,0)
    for i in range (30,0,-10):
        circle(i,-50,100,fill = True)
    for i in range (30,0,-10):
        circle(i,50,100,fill = True)
    polygon(100,3,xstart = -50,ystart = 200,fill = True)
    polygon(20,10,xstart = -10,ystart = 30,fill = True)
    rectangle(100,10,-200,-105, fill = False)
    rectangle(100,10,100,-105, fill = False)
    polygon(10,8,xstart = -200,ystart = -110,fill = True)
    polygon(10,8,xstart = 200,ystart = -110,fill = True)
    chessboard(-100,-200,200) 
    spiral(20,-200,100)
    turtle.done()
main()   
 