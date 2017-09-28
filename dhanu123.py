#!/usr/bin/python3
import random
# system choses the random numbers
count=0
r=0
while count<=100:
    roll=input("press r to roll the dice")
    # r is used to roll the dice 
   if roll=="r":
        r=random.randint(1,6)
        # it gives random numbers between 1 to 6
        count=count+r
        print("your random num is",r)
        print("you are on count",count)
        if count==8:
           count=37
           print("wow.....up the ladder",count)
        elif count==11:
             count=2
             print("omg...down the ladder",count)
        elif count==13:
              count=34
              print("yess...pu the ladder",count)
        elif count==25:
              count=4
              print("shit not again ...down the ladder",count)
        elif count==38:
             count=9
             print("dam...down the ladder",count)
        elif count==40:
             count=68
             print("yuppe...up the ladder",count)
        elif count==52:
             count=81
             print("finally....up the ladder",count)
        elif count==65:
             count=46
             print("nooo...down the ladder",count)
        elif count==76:
             count=97
             print("wow...up the ladder",count)
        elif count==89:
             count=70
             print("saddd...down the ladder",count)
        elif count==93:
             count=64
             print(":(...down the ladder",count)
        elif count>=100:
             print("you are always the winner")

