import random

print('Welcome to the PyPassword Generator!')
letters_1 = int(input('How many letters would you like in your password?\n'))
symbols_1 = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
let = []
random_capital = 0
for s in range(0,letters_1):
    selector = random.randint(0,25)
    cap = random.randint(0,1)
    if cap == 1:
        let.append(letters[selector])
    elif cap == 0:
        new_cap = letters[selector]
        new_cap = new_cap.upper()
        let.append(new_cap)


symbols= ['!','@','#','$','%','^','&','*']
sym = []
for s in range(0,symbols_1):
    selector = random.randint(0,7)
    sym.append(symbols[selector])



num = []
for nums in range(0,numbers):
    rand = random.randint(0,9)
    num.append(rand)

password = num+sym+let

# random.shuffle(password)
# password = ''.join(password)

### convert all items in list to string objects
new = []
for i in password:
    new += str(i)

### create single list called password with all items from the password list
password = ''.join(new)

### shuffle and print
password = ''.join(random.sample(password,len(password)))
print(password)


# print(f"Here is your password: {password}")
