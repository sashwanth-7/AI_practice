#1️⃣ if statement basics

age = 18 
if age>=18:
    print("you are eligible to vote")

#2️⃣ if-else

num = 5
if num%2 == 0:
    print("even number")
else:
    print("odd number")

#3️⃣ if-elif-else ladder

mark = 85
if mark>=90:
    print("grade A")
elif mark>=75:
    print("grade B")
elif mark>=50:
    print("grade C")
else:
    print("fail")

#4️⃣ Nested if

num = 12
if num>=0:
    if num % 2 ==0:
        print("positive even number")
    else:
        print("positive odd number")
else:
    print("negarive number")

#1️⃣ Check Positive/Negative/Zero

num = float(input("enter a number:"))
if num >0:
    print("positive number")
elif num<0:
    print("negative number")
else:
    print("the number is zero")

#Find the Largest of 3 Numbers

num1 = float(input("enter number1: "))
num2 = float(input("enter number2: "))
num3 = float(input("enter number3: "))

if num1>=num2 and num1>=num3:
    print("the greatest number is:",num1)
elif num2>=num1 and num2>=num3:
    print("the greatest number is:",num2)
else:
    print("the greatest number is:",num3)

#3 – Even or Odd

num = int(input("enter a number:"))

if num%2 == 0:
    print ("the number is even")
else:
    print ("the number is odd")

#4 – Grade Calculator

marks = float(input("enter your marks(0=100) : "))

if marks>=90:
    print("grade A")
elif marks>=75:
    print("grade B")
elif marks>=50:
    print("grade C")
else:
    print("fail")

#5 – Nested Conditions (Age & Permission)

age = int(input("enter your age:"))
if age>=18:
    id_proof = input("do yuo have id proof (yes/no):").lower()
    if id_proof == "yes":
        print("you can enter")
    else:
        print("show id proof")
else:
    print("not allowed")