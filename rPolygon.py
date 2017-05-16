'''
Parameshor Bhandari
Date: 7th October,2014
COSC 2347
Title: Finding Polygon angle by using the sides from the user
'''
def rPolygonAngle(shape):
    angle = (180 * (shape - 2))/shape
    return angle
def main():
    sides = int(input("Please enter sides of a polygon:  "))
    a = rPolygonAngle(sides)     
    print("The interior angle of the shape having",sides," sides is: ",format(a,".2f"))             
main()
