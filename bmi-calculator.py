# Add some if / elif / else statements to the BMI calculator so that it interprets the BMI values calculated.
# If the bmi is under 18.5 (not including), print out "underweight"
# If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
# If the bmi is 25 (including) or over, print out "overweight"


print("Welcome to the BMI calculator!")
weight = float(input("Enter your weight in lbs: \n"))
height = float(input("Enter your height in inches: \n"))

bmi = weight / (height ** 2) * 703

if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5 and bmi < 25:
    print("normal weight")
else:
    print("overweight")

print(f"Your BMI is {bmi:.2f}")
