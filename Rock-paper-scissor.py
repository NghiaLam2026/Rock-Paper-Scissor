import random

def rock_game():
    print("Welcome to the ultimate game of rock, paper, and scissor!")
    choices = ['rock', 'paper', 'scissor']
    user_c = input("Please choose rock, paper, or scissor: ")
    comp_c = random.choice(choices)
    if user_c == 'rock' and comp_c == 'paper':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("The computer have won!")    
    elif user_c == 'paper' and comp_c == 'rock':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("You have won!")
    elif user_c == 'paper' and comp_c == 'scissor':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print('The computer have won!')
    elif user_c == 'scissor' and comp_c == 'paper':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("You have won!")
    elif user_c == 'scissor' and comp_c == 'rock':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("The computer have won!")
    elif user_c == 'rock' and comp_c == 'scissor':
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("You have won!")
    else:
        print("You have chosen", user_c, "and the computer has chosen", comp_c)
        print("Tied!")
          
rock_game()