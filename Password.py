from tkinter import*
class password:
    def __init__(self):
        window = Tk()
        window.title("password configuration")
        frame1 = Frame(window)
        frame2 = Frame(window)
        frame3 = Frame(window)
        frame4 = Frame(window)
        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        label1 = Label(frame1, text = "Enter Passoword")
        label1.grid(row = 1, column = 1)
        self.password1 = StringVar()
        entry1 = Entry(frame1,textvariable = self.password1, show = '*')
        entry1.grid(row = 1, column = 2)
        labe2 = Label(frame2, text = "Enter Passoword")
        labe2.grid(row = 1, column = 1)
        self.password2 = StringVar()
        entry2 = Entry(frame2,textvariable = self.password2, show = '*')
        entry2.grid(row = 1, column = 2)

        button1 = Button(frame3, text = "Save", command = self.processButton)
        button1.grid(row = 1,column = 2)
        self.v = StringVar()
        label3= Label(frame4, textvariable = self.v)
        label3.pack()
        

        window.mainloop()

    def hasLower(self,p):
        for i in p:
            if i.islower():
                return True
        return False
        
    def hasUpper(self,p):
        for i in p:
            if i.isupper():
                return True
        return False
        
    def hasDigit(self,p):
        for i in p:
            if i.isdigit():
                return True
        return False
        
    def nonAlphaNumeric(self,p):
        for i in p:
            if not i.isalnum():
                return True
        return False
    def totalCombination(self,p):
        totalStrength = 0
        if (self.hasLower(p)):
            totalStrength +=1
        if (self.hasUpper(p)):
            totalStrength +=1
        if (self.hasDigit(p)):
            totalStrength +=1
        if (self.nonAlphaNumeric(p)):
            totalStrength +=1
        return totalStrength
    
    def passwordStrength(sef,a):
        if a == 1:
            return "Password Strength: Week "
        if a == 2:
            return "Password Strength: Acceptable "
        if a == 3:
            return "Password Strength: Strong "
        if a == 4:
            return "Password Strength: Super Strong "
            
            
    def same(self,p1,p2):
        if p1 !=p2:
            return False
        return True
    def passwordLength(self,p):
        if len(p)>=8:
            return True
        return False
    
    def processButton(self):
        p1 = self.password1.get()
        p2 = self.password2.get() 
        if not self.same(p1,p2): 
            self.v.set("Error: Password doesn't match")
            self.password2.set("")
            self.password1.set("")
        elif not self.passwordLength(p1):
            self.v.set("Error: Password must be at least 8 character")
            self.password2.set("")
            self.password1.set("")
        else:

           
            passwordStrength = self.passwordStrength(self.totalCombination(p1))
            self.v.set(passwordStrength)
            
            
            

        
password()

