# based on user order determine final bill
# small pizza = 15
# medium pizza = 20
# large pizza = 25
# add pepperoni for small pizza = +2
# add pepperoni for medium or large pizza = +3
# add extra cheese for any size pizza = +1


print("Welcome to Python Pizza Deliveries!")

size = input('What size pizza do you want? S, M, or L:\n')
pepperoni = input('Do you want pepperoni? Y or N:\n')
extra_cheese = input('Do you want extra cheese? Y or N:\n')
bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill += 3
else:
    bill = 25
    if pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bil is: ${bill}. Enjoy your pizza!")
