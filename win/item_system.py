"""

Inputs:
    inventory (list), health (integer)

Outputs:
    inventory (list), health (integer)

"""


import random

defenseItemList = ['meat', 'umbrella', 'cheese', 'sunglasses', 'antivenom', 'earplugs', 'teddy bear', 'gas mask', 'mannequin head']
healthItemList = ['mint', 'mini elixir', 'elixir', 'potent elixir', 'medkit'] # Ordered from least to greatest health recovered

# Mint heals 10 health
# Mini Elixir heals 20 health
# Elixir heals 30 health
# Potent Elixir heals 35 health
# Medkit heals 40 health

recover = int(0)
chosenDefenseItem = ''
chosenHealthItem = ''

def defense_or_health():
    setList = ['defense', 'health']
    setNumber = random.randint(0, 1)

    whichSet = setList[setNumber]

    if whichSet == 'defense':
        return 'defense'
    elif whichSet == 'health':
        return 'health'

def defense_items(inventory):
    global defenseItemList
    global chosenDefenseItem

    defenseItemNumber = random.randint(0, len(defenseItemList)-1)

    chosenDefenseItem = defenseItemList[defenseItemNumber]

    if chosenDefenseItem == 'meat':
        print("\nThe item that appeared was a slab of meat.")
        print("Even with food presented in front of you, it's very apparent that you don't feel the need to eat.")
        print("\nYou touch the meat, and it enters your inventory.")
        inventory.append('meat')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'umbrella':
        print("\nThe item that appeared was an umbrella.")
        print("It seems as if no light is able to pass through the canopy's fabric.")
        print("\nYou touch the umbrella, and it enters your inventory.")
        inventory.append('umbrella')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'cheese':
        print("\nThe item that appeared was a wedge of cheese.")
        print("It looks perfectly fresh and free of bacteria, somehow.")
        print("\nYou touch the cheese, and it enters your inventory.")
        inventory.append('cheese')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'sunglasses':
        print("\nThe item that appeared was a pair of sunglasses.")
        print("They are not stylish in teh slightest, and the lenses look extremely tinted.")
        print("\nYou touch the sunglasses, and they enter your inventory.")
        inventory.append('sunglasses')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'antivenom':
        print("\nThe item that appeared was a syringe labelled 'ANTIVENOM'.")
        print("You are instantly unsettled by its presence.")
        print("\nYou touch the syringe, and it enters your inventory.")
        inventory.append('antivenom')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'earplugs':
        print("\nThe item that appeared was a pair of earplugs.")
        print("The tiny pieces, of what you assume is foam, present a simple, off-white color.")
        print("\nYou touch the earplugs, and they enter your inventory.")
        inventory.append('earplugs')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'teddy bear':
        print("\nThe item that appeared was a teddy bear.")
        print("The brown animal holds a heart in front of it with its arms.")
        print("\nYou touch the teddy bear, and it enters your inventory.")
        inventory.append('teddy bear')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'gas mask':
        print("\nThe item that appeared was a gas mask.")
        print("The assumed-fact that you may need to use this at some point is intimidating.")
        print("\nYou touch the gas mask, and it enters your inventory.")
        inventory.append('gas mask')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    elif chosenDefenseItem == 'mannequin head':
        print("\nThe item that appeared was the head of a mannequin.")
        print("It's white and shiny. You wonder how it could be so pristine in a place like this.")
        print("\nYou touch the mannequin head, and it enters your inventory.")
        inventory.append('mannequin head')

        if len(inventory) == 1:
            print(f"Your inventory is now: {inventory[0]}.")
        elif len(inventory) == 2:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}.")
        elif len(inventory) == 3:
            print(f"Your inventory is now: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

    return inventory

def health_items(health):
    global healthItemList
    global chosenHealthItem
    global recover

    healthItemNumber = random.randint(0, len(healthItemList)-1)

    chosenHealthItem = healthItemList[healthItemNumber]

    print("\nIt is glowing.\n")

    if chosenHealthItem == 'mint':
        print("The item that appeared was a mint.")
        print("'10'")

        print(f"\nYour health is at {health}/100.")

        recover = int(10)
        if recover > (100 - health):
            print("\n'DON'T GO THINKING YOU CAN BITE MORE THAN YOU ARE ABLE TO CHEW'")
            print(f"\nThe mint disappears right in front of you. Your health stays at {health}/100.")
        elif recover <= (100 - health):
            print("\nYou pick up the sweet-smelling mint and pop it in your mouth. It melts away on your tongue.")
            print("You feel like it took the edge off just a bit.")
            print("\nYou have recovered 10 health.")
            health = health + recover
            print(f"Your health is now at {health}/100.")

    elif chosenHealthItem == 'mini elixir':
        print("The item that appeared was a mini-elixir.")
        print("'20'")

        print(f"\nYour health is at {health}/100.")

        recover = int(20)
        if recover > (100 - health):
            print("\n'DON'T GO THINKING YOU CAN BITE MORE THAN YOU ARE ABLE TO CHEW'")
            print(f"\nThe mini-elixir disappears right in front of you. Your health stays at {health}/100.")
        elif recover <= (100 - health):
            print("\nYou pick up the elixir and pop off its cap to reveal a light-green liquid inside. You drink it.")
            print("You feel a little better.")
            print("\nYou have recovered 20 health.")
            health = health + recover
            print(f"Your health is now at {health}/100.")

    elif chosenHealthItem == 'elixir':
        print("The item that appeared was an elixir.")
        print("'30'")

        print(f"\nYour health is at {health}/100.")

        recover = int(30)
        if recover > (100 - health):
            print("\n'DON'T GO THINKING YOU CAN BITE MORE THAN YOU ARE ABLE TO CHEW'")
            print(f"\nThe elixir disappears right in front of you. Your health stays at {health}/100.")
        elif recover <= (100 - health):
            print("\nYou pick up the elixir and pop off its cap to reveal cerulean, sparkling liquid inside. You drink it, feeling it fizz gently on your tongue and down your throat.")
            print("You feel refreshed.")
            print("\nYou have recovered 30 health.")
            health = health + recover
            print(f"Your health is now at {health}/100.")

    elif chosenHealthItem == 'potent elixir':
        print("The item that appeared was a potent elixir.")
        print("'35'")

        print(f"\nYour health is at {health}/100.")

        recover = int(35)
        if recover > (100 - health):
            print("\n'DON'T GO THINKING YOU CAN BITE MORE THAN YOU ARE ABLE TO CHEW'")
            print(f"\nThe potent elixir disappears right in front of you. Your health stays at {health}/100.")
        elif recover <= (100 - health):
            print("\nYou pick up the potent elixir and pop off its cap to reveal pink, sparkling liquid inside. You drink it, feeling it fizz relentlessly on your tongue and down your throat.")
            print("You feel very refreshed.")
            print("\nYou have recovered 35 health.")
            health = health + recover
            print(f"Your health is now at {health}/100.")

    elif chosenHealthItem == 'medkit':
        print("The item that appeared was a medkit.")
        print("'40'")

        print(f"\nYour health is at {health}/100.")

        recover = int(40)
        if recover > (100 - health):
            print("\n'DON'T GO THINKING YOU CAN BITE MORE THAN YOU ARE ABLE TO CHEW'")
            print(f"\nThe medkit disappears right in front of you. Your health stays at {health}/100.")
        elif recover <= (100 - health):
            print("\nYou pick up the medkit and open it. It's full of supplies to aid your spiritual wounds. You use what you can.")
            print("You feel like you can finally relax.")
            print("\nYou have recovered 40 health.")
            health = health + recover
            print(f"Your health is now at {health}/100.")

    return int(health)


def item_system(inventory, health):
    global recover
    global chosenDefenseItem
    global chosenHealthItem
    recover = int(0)
    chosenDefenseItem = ''
    chosenHealthItem = ''

    print("\nApproaching the door to the next room, you observe the item in front of it...")

    if defense_or_health() == 'defense':
        if len(inventory) == 3:
            print("\n'THE GUILT OF GREEDY POCKETS ISN'T NECESSARY'")
            print("\nYour inventory is full, so the item disappears.")
        else:
            inventory = defense_items(inventory)

    else:
        health = health_items(health)

    print("\nYou place your hand on the knob of the door, and enter the next room.")

    return inventory, int(health)

item_system(['teddy bear', 'gas mask'], 70)