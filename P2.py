# Importing module
from pyfiglet import Figlet

# Setting Font
font = Figlet(font="cosmic")

# Inputs:
user_name = str(input("What is your name? (Last name, Given name M.I.): "))
user_dream_job = str(input("What is your dream job?: "))

# Outputs:
print("--------------------------------------------------")
text_style1 = (font.renderText(user_name))
print('\033[91m' + "Your name is: ")
print('\033[93m' + text_style1)
text_style2 = (font.renderText(user_dream_job))
print('\033[91m' + "Your dream job is: ")
print('\033[93m' + text_style2)
print("--------------------------------------------------")
