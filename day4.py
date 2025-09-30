# Day 4 – Loops

# Program 1: Print numbers 1 to 10
for i in range(1, 11):
    print(i)

# Program 2: Sum of first 10 natural numbers
total = 0
for i in range(1, 11):
    total += i
print("Sum:", total)

# Program 3: Countdown using while loop
n = 5
while n > 0:
    print("Countdown:", n)
    n -= 1

# Program 4: Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Program 5: Factorial using loop
fact = 1
n = int(input("Enter a number for factorial: "))
for i in range(1, n + 1):
    fact *= i
print("Factorial:", fact)