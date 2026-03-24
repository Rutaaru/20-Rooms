"""

Inputs:
    None

Outputs:
    True or False

"""


import random

choiceWords = ['rock', 'paper', 'scissors']
score = [0, 0]
win = ''


def getDarkMove():
    ran = random.randint(0, 2)
    print("It chose " + choiceWords[ran] + ".")
    return ran

def getUserMove():
    enter = input("Rock, paper, scissors...: ")
    invalid = True
    while invalid:
        if enter == 'R' or enter == 'r' or enter == 'Rock' or enter == 'rock':
            print("\n'SHOOT'")
            print("\nYou chose rock.")
            return 0
            invalid = False
        elif enter == 'P' or enter == 'p' or enter == 'Paper' or enter == 'paper':
            print("\n'SHOOT'")
            print("\nYou chose paper.")
            return 1
            invalid = False
        elif enter == 'S' or enter == 's' or enter == 'Scissors' or enter == 'scissors':
            print("\n'SHOOT'")
            print("\nYou chose scissors.")
            return 2
            invalid = False
        else:
            enter = input("'ROCK, PAPER, OR SCISSORS, ONLY.' [Try again:] ")


def roundWinner(userRound, darkRound):
    global score
    if (userRound == 1 and darkRound == 0) or (userRound == 2 and darkRound == 1) or (userRound == 0 and darkRound == 2):
        print("\n'YOU WON'")
        score[0] = score[0] + 1
    elif (userRound == 0 and darkRound == 1) or (userRound == 1 and darkRound == 2) or (userRound == 2 and darkRound == 0):
        print("\n'I WON'")
        score[1] = score[1] + 1
    elif userRound == darkRound:
        print("\n'TIED.'")

def matchWinner(userMatch, darkMatch):
    global win
    if userMatch > darkMatch:
        print("\n'LUCKY WINNER'")
        print("\nThe shroud of darkness dissipates from the front of the room. The door is now visible.")
        win = True
    elif userMatch < darkMatch:
        print("\n'LOSER'")
        print("You feel a chill run down your spine as one of the darkness' hands points behind you. You turn around to look... You can no longer move.")
        win = False


def rps():
    global choiceWords
    global win
    global score
    win = ''
    score = [0, 0]

    while score[0] < 2 and score[1] < 2:
        userMove = getUserMove()
        darkMove = getDarkMove()
        roundWinner(userMove, darkMove)
        print(f"\nYou - {score[0]}; It - {score[1]}\n")

    if score[0] == 2 or score[1] == 2:
        matchWinner(score[0], score[1])
        return win