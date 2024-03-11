import random
# To make ascii art
## http://patorjk.com/software/taag/#p=display&f=3D-ASCII&t=GUESS
logo =""""
                                                         
 ________  ___  ___  _______   ________   ________      
|\   ____\|\  \|\  \|\  ___ \ |\   ____\ |\   ____\     
\ \  \___|\ \  \\\  \ \   __/|\ \  \___|_\ \  \___|_    
 \ \  \  __\ \  \\\  \ \  \_|/_\ \_____  \\ \_____  \   
  \ \  \|\  \ \  \\\  \ \  \_|\ \|____|\  \\|____|\  \  
   \ \_______\ \_______\ \_______\____\_\  \ ____\_\  \ 
    \|_______|\|_______|\|_______|\_________\\_________\
                                 \|_________\|_________|

                                 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number beween 1 and 100")

attempts = 0

difficulty = input("Choose a difficulty. Type 'easy' or hard:\n").lower()
if difficulty == 'easy':
        attempts = 9
        print("You have 10 attempts remaining to guess the number")
elif difficulty == 'hard':
        attempts = 4
        print("You have 5 attempts remaining to guess the number")
number = random.randint(1,100)
#print(number)

keep_playing = True
while keep_playing:
    guess = int(input("Make a guess: "))
    if guess == number:
        keep_playing = False
        print(f"You got it! The answer was {number}")
    elif guess != number:
        if attempts == 0:
            keep_playing = False
            print(f'The number was {number}')
        if guess < number:
            print("Too low")
            attempts -=1
        elif guess > number:
            print("Too high")
            attempts -= 1
