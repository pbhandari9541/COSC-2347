'''
Created on Nov 1, 2014

@author: pramesh
'''

import turtle
import random
class MyTurtle:
    
    def circle(radius,cx = None,cy = None,color = 'black',fill = False ):
        turtle.showturtle()
        turtle.penup()
        if cx is not None and cy is not None:
            turtle.goto(cx,cy)
        else:
            x1,y1 = turtle.pos()
            turtle.goto(x1,y1)
        turtle.pendown()
        if fill :
            rN= random.randint(0,2)
            if rN == 0:
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.fillcolor("red")
                turtle.end_fill()
            elif rN == 1:
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.fillcolor("green")
                turtle.end_fill()
            else:
                turtle.begin_fill()
                turtle.circle(radius)
                turtle.fillcolor("blue")
                turtle.end_fill()
        else:
            turtle.circle(radius)
    




    def rectangle(length,width,x =None ,y = None,color = 'black',fill = False ):  
        turtle.penup()
        if x is not None and y is not None:
            turtle.goto(x,y)
        else:
            x2,y2 = turtle.pos()
            turtle.goto(x2,y2)
        
        turtle.color(color)
        turtle.setheading(0)
        turtle.pendown()
        if fill :
                turtle.fillcolor(color)
                turtle.begin_fill()
                turtle.forward(length)
                turtle.left(90)
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(length)
                turtle.left(90)
                turtle.forward(width)
                turtle.end_fill()                
            
        else:
                turtle.forward(length)
                turtle.left(90)
                turtle.forward(width)
                turtle.left(90)
                turtle.forward(length)
                turtle.left(90)
                turtle.forward(width)
    
    
    


    def polygon(side,numberSides,angle = None,xstart = None,ystart = None,color = 'black',fill = False):
        insideAngle = (180 * (numberSides - 2))/numberSides
        turtle.penup()
        if angle is not None:
            turtle.setheading(0)
            turtle.left(angle)
        else:
            turtle.setheading(0)
        if xstart is not None and ystart is not None:
            turtle.goto(xstart,ystart)
            turtle.setheading(0)
        else:
            x3,y3 = turtle.pos()
            turtle.goto(x3,y3)
            turtle.setheading(0)
        turtle.pendown()
        if fill:
            rN= random.randint(0,2)
            if rN ==0:
                turtle.fillcolor('green')
                turtle.begin_fill()
                for i in range(1,numberSides+1):
                    turtle.forward(side)
                    turtle.left(180-insideAngle)
                turtle.end_fill()    
            elif rN ==1:
                turtle.fillcolor('blue')
                turtle.begin_fill()
                for i in range(1,numberSides+1):
                    turtle.forward(side)
                    turtle.left(180-insideAngle)
                turtle.end_fill()    
            else:
                turtle.fillcolor('purple')
                turtle.begin_fill()
                for i in range(1,numberSides+1):
                    turtle.forward(side)
                    turtle.left(180-insideAngle)
                turtle.end_fill()    
                
        else:
            for i in range(1,numberSides+1):
                turtle.forward(side)
                turtle.left(180-insideAngle)
    
    
    
    def chessboard(xstart,ystart,side,color = 'black',background = 'white'):
        turtle.penup()
        turtle.goto(xstart,ystart)
        turtle.setheading(0)
        boxSide = side/8
        turtle.pendown()
        for i in range(0,8):
            for j in range(0,8):
                if j % 2 ==0 :
                    if i % 2 ==0:
                        rectangle(boxSide,boxSide,xstart + i * boxSide,ystart + j * boxSide,color,True )
                    else:
                        rectangle(boxSide,boxSide,xstart + i * boxSide,ystart + j * boxSide,background,True )
                        
                else:
                    if i % 2 ==0:
                        rectangle(boxSide,boxSide,xstart + i * boxSide,ystart + j * boxSide,background,True )
                    else:
                        rectangle(boxSide,boxSide,xstart + i * boxSide,ystart + j * boxSide,color,True )
        
        rectangle(side,side,xstart,ystart,color,False)
    
    def writeText(x,y,text,color = 'black'):
        turtle.penup()
        turtle.goto(x,y)
        turtle.color(color)
        turtle.pendown()
        turtle.write(text)