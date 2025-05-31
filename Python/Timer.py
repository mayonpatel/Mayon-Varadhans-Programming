# Timer
# Programmed by Mayon & Varadhan
# GitHub: https://github.com/mayonpatel/Mayon-Varadhans-Programming

import time # import time library

secondsinput = int(input("Enter seconds")) # Prompt user for seconds

for x in range(secondsinput, 0, -1):
    seconds = x % 60 # seconds
    minutes = int(x / 60) % 60 # minutes
    hours = int(x / 3600) # hours
    print(f"00:{minutes:02}:{seconds:02}") # print time
    time.sleep(1) # wait 1 second then send next number.

print(f"Time is up, it has been {secondsinput} seconds!")
input("Press enter to close terminal.") # when enter is clicked, the console/terminal closes
