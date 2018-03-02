from random import randint
from time import sleep
from operator import itemgetter
import pickle
import sys

rock = 1
paper = 2
scissors = 3

lBoard = open('top10.txt', 'w')
lBoard.write("___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n___________    0\n")
lBoard.close()
lBoard = open('top10.txt', 'r')
lBoard.seek(0)
sBoard = lBoard.read()
#print(sBoard)

lBoard.close()


global ps
global cs
global rnd
ps = 0
cs = 0
rnd = 0
nQ = input("What is your name? ")
hSQ = input("Would you like to see the scoreboard? Y/N? ")
GS = input("Would you like to play a game Y/N? ")

if hSQ == "Y" or hSQ == "y":
    print(sBoard)
else:
    print("Ok")


def gStart():
    global ps
    global cs
    global rnd
    rnd = rnd + 1
    print("Round",rnd)
    player = int(input("Rock(1), Paper(2), Scissors(3)"))
    cpu = randint(1,3)
    
    if player == 1:
        print ("You chose Rock")
    elif player == 2:
        print ("You chose Paper")
    elif player == 3:
        print ("You chose scissors")
    else:
        print ("Invalid input. Please choose Rock[1], Paper[2], or Scissors[3]")


    if cpu == 1:
        sleep(1)
        print ("AI chose Rock")
    elif cpu == 2:
        sleep(1)
        print ("AI chose Paper")
    else:
        sleep(1)
        print ("AI chose Scissors")


    if player == 1 and cpu == 1:
        sleep(1)
        print ("Rock vs. Rock. Tie!")
    elif player == 1 and cpu == 2:
        sleep(1)
        print ("Rock vs. Paper. You Lose!")
        cs = cs + 1
    elif player == 1 and cpu == 3:
        sleep(1)
        print ("Rock vs. Scissors. You Win!")
        ps = ps + 1
    elif player == 2 and cpu == 1:
        sleep(1)
        print ("Paper vs. Rock. You Win!")
        ps = ps + 1
    elif player == 2 and cpu == 2:
        sleep(1)
        print ("Paper vs. Paper. Tie!")
    elif player == 2 and cpu == 3:
        sleep(1)
        print ("Paper vs. Scissors. You Lose!")
        cs = cs + 1
    elif player == 3 and cpu == 1:
        sleep(1)
        print ("Scissors vs. Rock. You Lose!")
        cs = cs + 1
    elif player == 3 and cpu == 2:
        sleep(1)
        print ("Scissors vs. Paper. You Win!")
        ps = ps + 1
    elif player == 3 and cpu == 3:
        sleep(1)
        print ("Scissors vs. Scissors. Tie!")
    else:
        print ("Invalid")
        
    print("Computer score: ",cs, "  Player score: ",ps)
    sleep(1)

def sGQuestion() :
    SG = input('Would you like to play again? Y/N ')
    if SG == "Y" or SG == "y":
        gStart() ## Starts the game!
    elif SG == "N" or SG == "n":
        print ("Then why are you here for? Get Out!")
        sys.exit(0)
    else:
        print ("Invalid Answer")


if GS == "Y" or GS == "y":
    gStart() ## Starts the game!
elif GS == "N" or GS == "n":
    print ("Then why are you here for? Get Out!")
    sys.exit(0)
else:
    print ("Invalid Answer")



while cs >= 0 or ps >= 0:
    if cs >= 5:
        ps = 0
        cs = 0
        sGQuestion()
    if ps >= 5:
        ps = 0
        cs = 0
        sGQuestion()
    gStart()




