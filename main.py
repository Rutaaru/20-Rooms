"""

Program Name:
    20 Rooms

Program Description:
    "Filler."

Author:
    L. A.

Code Update Date:
    03/20/26

"""


import random

from game.play_again import play_again
from game.rps import rps
from game.rps_SD import rps_SD

from lose.entity_system import entity_system

from story.beginning import beginning
from story.death_screen import death_screen
from story.ending import ending

from win.item_system import item_system


def main():

    beginning() # Introductory print text when you first start the program
    startGame = True # Begin the actual game

    while startGame: # Loop the overall scope of the game
        health = int(100)  # Start/restart user health
        inventory = ['']  # Start/restart user inventory
        room = int(1) # Start/restart room number to "Room 1"
        gameLoop = True # Activate regular loop of the game

        if play_again.called: # Dialogue for user retrying the game
            print("\nYou wake up on the floor of one of the rooms, again. The shady forearms immediately immerge from the front of the room's darkness.\n")
            print("\"ANOTHER GO, HUH?\"\n")
            print("You get up, and walk over to it before posing your hands and arms for another match.")
            print("It follows suit.\n")
            print("\"LET'S SEE IF YOU CAN GET LUCKY ENOUGH, THIS TIME.\"\n")
            print("A bright-red '1' appears in your mind's eye, once more.\n")

        while gameLoop: # Loop the main game
            match = ''

            if 1 <= room <= 20:
                if room == 10 or room == 20: # Sudden-Death rooms
                    print("\n'SUDDEN DEATH'")
                    print("'1-OUT-OF-1 MATCH'\n")
                    print("'BE READY'\n")

                    if rps_SD():
                        match = 'won'
                    else:
                        match = 'lost'

                else:
                    if rps():
                        match = 'won'
                    else:
                        match = 'lost'

                if match == 'won':
                    if room < 20:
                        print("An item lies in front of it.")
                        item_system(inventory, health)
                        print(f"\n'{room + 1}'")
                        print(f"The door to room {room} closes behind you.")
                        print("\nYou approach the front of this room's darkness, and ready your arms and hands.")
                        room = room + int(1)
                    elif room == 20:
                        room = room + int(1)


                elif match == 'lost':
                    entity_system(inventory, health)

                    if health < 1:
                        death_screen()

                        if play_again():
                            play_again.called = True
                            gameLoop = False

                        else:
                            startGame = False

            else:
                ending()
                gameLoop = False

        startGame = False


if __name__ == "__main__":
    main()