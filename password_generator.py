"""
Program that stimulates an online password generator.
"""

import random

import os
os.system('clear')

from data import alphabets, numbers, symbols

print("Welcome to PyPassword Generator!!!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
char_password = ''

for x in range(num_letters):
    password.append(random.choice(alphabets))

for y in range(num_numbers):
    password.append(random.choice(numbers))

for z in range(num_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
for char in password:
    char_password += char

print(f"Here is your password: {char_password}")
