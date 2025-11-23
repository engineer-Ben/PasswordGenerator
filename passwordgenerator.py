import random
import string


letters = string.ascii_letters
numbers = string.digits
signs = "@#$%_&"
password = ""
all_chars = ""


length_pass = int(input("Enter the number of characters do you want in your password: "))
letter_pass = input("Do you want your password includes letters? (Y/N): ")
number_pass = input("Do you want your password includes numbers? (Y/N): ")
sign_pass = input("Do you want your password includes signs? (Y/N): ")

if letter_pass.upper() == "Y":
        all_chars += letters 

if number_pass.upper() == "Y":
    all_chars += numbers 

if sign_pass.upper() == "Y":
    all_chars += signs

if all_chars == "":
     print("YOU ARE STUPID, respectfully!!!")  
else:
     for _ in range(length_pass):
          password +=random.choice(all_chars)
     print(f"Your password is ready: {password}" )            
       



    
