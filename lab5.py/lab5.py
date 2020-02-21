import random

def print_intro():
    print("Welcome to Camel!")
    print("\nIn your desperation, you have stolen a camel to make your way")
    print("across the great Mobi desert.")
    print("The locals want their camel back and are chasing you down!")
    print("Survive your desert trek and out run the locals.\n")

def main():
    print_intro()

    milesTraveled = 0
    thirst = 0
    camelTiredness = 0
    localTraveled = -20
    drinks = 3
    oasis = -1

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.\n")  
        choice = input("Your choice? ")
       
        if choice.upper() == "Q" :
            done = True
        elif choice.upper() == "E":
            print("Miles Traveled: ", milesTraveled)
            print("Drinks in canteen: ", drinks)
            print("The locals are", milesTraveled - localTraveled, "miles behind you.\n")
        elif choice.upper() == "D":
            camelTiredness = 0 
            print("The camel is happy!\n")
            localTraveled += random.randrange(7,14)
        elif choice.upper() == "C":
            milesTraveled += random.randrange(10,20)
            print("You have traveled", milesTraveled, "miles.")
            thirst += 1
            camelTiredness += random.randrange(1,3)
            localTraveled += random.randrange(7,14)
            oasis = random.randrange(1, 20)
        elif choice.upper() == "B":
            milesTraveled += random.randrange(5, 12)
            print("You have traveled", milesTraveled, "miles.")
            thirst += 1
            camelTiredness += 1
            oasis = random.randrange(1, 20)
            localTraveled += random.randrange(7,14)
        elif choice.upper() == "A":
            if drinks > 0:
                drinks -= 1
                thirst = 0
            else:
                print("Uh oh, you have no drinks left!")
        if milesTraveled >= 200:
                print("You have successfully escaped and won!")
                done = True
        if thirst > 6:
            print("You died of thirst!")
            done = True
        elif thirst > 4:
            print("You are thirsty.")
        if camelTiredness > 8:
            print("Your camel is dead!")
            done = True
        elif camelTiredness > 5:
            print("Your camel is gettng tired.")
        if localTraveled >= milesTraveled:
            print("The locals have caught you!")
            done = True
        elif localTraveled + 15 >= milesTraveled:
            print("The locals are getting close!")
        if oasis == 2:
            thirst = 0
            camelTiredness = 0
            drinks = 3
            print("You have stumbled across an oasis!")
            print("Your thirst, drinks, and camel tiredness have been reset!")

if __name__ == '__main__':
    main()

# It still displays oasis text if dead.