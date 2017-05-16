'''
Created on Nov 1, 2014

@author: pramesh
'''
import turtle
from MyTurtle import*
class Room:
    def __init__(self,x,y,l,w,n = None):
        self.__x = x
        self.__y = y
        self.__length = l 
        self.__width = w
        if n is not None:
            self.__name = n  
        else:
            self.__name = " "
            
    def setX(self,x):
        self.__x = x
        
    def setY(self,y):
        self.__y = y
        
    def setLength(self,l):
        self.__length = l 
        
    def setWidth(self,w):
        self.__width = w
        
    def setName(self,n):
        self.__name = n 
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def getName(self):
        return self.__name 
    
    def showRoom(self):
        MyTurtle.rectangle(self.__length,self.__width,self.__x,self.__y)
        MyTurtle.writeText(self.__x + (self.__length / 5 ),self.__y + (self.__width / 2), self.__name,"red")
        if(self.__width >= 50 and self.__width <= 150):  
            MyTurtle.writeText(self.__x +(self.__length / 4), self.__y + (self.__width / 4),str(self.__length) + "*" + str(self.__width),"brown")
            
        
class Table:
    def __init__(self,x,y,l,c,s = 0,w = None):
        self.__x = x
        self.__y = y
        self.__side1 = l
        self.__color = c 
        self.__shape = s
        self.__side2 = w 
    
    def setX(self,x):
        self.__x = x
        
    def setY(self,y):
        self.__y = y
        
    def setShape(self,s):
        self.__shape = s 
        
    def setSide1(self,l):
        self.__side1 = l 
        
    def setSide2(self,w):
        self.__side2 = w
        
    def setColor(self,c):
        self.__color = c 
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def getShape(self):
        return self.__shape
    
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getColor(self):
        return self.__color
    
    def showTable(self):
        if (self.__shape == 0):
            MyTurtle.circle(self.__side1, self.__x,self.__y,self.__color,True)
            MyTurtle.writeText(self.__x, self.__y,"Table")
            
        elif(self.__shape == 4):
            MyTurtle.rectangle(self.__side1,self.__side2,self.__x,self.__y,self.__color,False)
            MyTurtle.writeText(self.__x + (self.__side1 / 3 ),self.__y + (self.__side2 / 2),"Table")
            
        else:
            MyTurtle.polygon(self.__side1,self.__shape,xstart = self.__x, ystart = self.__y,color = self.__color, fill = True)
            MyTurtle.writeText(self.__x,self.__y + self.__side1,"Table")
            
class Sofa:
    def __init__(self,x,y,l,w,c):
        self.__x = x
        self.__y = y
        self.__length = l
        self.__width = w
        self.__color = c  
        
    def setX(self,x):
        self.__x = x
        
    def setY(self,y):
        self.__y = y
        
    def setLength(self,l):
        self.__length = l
         
    def setWidth(self,w):
        self.__width = w
        
    def setColor(self,c):
        self.__name = c 
        
    def getX(self):
        return self.__x
        
    def getY(self):
        return self.__y
    
    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def getColor(self):
        return self.__color  
    
    def showSofa(self):
        MyTurtle.rectangle(self.__length,self.__width,self.__x,self.__y,self.__color,False)
        MyTurtle.writeText(self.__x + (self.__length / 3 ),self.__y + (self.__width / 2),"Sofa")