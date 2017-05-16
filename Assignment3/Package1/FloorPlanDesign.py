'''
Created on Nov 1, 2014

@author: pramesh
'''
import turtle
from MyTurtle import*
from FurnitureComponents import*
def main():
    # Room creation
    space = Room(-250,-150,500,300)
    room1  = Room(-250,-150,200,150,"Master Bedroom")
    room2  = Room(-250,0,150,50,"Attached Bathroom")
    room3  = Room(-250,50,150,100," Kids Room")
    room4  = Room(150,-150,100,100,"Guest Room")
    room5  = Room(150,-50,100,75,"Bathroom")
    room6  = Room(150,25,100,125,"Open Kitchen")
    
    # door creation
    room7  = Room(10,-150,80,20) # main door
    room8  = Room(-90,140,50,10) # back door
    room9  = Room(-205,-5,30,10)  # bathroom entrance for master bedroom
    room10  = Room(-205,45,30,10) # bathroom entrance for kids room
    room11  = Room(-55,-50,10,30)  # Master bedroom door
    room12  = Room(-105,80,10,30)   # Kids room door
    room13  = Room(145,-100,10,30)  #Guest room door
    room14  = Room(145,-25,10,30)   # Living room Bathroom door
    room15  = Room(10,125,25,25,"T.V") # T.v table
    
    #sofa creation
    sofa1 = Sofa(-10,-25,70,30,"brown")
    sofa2 = Sofa(-65,15,40,80,"brown")
    sofa3 = Sofa(75,15,40,80,"brown")
    
    #Table creation
    table1 = Table(10,40,25,"green",7)
    table2  = Table(170,100,20,"brown")
    
    turtle.showturtle()
    
    #Show Room
    space.showRoom()
    room1.showRoom()
    room2.showRoom()
    room3.showRoom()
    room4.showRoom()
    room5.showRoom()
    room6.showRoom()
    room7.showRoom()
    MyTurtle.writeText(25,-130,"Main Door","blue")
    room8.showRoom()
    MyTurtle.writeText(-87,150,"Back Door","blue")
    room9.showRoom()
    room10.showRoom()
    room11.showRoom()
    room12.showRoom()
    room13.showRoom()
    room14.showRoom()
    room15.showRoom()
    
    # show Sofa
    sofa1.showSofa()
    sofa2.showSofa()
    sofa3.showSofa()
    
    #show Table
    table1.showTable()
    table2.showTable()
    
    turtle.done()

main()

    
    