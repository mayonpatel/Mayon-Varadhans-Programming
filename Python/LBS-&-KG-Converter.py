# Weight converter: LBS & KG
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming
weight = float(input("What is your weight?")) # Prompt for weight
ogunit = str(input("What unit was your weight in? (KG/LBS)")) # Prompt for original unit

if ogunit == "KG":
    conversion = float(round(weight * 2.20462262, 2)) # Convert from KG to LBS
    print(f"Converted! You weigh {conversion} pounds.")
    input("Press enter to close terminal.")
elif ogunit == "LBS":
    conversion = float(round(weight / 2.20462262, 2)) # Convert LBS to KG
    print(f"Converted! You weigh {conversion} pounds.")
    input("Press enter to close terminal.")
else: # detect if input for original unit is invalid
    print("Invalid input!")
    input("Press enter to close terminal.")
