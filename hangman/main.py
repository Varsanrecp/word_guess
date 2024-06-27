# hangman project
import random
from dataset import cricketers


def game():
    comp = random.choice(cricketers)

    find = []
    for i in range(len(comp)):
        find.append('_')

    print(find)
    guess = 8
    while '_' in find and guess > 0:
        predict = input("Guess a letter : ")
        if predict in comp:
            for i, j in enumerate(comp):
                if j == predict:
                    find.pop(i)
                    find.insert(i, j)
        else:
            print("Wrong prediction , Oops")
            guess -= 1
            print(f"your guess left {guess}")
        print(find)

    if '_' not in find and guess > 0:
        print("You found the word You WON")
    elif guess == 0:
        print(f"YOU OUT OF GUESSES YOU LOST {comp} was the word")
    else:
        print("doubt")


s = True
while s:
    game()
    a = input("Do you want to play again : ")
    if a == 'no':
        s = False
print("Thank you for playing")
