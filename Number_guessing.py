import random
def game():
    a=[4,5,8,9]
    b=int(input("Enter another number"))
    c=random.choice(a)
    print(c)
    if(b!=c):
        print("You have lost the game")
        game()
    else:
        print("You have won the game")
game()
        
