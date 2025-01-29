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

computer_choice = random.randint(0, 2)
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choices_available = [rock, paper, scissors]

print(choices_available[player_choice])
print("And the computer chooses: ")
print(choices_available[computer_choice])

if computer_choice == player_choice:
    print("It is a draw")
elif computer_choice == 0 and player_choice == 1:
    print("You Won")
elif computer_choice == 0 and player_choice == 2:
    print("Computer Won")
elif computer_choice == 1 and player_choice == 0:
    print("Computer Won")
elif computer_choice == 1 and player_choice == 2:
    print("You Won")
elif computer_choice == 2 and player_choice == 0:
    print("You Won")
elif computer_choice == 2 and player_choice == 1:
    print("Computer Won")   