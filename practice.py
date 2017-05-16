import turtle
def concentricCircles(n,radius,step):
    turtle.showturtle()
    i = 0
    while i< n+1:
        turtle.showturtle()
        turtle.circle(radius)
        radius +=step
number = eval(input('enter number of circles: '))
rad = eval(input("enter radius: " ))
inc = eval(input("enter step : "  ))
concentricCircles(number,rad,inc)
