#1. This is a comment

# print("Hello") This is a commemt

#2. Variables 
x = 10
y = 'coding'

print(x)
print(y)


x = str(10)
y = int("3")
z = float(3)

print(x)
print(y)
print(z)

x = 'coding'
y = "coding"

print(x)
print(y)


A = "Python"
a = "Variables"

print(A)
print(a)

# Data Types 

x = 1
y = 2.8

print(type(x))
print(type(y))

# Strings 

a =  """Hi I am Ricky J. Sparks, A very hard-working engineer, 
totally committed to excellence, and also someone who wants to continually improve 
and develop my skillset to ensure I maintain competence in my role. 
I will be able to start contributing positively towards the team's goals, 
whilst also bringing a positive, can-do attitude to the organization and those I am working alongside."""

print(a)

a = ("Hello World")

print(a[1])
print(len(a))

# Booleans 

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 100
b = 50

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))


print(bool("abc"))
print(bool(123))
print(bool(["apple, cherry, banana"]))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool({}))

# Operators 

a = ["apple"]
b = ["banana"]

print(a + b)

# Operators 

# (+) --> addition 
# (-) --> subtraction 
# (*) --> multiplication 
# (%) --> modulus 

# Assignment operators 

# x += 3 or x = x + 3
# x -= 3 or x = x - 3 

# Comporator Operators

# == --> Equal to 
# >= --> Greater than or equal to 
# <= --> Lesser than or equal to 

# Python List 

list = ["apples", "bananas", "oranges", "apples", "oranges"]

print(list)
print(len(list))

# Tuples 

tuple = ("apples", "bananas", "oranges")

print(tuple)
print(len(tuple))

this_tuple = ("apples",)
print(this_tuple)

# Sets

set = {"apples", "bananas", "oranges", "apples"}

print(set)

# Dictionaries 

dictionary = {
    "brand": "Ford",
    "model": "Focus",
    "year": 2010,

}

print(dictionary)

# Conditional Statements 

a = 100 
b = 100

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are both equal")
else: 
    print("a is greater than b")

# Python While Loops

i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# For Loops 

fruits = ["apple", "banana", "orange"]

for x in fruits: 
    print(x)
else: 
    print("Its done!")

# Functions 

def function():
    print("Hello, I'm a function created by Ricky Sparks!")

function()
# Function with a argument
def name(name):
    print(name)

name("Ricky")