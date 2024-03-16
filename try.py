# Importing module
from pyfiglet import Figlet
import time
import colorama
from colorama import Fore

# Initializing colorama
colorama.init()

# Setting Font
font = Figlet(font="cosmic")

# Inputs:
user_name = str(input("What is your name? (Last name, Given name M.I.): "))
user_dream_job = str(input("What is your dream job?: "))

# Animation speed (lower is faster)
speed = 0.05

# Outputs:
print("--------------------------------------------------")

# Animate name rendering
for char in user_name:
    print('\033[95m' + font.renderText(char), end='', flush=True)
    time.sleep(speed)
print("\nYour name is:")
time.sleep(0.5)  # Pause for emphasis

# Animate dream job rendering
for char in user_dream_job:
    print('\033[95m' + font.renderText(char), end='', flush=True)
    time.sleep(speed)
print("\nYour dream job is:")
time.sleep(0.5)  # Pause for emphasis

print("--------------------------------------------------")
