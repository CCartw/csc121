for i in range(5):
    print("I will not chew gum in class")

for i in range (5):
    print("Please,")
print("Can I go to the mall?")

for i in range (5):
    print("Please,")
    print("Can I go to the mall?")

repetitions = int(input("How many times should I repeat? "))

for i in range(repetitions):
    print("I will not chew gum in class.")

     def print_about_gum(repetitions):
 
for i in range(repetitions):
     print("I will not chew gum in class.")
    
def main():
     print_about_gum(10)


main()

for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in [2,6,4,2,4,6,7,4]:
    print(i)

for i in range(3):
    print("a")
for j in range(3):
    print("b")

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")

total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total = total + new_number
print("The total is: ", total)

total = 0
for i in range(1, 101):
    total = total + i
    print(total)

total = 0
for i in range(5):
    new_number = int(input( "Enter a number: "))
    if new_number == 0:
        total += 1
print("You entered a total of", total, "zeros")

i = 0
while i < 10:
    print(i)
    i = i + 1

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True

while True: # Loop forever
    quit = input("Do you want to quit? ")
    if quit == "y":
        break

    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        break

import random

for i in range(20):
    if random.randrange(5) == 0:
        print("DRAGON!!!")
    else:
        print("No dragon.")