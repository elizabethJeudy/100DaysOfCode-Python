# using random and lists, create a program that randomly generates who will pay the bill

import random

friends = ["Elizabeth", "Yahaira", "Jeyson", "Eve", "Wadlene"]

# random.choice allows for multiple values vs .randit
payer = random.choice(friends)


print(f"{payer} is going to pay the bill today!")
