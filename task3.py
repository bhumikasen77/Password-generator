import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u' ,'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
           'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to password generator")
num_of_letter=int(input("How many letter you want in your password?\n"))
num_of_symbols=int(input("How many symbols you want in your password?\n"))
num_of_numbers=int(input("How many numbers you want in your password?\n"))
password=""
for i in range(1,num_of_letter+1):
    char=random.choice(letters)
    password = password+char
for i in range(1,num_of_symbols+1):
    char = random.choice(symbols)
    password += char
for i in range(1,num_of_numbers+1):
    char = random.choice(numbers)
    password += char
print(password)