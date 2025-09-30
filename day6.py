#1️⃣ Dictionaries – Basics

my_dict = {"name":"alice","age":20,"city":"delhi"}
print(my_dict["name"])

my_dict["age"] = 21
my_dict["country"] = "India" 
print(my_dict)

del my_dict["city"]
print(my_dict)

#2️⃣ Iterating Through a Dictionary

for key in my_dict:
    print(key)

for values in my_dict.values():
    print(values)

for key , values in my_dict.items():
    print(key,":",values)

#3️⃣ Sets – Basics

my_set = {1,2,3,3,4}
print(my_set)

my_set.add(5)
my_set.remove(2)
print(my_set)

#Set Operations

a={1,2,3}
b={2,3,4}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#examples

st_dict = {"name":"sash","age":19,"marks":73}
print(st_dict["name"])

st_dict["marks"] = 95
st_dict["grade"] = "A"
del st_dict["age"]
print(st_dict)

items = {"apple":50,"banana":20,"orange":30}

for key in items.values():
    print(key)

for value in items:
    print(value)

for key, value in items.items():
    print(key,":",value)