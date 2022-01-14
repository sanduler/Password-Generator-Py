# Name: Ruben Sanduleac
# Date: 01/14//2022
# Description:

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = ''
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

print(letters)

for letter in range(0, nr_letters):
    rand_number = random.randint(0, 51)
    let = letters[rand_number]
    total += let
for number in range(0, nr_numbers):
    rand_number = random.randint(0, 8)
    num = numbers[rand_number]
    total += num
for symbol in range(0, nr_symbols):
    rand_number = random.randint(0, 7)
    sym = symbols[rand_number]
    total += sym
print("\n")
print(''.join(random.sample(total, len(total))))
