from random import randint
print('This is a number guessing game.You have to guess the number in 6 attempts, otherwise you lose!! Best of luck')
x= randint(1,50)
for i in range(6):
    num=int(input("Guess a number from 1 to 50:"))
    if num<x:
        print("You hit the number a bit low")
        if i==5:
            print("Sorry,the game has ended")
            break;
        print(f"You have {5-i} attempts left! Try again")
    elif num>x:
        print("You hit a number a bit high")
        if i==5:
            print("Sorry,the game has ended")
            break;
        print(f"You have {5 - i} attempts left! Try again")
    else:
        print("Congratulations!You hit the number right")
        break;

