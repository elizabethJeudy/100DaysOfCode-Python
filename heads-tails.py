# create program that random generates either heads or tails

import random

heads_or_tails = random.randint(0, 1)

if heads_or_tails == 0:
    print("Tails")
else:
    print("Heads")
