# Counter
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming

import time
num1 = int(input("What number would you like to start counting from?"))
num2 = int(input("What number would you like to end at?"))
num2 = num2 + 1
for x in range(num1, num2):
    print(x)
    time.sleep(0.07)
input("Press enter to exit terminal.")
