#Week 3
'''#1
for i in range(1,11):
    print(i)

#2
for a in range(2,21,2):

    print(a)

#3
for a in range(1,16,2):
    print(a)

#4
for a in range(1,11):
    print(a**2)

#5
list1=["apple","banana","cherry"]
for element in list1:
    print("Element:",element) '''

'''#1
for a in range(1,11):
    print(a)

#2
for a in range(2,21,2):
    print(a)
#3
for a in "hello":
    print(a)
#4
b=0
for a in range(1,21):
    b=b+a
print(b)

#5
a=11
for i in range(2,12):
    a=a-1
    print(a)
#6
for i in range(1,6):
    print(i**2)
#7
names=["John","Alice","Bob"]
for name in names:
    print(name)'''

#WHILE LOOPS
'''#1
count=0
while count<10:
    count=count+1
    print(count)
print()
#2
count1=11
while count1>1:
    count1=count1-1
    print(count1)'''

'''#3
count=0
while count<19:
    count=count+2
    print(count)
#4
while True:
    num=float(input("Enter a number:"))
    if num==0:
        print("Correct")
        break
    else:
        print("Not Correct")'''

'''#1
while True:
    password=input("Enter the password:")
    if password=="Python123":
        print("Access granted!")
        break
    else:
        print("Wrong password, try again")
#2
while True:
    num=float(input("Enter a number:"))
    if num>0:
        print("Thank you!")
        break
    else:
        print("Number must be positive")
#3
secret_number=7
while True:
    guess=int(input("Enter your guess:"))
    if guess==secret_number:
        print("You got it!")
        break
    else:
        print("Try again")'''
#1
try:
    num=float(input("Enter a number:"))
    print(num)
except ValueError:
    print("This is not a number")
#2
try:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    print(num1/num2)
except ZeroDivisionError:
    print("You can't divide by 0")
#3
try:
    age=int(input("Enter your age:"))
    if age<=0:
        raise ValueError("Age can't be negative")
    print(age)
except ValueError:
    print("Age can't be negative")
#4
try:
    a=float(input("Enter the first number:"))
    b=float(input("Enter the second number:"))
    print(a/b)
except ValueError:
    print("Enter numbers")
except ZeroDivisionError:
    print("You can't divide by 0")
        
