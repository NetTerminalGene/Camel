import random

miles_traveled = 0
thirst = 0
camel_fatigue = 0
natives_distance = -200
canteen_drinks = 5

print("\nWelcome to Camel!")
print("You've stolen a camel to make your way across the great Gobi Desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives.")

done = False
while not done:
    print("\nA. Drink from your canteen.")
    print("B. Move ahead at moderate speed.")
    print("C. Full speed ahead.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    choice = input("\nYour choice? ")

    if choice.upper() == "Q":
        print(f"\nGOODBYE")
        done = True

    elif choice.upper() == "E":
        print(f"\nMiles traveled: {miles_traveled}")
        print(f"Drinks in canteen: {canteen_drinks}")
        print(f"The natives are {natives_distance} miles behind you.")

    elif choice.upper() == "D":
        camel_fatigue = 0
        print(f"\nYou stop for the night.")
        print(f"Your camel is happy!")
        natives_distance += random.randint(7, 14)

    elif choice.upper() == "C":
        miles_traveled += random.randint(10, 20)
        print(f"\nYou've traveled {miles_traveled} miles.")
        thirst += 1
        camel_fatigue += random.randint(1, 3)
        natives_distance += random.randint(7, 14)

    elif choice.upper() == "B":
        miles_traveled += random.randint(5, 8)
        print(f"\nYou've traveled {miles_traveled} miles.")
        thirst += 1
        camel_fatigue += 1
        natives_distance += random.randint(7, 14)

    elif choice.upper() == "A":
        if canteen_drinks != 0:
            canteen_drinks -= 1
            thirst = 0
            print(f"\nYou drink from your canteen.")
        else:
            print(f"\nYour canteen is empty!")

    if thirst > 4:
        print(f"\nYou are thirsty.")

    elif thirst > 6:
        print(f"\nYou've died of thirst.")
        print(f"\nGAME OVER")
        done = True

    if camel_fatigue > 5:
        print(f"\nYour camel is getting tired.")

    elif camel_fatigue > 8:
        print(f"\nYour camel is dead.")
        print(f"\nGAME OVER")
        done = True

    if natives_distance == 0:
        print(f"\nThe natives have caught you.")
        print(f"\nGAME OVER")
        done = True

    elif natives_distance >= 90:
        print(f"\nThe natives are getting close!")

    if miles_traveled >= 200 and (natives_distance > 0, thirst < 6, camel_fatigue < 8):
        print(f"\nYou've made it across the desert!")
        print(f"\nYOU WON")
        done = True
