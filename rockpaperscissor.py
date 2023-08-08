import random

valid = True
choice = int(input("Choose any one: 1 for rock, 2 for paper, 3 for scissor "))
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
if choice < 1 or choice > 3:
    valid = False
    print("invalid input")
elif choice == 1:
    print("You chose:\n", rock)
elif choice == 2:
    print("You chose:\n", paper)
elif choice == 3:
    print("You chose:\n", scissors)

if valid == True:
    game = [rock, paper, scissors]
    comp_choice = random.choice(game)
    print("Computer chose:\n", comp_choice)

    if choice == 1 and comp_choice == scissors:
        print("you won")
    elif choice == 2 and comp_choice == rock:
        print("you won")
    elif choice == 3 and comp_choice == paper:
        print("you won")
    else:
        if choice == 1 and comp_choice == rock:
            print("draw")
        elif choice == 2 and comp_choice == paper:
            print("draw")
        elif choice == 3 and comp_choice == scissors:
            print("draw")
        else:
            print("you lost")
