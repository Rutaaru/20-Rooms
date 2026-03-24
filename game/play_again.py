"""

Inputs:
    None

Outputs:
    True or False

"""


def play_again():
    resetChoice = input("\n(Would you like to reset from the beginning and try the game again? [y/n]:) ").lower()

    while resetChoice != 'y' and resetChoice != 'yes' and resetChoice != 'n' and resetChoice != 'no':
        print("\n(Bad input.)")
        resetChoice = input("(To play the game again, try entering 'y'/'yes'/'Y'/'Yes'/'YES'. To end the game, try entering 'n'/'no'/'N'/'No'/'NO':) ").lower()

    if resetChoice == 'y' or resetChoice == 'yes':
        print("\n(You persist. You wish to be trapped no longer.)")
        print("\n(A shining light can be seen in your mind, warming your physiology awake.)")
        print("(You begin to feel a resurgence within yourself...)")
        return True

    elif resetChoice == 'n' or resetChoice == 'no':
        print("\n(You have given up.)")
        print("\n(Your body remains lifeless.)")
        print("(Your spirit amounts to nothing.)")
        print("\n\n[GAME OVER]")
        return False