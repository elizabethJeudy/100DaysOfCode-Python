import random


print("Let\'s play Rock, Paper, Scissors! You go first. What your choice: 0 for rock, 1 for paper, or 2 for scissors?")

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


user_choice = int(input("Chose a number: 0, 1, or 2\n"))
# computer chosing between 0,1 2 randomly
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print("You chose Rock")
    print(rock)
    if computer_choice == 0:
        print("Computer chose Rock, it\'s a tie!")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose Paper, you lose!")
        print(paper)
    else:
        print("Computer chose Scissors, you win!")

elif user_choice == 1:
    print("You chose Paper")
    print(paper)
    if computer_choice == 0:
        print("Computer chose Rock, you win!")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose Paper, it\'s a tie!")
        print(paper)
    else:
        print("Computer chose Scissors, you lose!")
        print(scissors)

elif user_choice == 2:
    print("You chose Scissors")
    print(scissors)
    if computer_choice == 0:
        print("Computer chose Rock, you lose!")
        print(rock)
    elif computer_choice == 1:
        print("Computer chose Paper, you win!")
        print(paper)
    else:
        print("Computer chose Scissors, it\'s a tie!")
        print(scissors)
else:
    print("You've entered an invalid number, try again!")
