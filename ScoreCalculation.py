from tkinter import*
class ScoreCalculation:
    def __init__(self):
        window1 = Tk()
        label1 = Label(window1,text = "Score Calculation", justify = LEFT).grid(row = 1, column = 1)
        label2 = Label(window1,text = "Assignments").grid(row = 2, column = 1)
        label3 = Label(window1,text = "First exam").grid(row = 3, column = 1)
        label4 = Label(window1,text = "Second exam").grid(row = 4, column = 1)
        label5 = Label(window1,text = "Class participation").grid(row = 5, column = 1)
        label6 = Label(window1,text = "Labs & Quizzes").grid(row = 6, column = 1)
        label7 = Label(window1,text = "Final exam").grid(row = 7, column = 1)

        self.v1 = StringVar()
        entry1 = Entry(window1,textvariable = self.v1).grid(row = 2, column = 2)
        self.v2 = StringVar()
        entry2 = Entry(window1,textvariable = self.v2).grid(row = 3,column = 2)
        self.v3 = StringVar()
        entry3 = Entry(window1,textvariable = self.v3).grid(row = 4,column = 2)
        self.v4 = StringVar()
        entry4 = Entry(window1,textvariable = self.v4).grid(row = 5,column = 2)
        self.v5 = StringVar()
        entry5 = Entry(window1,textvariable = self.v5).grid(row = 6,column = 2)
        self.v6 = StringVar()
        entry6 = Entry(window1,textvariable = self.v6).grid(row = 7,column = 2)

        self.v7 = StringVar()
        entry7 = Entry(window1,textvariable = self.v7).grid(row = 2,column = 5, padx = 30)

        self.v8 = IntVar()
        rbShowScore1 = Radiobutton(window1,text = "Show score 1", variable = self.v8,\
                                   value = 1, fg = "red", command = self.showScore1).grid(row = 4,column = 5)
        rbShowScore1 = Radiobutton(window1,text = "Show score 1", variable = self.v8,\
                                   value = 2, fg = "red", command = self.showScore2).grid(row = 5,column = 5)


        window1.mainloop()
        
    def showScore1(self):
        result1 = 0.20 * eval(self.v1.get()) + 0.15 * eval(self.v2.get()) + 0.15 * eval(self.v3.get())\
                  + 0.10 * eval(self.v4.get()) + 0.20 * eval(self.v5.get()) + 0.20 * eval(self.v6.get())
        self.v7.set(result1)
    def showScore2(self):
        result2 = 0.20 * eval(self.v1.get()) + 0.10 * eval(self.v2.get()) + 0.15 * eval(self.v3.get()) \
                  + 0.10 * eval(self.v4.get()) + 0.20 * eval(self.v5.get()) + 0.25 * eval(self.v6.get())
        self.v7.set(result2)
        
ScoreCalculation()
