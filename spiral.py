import turtle
def main():
 side = 10
 n = int(input("How many sides do you want on your spiral square?  "))
 turtle.showturtle()
 turtle.pendown()
 for i in range(n):
     turtle.forward(side)
     turtle.right(90)
     side = side + 10
main()
