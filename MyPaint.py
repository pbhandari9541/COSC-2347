from tkinter import*

class MyPaint:
    def __init__(self):
        window = Tk()
        window.title("MyPaint")
        menubar = Menu(window)
        window.config(menu = menubar)
        
        #add menu item to Draw menu
        drawMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Draw",menu = drawMenu)
        
        drawMenu.add_command(label = "Oval", command = self.processOval)
        drawMenu.add_command(label = "Arc", command = self.processArc)
        drawMenu.add_command(label = "Rectangle",command = self.processRectangle)
        drawMenu.add_command(label = "Line", command = self.processLine)
        drawMenu.add_separator()
        drawMenu.add_command(label = "Free Draw",command = self.processFreeDraw)
        subMenubar = Menu(drawMenu, tearoff = 0)
        drawMenu.add_cascade(label = "Color",menu = subMenubar)
        subMenubar.add_command(label = "Red", command = self.setColorRed)
        subMenubar.add_command(label = "Orange", command = self.setColorOrange)
        subMenubar.add_command(label = "Blue", command = self.setColorBlue)
        subMenubar.add_command(label = "Yellow", command = self.setColorYellow)

        # add menu to edit menu
        editMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "Edit", menu = editMenu)
        editMenu.add_command(label = "Undo", command = self.undo)
        editMenu.add_command(label = "Clear All", command = self.clearAll)
        # add Help menu
        menubar.add_command(label = "Help", command = self.help)

        # add Buttons for the shape
        frame1 = Frame(window)
        frame1.grid(row = 1,column = 1, sticky = W)
        frame2 = Frame(window)
        frame2.grid(row = 2, column = 1, sticky = W)
        frame3 = Frame(window)
        frame3.grid(row = 3, column = 1)
        '''
        imageOval = PhotoImage(file = "C:\COSC2347\Python34\oval4.gif")
        imageLine = PhotoImage(file = "C:\COSC2347\Python34\diagonal2.gif")
        imageRectangle = PhotoImage(file = "C:\COSC2347\Python34\round-image1.gif")
        '''
        
        btnRectangle =  Button(frame1, text = 'Rectangle', command = self.processRectangle).grid(row = 1, column = 1)
        btnOval = Button(frame1, text = 'Oval', command = self.processOval).grid(row = 1, column = 2)
        btnArc = Button(frame1, text = 'Arc', command = self.processArc).grid(row = 1, column = 3)
        btnLine = Button(frame1, text = 'Line',command = self.processLine).grid(row = 1, column = 4)
        btnFreeDraw = Button(frame1, text = "Free Draw", command = self.processFreeDraw).grid(row = 1, column = 5)
        #btnWriteText = Button(frame1, text = "Write Text", command = self.processWriteText).grid(row = 1, column = 6)
        btnUndo = Button(frame1,text = "Undo", command = self.undo).grid(row = 1, column = 7)
        btnClearAll = Button(frame1,text = "Clear", command = self.clearAll).grid(row = 1, column = 8)

        self.currentColor = "black"
        
        btnOrange = Button(frame2, text = 'Orange', command = self.setColorOrange).grid(row = 1, column = 1)
        btnRed = Button(frame2, text = 'Red', command = self.setColorRed).grid(row = 1, column = 2)
        btnBlue = Button(frame2, text = 'Blue',command = self.setColorBlue).grid(row = 1, column = 3)
        btnYellow = Button(frame2, text = 'Yellow',command = self.setColorYellow).grid(row = 1, column = 4)
        self.v0 = StringVar()
        label = Label(frame2, textvariable = self.v0, fg = "red").grid(row = 1,column = 5,padx = 20)
        
        self.v1 =IntVar()
        rdFill = Radiobutton(frame1,text ="Fill",variable = self.v1,value  = 1, command = self.fill).grid(row =1, column = 9, padx = 20)
        rdFill = Radiobutton(frame1,text ="Unfill",variable = self.v1,value = 2, command =  self.fill).grid(row = 1,column = 10)
        
        self.canvas = Canvas(frame3, height =600, width = 1000, bg = "white")
        self.canvas.grid(row = 2, column = 1)
        # bind canvas with mouse event
        self.canvas.bind("<Button-1>",self.startShape)
        self.canvas.bind("<B1-Motion>",self.drawShape)
        self.canvas.bind("<ButtonRelease-1>",self.drawShape)
        

        self.xStart = 0
        self.yStart = 0
        self.xEnd = 0
        self.yEnd = 0
        window.mainloop()
       
    def fill(self):
        if self.v1.get() == 1:
            return True

        elif self.v1.get() ==2:
            return False

    

    def processRectangle(self):
        self.currentShape = 'Rectangle'

    def processOval(self):
        self.currentShape = 'Oval'
    def processArc(self):
        self.currentShape = 'Arc'

    def processLine(self):
        self.currentShape = 'Line'

    def processFreeDraw(self):
        self.currentShape = 'Draw'

    def processWriteText(self):
        self.currentShape = "Text"


    def setColorOrange(self):
        self.currentColor = "orange"
             
    def setColorRed(self):
        self.currentColor = "red"
            
    def setColorBlue(self):
        self.currentColor = "blue"
            
    def setColorYellow(self):
        self.currentColor = "yellow"


    def getColor(self):
         return self.currentColor


    def paint(self,event):
        self.canvas.create_oval(event.x-1,event.y-1,event.x+1,event.y+1, fill = self.getColor(), tag = 'Draw')
       

    #def writeText(self):
        

    def startShape(self,event):
        self.xStart = event.x
        self.yStart = event.y

    def drawShape(self,event):
        self.xEnd = event.x
        self.yEnd = event.y
        
        if self.currentShape == 'Oval':
            self.canvas.delete('Oval')
            
            if self.fill():
                
                self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Oval', fill = self.getColor(), outline = self.getColor())
            else:
                self.canvas.create_oval(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Oval', outline = self.getColor())

        elif self.currentShape == 'Rectangle':
            self.canvas.delete('Rectangle')
            
            if self.fill():
                self.canvas.create_rectangle(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Rectangle', fill = self.getColor(), outline= self.getColor())
            else:
                
                self.canvas.create_rectangle(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Rectangle', outline= self.getColor())

        elif self.currentShape == 'Line':
            
            self.canvas.delete('Line')
            
            if self.fill():
                self.canvas.create_line(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Line', fill = self.getColor())
            else:
                self.canvas.create_line(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Line', fill = 'black')
        if self.currentShape == 'Arc':
            self.canvas.delete('Arc')
            
            if self.fill():
                self.canvas.create_arc(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Arc', fill = self.getColor(), outline = self.getColor())
            else:
                self.canvas.create_arc(self.xStart,self.yStart,self.xEnd,self.yEnd,tags = 'Arc', outline = self.getColor())

        elif self.currentShape == 'Draw':
            self.v0.set(" Click Right button and Drag the mouse to draw")
            self.canvas.bind( "<B3-Motion>", self.paint)
            

        #elif self.currentShape == "Text":
            #self.canvas.delete('Text')
            #self.v0.set("Click on desired place for the text on Canvas  and Go to the python console for the text to be shown")
            #self.canvas_id = self.canvas.create_text(self.xStart, self.xStart, anchor="nw")
            #self.canvas.itemconfig(self.canvas_id, text="")
            #self.canvas.insert(self.canvas_id, self.xStart,self.userInput())  
        else:
            self.v0.set("please choose valid shape")
        
    def userInput(self):
        input1 =input("type smthng")
        self.canvas.bind("<Enter>", self.processWriteText)
    
        return input1

        
    def extractColor(self, statement):
     validColor = ['red', 'orange', 'black', 'yellow','blue']  
     for i in range(len(validColor)):     
        if validColor[i] in statement:   
            return validColor[i]
     return None    
  
    def undo(self):

        if self.currentShape == 'Oval':

            self.canvas.delete('Oval')

        elif self.currentShape == 'Rectangle':
            self.canvas.delete('Rectangle')

        elif self.currentShape == 'Line':
            self.canvas.delete('Line')
            
        elif self.currentShape == 'Draw':
            self.canvas.delete('Draw')
            
        elif self.currentShape == 'Arc':
            self.canvas.delete("Arc")
        elif self.currentShape == 'Text':
            self.canvas.delete('Text')
        
        
  
            
        
    def clearAll(self):
        self.canvas.delete('all')

    def help(self):
        self.v0.set("please click the right shape and color to draw")
        
                   
        
MyPaint()
                       
        
        
        
