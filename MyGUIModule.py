from tkinter import*
class MyGUI:
    def __init__(self):
        window1 = Tk()
        label = Label(window1,text = "Welcome to GUI tkinter demo")
        button = Button(window1,text = "click me ")
        label.pack()
        button.pack()
        window1.mainloop()
MyGUI()
