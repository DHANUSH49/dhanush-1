#!/usr/bin/python3
import random
# system choses random numbers
n=(int(input("press 7 to play")))
i=0
j=0
while(n==7):
    t=["Rock","Paper","Scissors"]
    Computer=t[random.randint(0,2)]
    # system chooses a random number from 0 to 2
    print("Enter your Choice:-")
    # it is used to choose your choice
    Player="False"
    Player=input("Rock, Paper, Scissors")
    if(Computer==Player):
        print("Tie!")
    elif(Computer=="Rock"):
        # system chooses its choice 
        if(Player=="Paper"):
            print("The computer played: ",Computer)
            # played by system
            print("The Player played: ",Player)
            # played by user
            print("The Paper Wraps the Stone!")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")
            j=j+1
    elif(Computer=="Paper"):
        if(Player=="Scissors"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("The Scissors Cuts Paper!")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")

            j=j+1
    elif(Computer=="Scissors"):
        if(Player=="Rock"):
            print("The computer played: ",Computer)
            print("The Player played: ",Player)
            print("Rock Breaks the Scissors")
            print("Player Wins!")
            i=i+1
        else:
            print("Computer Wins")
            # system wins
            j=j+1
    else:
        print("Enter Choice again")
    if(i>j):
        print("Player leads by ",i-j)
    elif(i==j):
        print("The Scores are tied ")
    else:
        print("Computer leads by ",j-i)
