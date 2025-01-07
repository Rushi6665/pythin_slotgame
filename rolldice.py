""" import random

while True:
    user_choice = input("Do you wnat to roll the dice? (Y/N)- ")
    if 'Y' in user_choice or 'N' in user_choice:
        if user_choice =='Y':
            value1 = random.randrange(1,6)
            value2 = random.randrange(1,6)
            print(value1,value2)
        else:
            print("Thank you for playing!")
            break
    else:
        print("please enter valid input")
 """






""" import random

system_number = random.randint(1, 100)
print(system_number)
while 1:
    guess = int(input("Please guess the number between 1-100 "))
    
    if system_number == guess:
        print("Congractulations!! You have guessed correct")
        break
    elif system_number < guess:
        print("Your guess is too high")
    else:
        print("Your guess is too low. Try again") """
        
        
        
""" #ROCK PAPER SCISSOR

import random


while True:
    user_input = input("Choose your option between r,p and s- ")
    options = ['r','p','s']
    comp_input = random.choice(options)
    print("computer choose- "+comp_input)

    if \
        (user_input=='s' and comp_input=='r') or \
        (user_input=='p' and comp_input=='s') or \
        (user_input=='r' and comp_input=='p'):
        print("You lost it")
        
    elif user_input== comp_input:
        print("its a tie")
    
    else:
        print("You won")
     
    play_again = input("do you want to play again?- (y/n)  ")
    if play_again=='n':
        break
     """
        
        



