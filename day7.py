#File Handling & Exception Handling

f = open("sample.txt","w")
f.write("Hello, this is Day 7 - File Handling!\n")
f.write("This file was created using Python.\n")
f.close()

print("file written successfully.")

#Read from a file

f = open("sample.txt", "r")
content = f.read()
f.close()
print("File content is:\n")
print(content)

#Append to a file

f = open("sample.txt","a")
f.write("this line was appended at the end.\n ")
f.close()
print("file appended successfully")

#Read file line by line

f = open("sample.txt","r")
for line in f:
    print(line.strip())
f.close()

#Exception handling

try:
    num1 = int(input("enter a number:"))
    num2 = int(input("enter another number:"))
    reuslt = num1/num2
    print("Result",reuslt)
except ValueError:
    print("Error:please enter a valid integer")
except ZeroDivisionError:
    print("Error:division by zero is not allowed")
finally:
    print("execution finished.")

#1. Count the number of lines in a file

with open("sample.txt","r") as f:
    lines = f.readlines()
    print("Number of lines:", len(lines))

#2. Write numbers 1–10 into a file

with open("numbers.txt","w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

print("Numbers written successfully.")

#3. Read the file and print only even numbers

with open("numbers.txt","r") as f:
    for line in f:
        num = int(line.strip())
        if num % 2 == 0:
            print(num)

#4. Handle division error (ZeroDivisionError)

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#5. Handle file not found error

try:
    with open("nofile.txt","r") as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("Error: File does not exist!")
