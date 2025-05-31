# Compound Interest Calculator
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming
principle = float(input("What is the starting amount? "))
while principle <= 0:
    print("The starting amount cannot be less than or equal to 0.")
    principle = float(input("What is the starting amount? "))
rate = float(input("What is the interest rate? "))
while rate <= 0:
    print("The interest rate cannot be less than or equal to 0.")
    rate = float(input("What is the interest rate? "))
time = float(input("What is the time in years? "))
while time <= 0:
    print("The time in years cannot be less than or equal to 0.")
    time = float(input("What is the time in years? "))
total = principle * pow((1 + rate / 100), time)
print (f"You would have ${total:.2f} after {time} years!")
