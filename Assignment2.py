import turtle
import random
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



circle(45,5,7,fill = True)

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


rectangle(100,50,20,20)


def polygon(side,numberSides,angle = None,xstart = None,ystart = None,color = 'black',fill = False):
    insideAngle = (180 * (numberSides - 2))/numberSides
    turtle.penup()
    x3,y3 = turtle.pos()
    turtle.setheading(0)
    if angle is not None:
        turtle.left(angle)
    else:
        turtle.setheading(0)
    if xstart is not None and ystart is not None:
        turtle.goto(xstart,ystart)
    else:
        turtle.goto(x3,y3)
    turtle.pendown()
    if fill:
        rN= random.randint(0,2)
        if rN ==0:
            turtle.fillcolor('green')
            turtle.begin_fill()
            for i in range(1,numberSides+1):
                turtle.forward(side)
                turtle.right(180-insideAngle)
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


polygon(100,5,45,xstart=-50,ystart=50)

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
                

chessboard(-100,-100,200)



def main():
 n = eval(input("How many sides do you want on your spiral square?\n"))
 side = 10
 turtle.pendown()
 for i in range(n):
     turtle.forward(side)
     turtle.right(90)
     side = side + 10
main()



