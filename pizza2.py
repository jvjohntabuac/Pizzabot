# pizza bot program
from doctest import OutputChecker
import random
from random import randint 

# list of random names
names = [ "John", "Michel", "Ana", "Hizhenberg", "Luke", "Jonathan", "Michel", "Alex", "Iris", "Mia" ]

num = randint(0,9) 

name = (names[num])

print(name)

def welcome():
    num = randint(0,9)
    name = (names[num])
    print("*** welcome to pizza ***")
    print(" my name is",name, "***")
    print("***I will be here to help your order***")

def main():

    '''
    comments 
    Purpose to run functions 
    a welcome message
    paramiters: none 
    returns: none 
    '''
    welcome()

main()

    
print("Do you want to pick up or delivery?")

print ("For delivery type 1")
print ("For delivery 1 or enter 2 for pickup")

delivery = input()

if delivery == "1": 
    print ("Delivery")
    
elif delivery == "2":
    print ("Pickup")
    
else:
     print("invalid response please use the options")

while True:
    try:
        delivery = int(input("please enter a valid option"))
        if delivery >= 1 and delivery <= 2:
         if delivery == 1:
            print("Pickup")
            break
        elif delivery == 2:
            print ("Delivery")
            break
        else:
            print("wrong")
    except ValueError:
        print("this is not a valid number")
        print("please enter 1 or 2")