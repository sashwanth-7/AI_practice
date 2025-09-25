fruits = ["apple","banana","mango","date"]
print("fruits list:", fruits)

print("first fruit:", fruits[0])

print("last fruit:", fruits[-1])

print("first 2 fruits:", fruits[0:2])

fruits.append("elderberry")
print("after append:", fruits)

fruits.pop(1)
print("after pop:", fruits)

# Tuple example

numbers = (10,20,30,40,50)

print("tuple numbers:",numbers)
print("first number:",numbers[0])
print("last number:",numbers[-1])
print("first 3 numbers:",numbers[:3])

# count() → tells how many times a value appears

print("count of 20:",numbers.count(20))

# index() → tells the position of a value

print("index of 40:",numbers.index(40))

# Set example

fruits = {"apple","banana","apple","mango"}
print("fruits set:",fruits)
print("is 'banana in set?","banana" in fruits)

fruits.add("orange")
print("after add:",fruits)

fruits.remove("mango")
print("after remove:",fruits)

# Union & Intersection

set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("union:", set1.union(set2))
print("intersection:", set1.intersection(set2))

# dictionary example

student = {
    "name": "Sashwanth",
    "age": 19,
    "college": "Mahendra Engineering College",
    "cgpa": 7.3,
    "hosteller": False
}
print("student dictionary:", student)


# accessing values
print("name:",student["name"])
print("age:",student["age"])

# adding a new key-value pair
student["semester"] = 5
print("after adding semester:",student)


# updating a value
student["cgpa"] = 7.5
print("after updating cgpa:",student)


# updating a value
student.pop("hosteller")
print("after removing:",student)


# updating a value
print("keys:",student.keys())
print("values:",student.values())