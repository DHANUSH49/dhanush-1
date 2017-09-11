#!/usr/bin/python3
import random

op = ["rock","paper","scissors"]
AI = op[random.randint(0,3)]
user = input("pick either rock, paper or scissors: ")
user = user.lower()
print("you chosse",user,"ai chosse",AI)
if user == 'rock' or 'paper' or 'scisssor':
    print ("the computer has drawn",AI,"whilst you have drawn ",user)
if user == 'rock':
    if AI == 'Rock':
        print ('tie game')
    elif AI == 'paper':
        print ('AI Wins')
    else:
        print ('user Wins')
if user == 'paper':
    if Ai =='rock':
        print ('user Wins')
    elif AI == 'paper':
        print ('tie game')
    else:
        print ('Ai Win')
if user == 'scissor':
    if AI == 'rock':
        print ('AI Wins')
    elif AI == 'paper':
        print ('user Wins') 
else:
        print ('tie game')