print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at a cross road, where do you want to go?")
print("Type: left or right")
user_input = input("Enter your choice: ").lower()
if user_input == "right":
    print("You have chosen poorly. Game over.")
elif user_input == "left":
    print("You arrive at a lake with an island in the center. Do you swim across or wait for a boat?")
    swim_or_wait = input("Typer: wait or swim: ").lower()
    if swim_or_wait == "swim":
        print("You have chosen poorly. Game over.")
    elif swim_or_wait == "wait":
        print("A boat arrives and ferries you to the island. On the island are three chests colored red, blue, and gold. Which do you open?")
        choice = input("Type: red, blue, or gold: ").lower()
        if choice == "red":
            print("You have chosen poorly. Game over.")
        elif choice == "blue":
            print("You have chosen poorly. Game over.")
        elif choice == "gold":
            print("Congratulations! You have found the treasure!")
        else:
            print("Please enter a valid input.")
    else:
        print("Please enter a valid input.")
else:
    print("Please enter a valid input.")