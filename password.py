#Creating a simple Password Generator

import random

cap_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=;:,.<>?/~`"

upper,lower,digits,special = True,True,True,True

finalpass = ""

if upper:
    finalpass += cap_letters
if lower:
    finalpass += low_letters
if digits:
    finalpass += numbers
if special:
    finalpass += symbols
    
length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(finalpass,length))
    print(password)
    
# This code generates a password of length 20 using uppercase letters, lowercase letters, digits, and special characters.




