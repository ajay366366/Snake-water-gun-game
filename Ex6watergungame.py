#this is program for a water snake gun game
print (" Play Snake Water Gun Game!!!!")
outcomes=("snake","water","gun")
i=1
a=0 # player 1  win count
b=0 # player 2 count
turn=1
print ("You will get total 5 turn to play this game.")
while(i<=5):
    def game():
        import random
        random1= random.choice(outcomes)
        return(random1)
    player1 = game()
    print(f"\n       Turn - {turn}         ")
    turn+=1
    player2=input("Enter your choice snake,gun,or water..\n")
    if player2 == "snake" and player1 == "snake":
        print("Draw!!")
    elif player2 == "snake" and player1 == "water":
        print("You Win!!")
        a=a+1
    elif player2 == "snake" and player1 == "gun":
        print("You lost!!")
        b=b+1
    elif player2 == "water" and player1 == "water":
        print("Draw!!")
    elif player2 == "water" and player1 == "snake":
        print("You lost!!")
        b=b+1
    elif player2 == "water" and player1 == "gun":
        print("You Won!!")
        a=a+1
    elif player2 == "gun" and player1 == "water":
        print("You lost!!")
        b=b+1
    elif player2 == "gun" and player1 == "snake":
        print("You Win!!")
        a=a+1
    elif player2 == "gun" and player1 == "gun":
        print("Draw!!")
    else:
        print("Invalid option ,Please learn to Play this  games ")
    i = i + 1
    print(f"Computer chosen - ({player1})")
if a>b:
    print("\nOhh Yes Over all You Won",a,"-",b)
elif a<b:
    print("\nOh No, Over all You lost by",a,"-",b)
else:
    print("\nUff Game is  Drawn ,No body won ")

