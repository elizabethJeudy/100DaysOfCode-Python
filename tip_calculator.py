print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n"))
print(f"${total_bill}")

tip_amt = int(input("How much tip would you like to give? 10, 12, or 15\n"))
print(f"{tip_amt}%")

split_bill = int(input("How many people to split the bill?\n"))
print(split_bill)

print(f"Each person should pay: ${(total_bill + tip_amt) / split_bill:.2f}")
