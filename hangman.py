import time
import string
from random import *
def hangman():
    word=choice(['ram','shyam','sita','gita','sandip','sudip','aarohi','sameer','saroj','binod','abhisek','bishal','rohit','subash','sadikshya','sarita'])
    validletters= string.ascii_letters
    turns=10
    guessedwords=""

    while len(word)>0:
        main=""
        for letter in word:
            if letter in guessedwords:
                main=main + letter
            else:
                main=main + "_" + " "

        if main==word:
            print(main)
            print("Congratulations,You won the game")
            break

        guess=print("Guess the word:",main)
        guess=input()


        if guess in validletters:
            guessedwords= guessedwords + guess.lower()

        else:
            print("Enter the valid letter")
            guess=input()

        if guess.lower() not in word:
            turns-=1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")
                break

print("This is a hangman game. Guess some famous Nepali names in less than 10 attempts")
name=input("Enter the name of the player:")
print("Loading the game")
for i in range(6):
    print("*", end=" ")
    time.sleep(0.5)
print()
print(f"Welcome to the game {name} .Best of luck buddy")
hangman()