import random
import string

print("Welcome to the Python Password Generator!")

string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

letters = int(input("How many letters would you like in your password? \n"))

ll = []
for l in range(0,letters):
    ll.append(random.choice(string.ascii_letters))

string.symbols = '''!@#$%^&*()}{:"><?,./;'[]'''

symbols = int(input("How many symbols would you like in your password? \n"))

ss = []
for s in range(0,symbols):
    ss.append(random.choice(string.symbols))


string.numbers = "1234567890"

numbers = int(input("How many numbers would you like in your password? \n"))

nn = []
for n in range(0,numbers):
    nn.append(random.choice(string.numbers))

pass_word = []
pass_word.append(ll+ss+nn)


for passs in range(len(pass_word)):
    new_pass = pass_word[passs]

new_pass = ''.join(random.sample(new_pass,len(new_pass)))

print(f"Here is your password: {new_pass}")
