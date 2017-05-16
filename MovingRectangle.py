from tkinter import *

class MovingRectangle:
    def __init__(self):
        self.canvasSize = 200
        self.squareSize = 10
        self.moveIncrement = 5
        self.bgColor = 'black'
        self.shapeColor = 'red'
        self.x = self.canvasSize/2 - self.squareSize/2
        self.y = self.x
        
        self.window = Tk()
        self.window.title('Moving Rectangle')
        self.canvas = Canvas(self.window, bg = self.bgColor, width = self.canvasSize, height = self.canvasSize)
        self.canvas.create_rectangle(self.x, self.y,self.x+self.squareSize, self.y+self.squareSize, fill=self.shapeColor, outline=self.shapeColor, tags='rect')
        self.canvas.bind("<Key-l>", self.MoveLeft)
        self.canvas.bind("<Key-r>", self.MoveRight)
        self.canvas.bind("<Key-u>", self.MoveUp)
        self.canvas.bind("<Key-d>", self.MoveDown)
        self.canvas.pack()
        self.canvas.focus_set()
        self.window.mainloop()
    
    def MoveLeft(self, event):
        if self.x > 0:
            self.x -= 5
        self.canvas.delete("rect")
        self.canvas.create_rectangle(self.x, self.y, self.x+self.squareSize, self.y+self.squareSize, fill=self.shapeColor, outline=self.shapeColor, tags='rect')
    
    def MoveRight(self, event):
        if self.x < (self.canvasSize - self.squareSize):
            self.x += 5
        self.canvas.delete("rect")
        self.canvas.create_rectangle(self.x, self.y, self.x+self.squareSize, self.y+self.squareSize, fill=self.shapeColor, outline=self.shapeColor, tags='rect')
    
    def MoveUp(self, event):
        if self.y > 0:
            self.y -= 5
        self.canvas.delete("rect")
        self.canvas.create_rectangle(self.x, self.y, self.x+self.squareSize, self.y+self.squareSize, fill=self.shapeColor, outline=self.shapeColor, tags='rect')
        
    def MoveDown(self, event):
        if self.y < (self.canvasSize-self.squareSize):
            self.y += 5
        self.canvas.delete("rect")
        self.canvas.create_rectangle(self.x, self.y, self.x+self.squareSize, self.y+self.squareSize, fill=self.shapeColor, outline=self.shapeColor, tags='rect')

MovingRectangle()
        
