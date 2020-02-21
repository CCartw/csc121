# Basic Comparisons
a = 4
b = 5

if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")

print ("Done")

# Indentation
if a == 1:
    print("If a is one, this will prnit")
    print("So will this")
    print("And this.")

print("This will always prin because it is not indented.")

# Using And/Or
if a < b and a < c:
    print ("a is less than b and c")

if a < b or a < c:
    print("a is less than either b or c (or both)")

# Boolean Variables
a = True
if a:
    print("a is true")
if not a:
    print("a is false")

a = 3
b = 3

c = a == b

print(c)

if 1: 
    print(1)
if "A":
    print("A")

if 0:
    print("Zero")

# The input Function

temperature = input("What is the temperature in Fahrenheit? ")
print("You said the temperature was " + temperature + ".")

temperature = input("What is the temperature in Fahrenheit? ")4
temperature = int(temperature)
if temperature > 90:
    print("It's hawt as shit outside.")

temperature = int(input("What is the temperatuer in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
print("Done")

# Else and Else If
temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
print("Done")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("Mans hot")
else:
    print("Mans not hot")
print("Done")

temperature = int(input("What is the temperature in Fahrenheit? "))
if temperature > 90:
    print("It is hot outside")
elif temperature > 110:
    print("*insert bruh sound effect here* that pretty fukin hot ngl")
elif temperature < 30:
    print('It is the temperature where a random northern will appear out of no where and will tell you its not cold, as soon as you mention the fact that it is cold')
else:
    print("It is cash money outside")
print("Done")

user_name = input("What is your name? ")
if user_name == "Collin":
    print("You have a fanFUCKINGtastic name.")
else:
    print("Your name is shit and not worthy of mentioning.")

if user_name == "Paul" or user_name == "Mary":

# Case Insensitive Comparisons
user_name = input("What is your name? ")
if user_name.lower() == "collin":
    print("You have the best name.")
else:
    print("Your name is shit.")

# Example if Statements
a = 4
b = 5
c = 6

if a < b:
    print("a is less than b")
if a > b:
    print("a is greater than b")
if a <= b:
    print("a is less than or equal to b")
if a >= b:
    print("a is greater than or equal to b")
if a == b:
    print("a is equal to b")
if a!= b:
    ("a and b are not equal")
if a < b and a < c:
    ("a is less than both b and c")
if a < b or a < c:
    print("a is less than either a or c (or both)")

a = True
if a = True:
    print("a is true")

if not a:
    print("a is false")

a = True
b = False

if a and b:
    print("a and b are both true")

a = 3
b = 3
c = a == b
print(c)

if 1:
    print("1")

if "A":
    print("A")

if 0:
    print("0")

if a == "B" or a == "b":
    print("a is equal to b.")

# Example 2: IF Statement
temperature = int(input("What is the temperature in Fahrenheit?"))
if temperature > 90:
    print("It is hot outside.")

# Example 2: Else Statement
temperature = int(input("What is the temperature in Fahrenheit?"))
if temperature > 90:
    print("It is hot outside.")
else: 
    print("It is not hot outside")
print("Done)")

# Example 3 if else statement
temperature = int(input("What is the temperature in Fahrenheit?"))
if temperature > 90:
    print("It is hot outside.")
elif temperature < 30:
    print("It is cold outside.")
else:
    print("It is not hot outside")
print("Done)")

# Example 4 ordering statements
temperature = int(input("What is the temperature in Fahrenheit?"))
if temperature > 90:
    print("It is hot outside.")
elif temperature > 110:
    print("Oh man, you could fry egges on the pavement!")
elif temperature < 30:
    print("It is cold outside.")
else:
    print("It is ok outside")
print("Done)")

# Comparisons using string/text
user_name = input("What is your name? ")
if user_name == "Paul":
    print("Your name is generic and stupid")
else:
    print("Your name is ok, but it's better than being named Paul.")