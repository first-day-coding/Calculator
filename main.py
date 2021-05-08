#Hey guys, today, we are going to make a very simple calculator
#The code will be in the description
#This should work as long as you have python installed
#Enjoy

#Defining the numbers
number_one = 0
number_two = 0
result = 0
operation= 0

#Making four functions
def add():
    global result
    result = number_one + number_two

def minus():
    global result
    result = number_one - number_two

def times():
    global result
    result = number_one * number_two

def divide():
    global result
    result = number_one / number_two

#Making the program asking the questions

number_one = float(input("Enter your first number: "))
number_two = float(input("Enter your second number: "))

print("Enter one if you want to add the two numbers.")
print("Enter two if you want to minus the two numbers.")
print("Enter three if you want to times the two numbers.")
print("Enter four if you want to divide the two numbers.")

while (operation != 1) and (operation != 2) and (operation) != 3 and (operation != 4):
    operation = int(input("Enter your operation number: "))

if operation == 1:
    add()
elif operation == 2:
    minus()
elif operation == 3:
    times()
elif operation == 4:
    divide()

print("The result is " + str(result))

#Like and subscribe if this is helpful
#See you all in the next vid
#https://www.youtube.com/channel/UCAdHSy6KF9vFuPm0INi30Tg
