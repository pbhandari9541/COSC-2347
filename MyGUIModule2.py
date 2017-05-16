from tkinter import*
class MyGUICallbackFunctions:
    def __init__(self):
        window1 = Tk()
        window1.title("Button event demo")
        label = Label(window1,text = "Welcome to GUI tkinter demo")
        btOk = Button(window1,text = "OK",bg = 'yellow',fg = 'red', command = self.processOK)
        btCancel = Button(window1,text = "Cancel",bg = 'yellow',fg = 'black',\
                            command = self.processCancel)
        button = Button(window1,text = "click me ")
        label.pack()
        btOk.pack(side = LEFT)
        btCancel.pack(side = RIGHT)
        window1.mainloop()
    def processOK(self):
        print("OK is processed")
    def processCancel(self):
        print("Cancel is pressed")
MyGUICallbackFunctions()
