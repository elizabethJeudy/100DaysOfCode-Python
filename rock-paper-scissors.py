import random


print("Let\'s play Rock, Paper, Scissors! You go first. What your choice: 0 for rock, 1 for paper, or 2 for scissors?")
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")


user_choice = int(input())
# computer chosing between 1 2 3 randomly
computer_choice = random.randint(0, 2)
