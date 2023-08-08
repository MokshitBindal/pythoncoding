print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to the treasure island.")
print("Your mission is to find the Treasure.")
print("       You have 3 lives, make them count.       ")
game_won = False

for i in range(1, 4):
    print(f"This is your life number - {i}")
    print("*" * 100)
    first_choice = input("You\'re at a cross road,where do you want to go? Left or Right: ").casefold()
    if first_choice == "left":
        second_choice = input("You are now near a lake \n"
                              "You can see a house on the other side. \n"
                              "Type 'wait' to wait for a boat or 'swim' to swim across: ")

    elif first_choice == "right":
        print("You are in a jungle and feeling lost, Game Over.")
        i += 1
        continue

    else:
        print("Give valid input only please.")
        continue

    print("*" * 100)

    if second_choice == "wait":
        third_choice = input("A fisherman came and you asked him for help. \n"
                             "He obliged and helped tou reach the house safely. \n"
                             "You entered the house, through the open main gate and saw 3 doors. \n"
                             "The doors are of red, green and blue colour, which one do you choose to go in? ")

    elif second_choice == "swim":
        print("While you were swimming,half way across the river, you hear something in the water \n"
              "like a fish near your legs,you dunk down and see a electric eel \n"
              "it touches your legs just as you saw it \n"
              "LAGE 440V CHUNE SE TERE, Game Over.")
        i += 1
        continue


    else:
        print("Give valid input only please.")
        continue

    print("*" * 100)

    if third_choice == "green":
        print("YOU FOUND THE TREASURE, Enjoy being the KING of this World.")
        game_won = True
        break

    elif third_choice == "blue":
        print("You entered the blue door and suddenly a lion jumped on you, Game Over")
        i += 1
        continue

    elif third_choice == "red":
        print("Just as you entered the room,you are down in the river \n"
              "you hear something in the water \n"
              "like a fish near your legs,you dunk down and see a electric eel. \n"
              "it touches your legs just as you saw it, \n"
              "LAGE 440V CHUNE SE TERE, Game Over. ")
        i += 1
        continue
    else:
        print("Please give valid input")
        continue

if game_won == True:
    print("Congratulations on winning the game.")
else:
    print("You lost, maybe next time.")

input()
