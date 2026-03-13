"""

Name: 20 Rooms

Description:

Author: L.A.

Update Date: 03/12/26

"""

import random

from story.beginning import beginning

from game.rps import rps

def main():

    health = int(100)
    inventory = ['', '', '']
    room = int(0)


    beginning()

    gameLoop = True
    while gameLoop:
        match = ''
        if room >= 1 and room <= 20:
            if room == 10 or room == 20:
                rpsSD()
                if rpsSD() == True:
                    match = 'won'
                elif rpsSD() == False:
                    match = 'lost'
            else:
                rps()
                if rps() == True:
                    match = 'won'
                elif rps() == False:
                    match = 'lost'

            if match == 'won':
                item
            elif match == 'lost':
                entity

        else:
            game_loop = False


if __name__ == "__main__":
    main()