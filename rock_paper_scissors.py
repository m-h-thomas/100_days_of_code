import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Starting input
user_choice = int(input("Let's play rock paper scissors! Type '0' for Rock, '1' for Paper, '2' for Scissors: \n"))

#user input logic
if user_choice == 0:
    print("You chose Rock!" + rock)
elif user_choice == 1:
    print("You chose Paper!" + paper)
elif user_choice == 2:
    print("You chose Scissors!" + scissors)
else:
    print("Please enter a valid input!")
    exit()

#computer choice logic
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print("Computer chose Rock!" + rock)
elif computer_choice == 1:
    print("Computer chose Paper!" + paper)
else:
    print("Computer chose Scissors!" + scissors)

#win condition logic
if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 0:
    print("You Win!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")