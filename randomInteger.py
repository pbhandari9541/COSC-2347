'''
Parameshor Bhandari
Date: 7th October,2014
COSC 2347
Description: generate random integer and their average. the number of random
             integer will be prompted from user
'''             


import random
k = eval(input("Enter the number to generate random integers: "))
sum = 0;     
for i in range(1,k+1):
    randomNumber = random.randint(1,999)
    sum  += randomNumber
   # print("the random integer", i, 'is',randomNumber,)

print("\nthe average of",k,"integers is :",format(sum/k, "5.2f")) 
