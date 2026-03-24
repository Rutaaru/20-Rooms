"""

Inputs:
    inventory (list), health (integer)

Outputs:
    inventory (list), health (integer)

"""


import random

entityList = ['Dog', 'Ceiling', 'Mouse', 'Eye', 'Snake', 'Scree', 'Hug', 'Spore', 'Mask'] # Ordered from least to greatest damage done to user
itemList = ['meat', 'umbrella', 'cheese', 'sunglasses', 'antivenom', 'earplugs', 'teddy bear', 'gas mask', 'mannequin head'] # Ordered to match each correspondingly-numbered entity in entityList

# Dog is a thing that comes in on all fours and bites your leg - 2 damage - matching item: meat
# Ceiling is the ceiling of the room, where a human face replaces it, and starts crying acid, which burns you - 5 damage - matching item: umbrella
# Mouse is a big mouse that starts gnawing at your flesh - 8 damage - matching item: cheese
# Eye is an eye that hurts to look at - 10 damage - matching item: sunglasses
# Snake is a little snake that bites you and injects you with venom - 15 damage - matching item: antivenom
# Scree is a thing that screeches, and it hurts your ears - 20 damage - matching item: earplugs
# Hug is a person you love that hugs you, which burns where they touch you - 25 damage - matching item: teddy bear
# Spore are spores that spread across the room and cause sprouts to grow from your flesh - 30 damage - matching item: gas mask
# Mask is a mask that puts itself on your face, which begins to melt your skin off - 35 damage - matching item: mannequin head

damage = int(0)
chosenEntity = ''

def will_it_hurt():
    whichSet = random.randint(1, 25)

    if whichSet == 1:
        return False
    elif whichSet != 1:
        return True

def choose_entity():
    global entityList
    global chosenEntity

    entityPick = random.randint(0, len(entityList)-1)

    chosenEntity = entityList[entityPick]

    return chosenEntity

def entity_events(inventory):
    global damage
    global itemList

    damage = int(0)

    print("\n...")


    if chosenEntity == 'Dog':
        print("\nFrom the darkness...")
        print("A thing that looks sort of like a dog runs in on all fours, growling angrily and gnashing its teeth.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'meat':
                print("\nYou think of using the meat. It is ejected from your inventory.")
                print("\nThe meat is flung forward towards the creature, which promptly begins to gnaw on it, hunger flooding its eyes.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'meat':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nThe thing bites your leg with aggression.")
                print("You have taken 2 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(2)
                return inventory
        else:
            print("\nIt bites your leg with aggression.")
            print("You have taken 2 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(2)
            return inventory


    elif chosenEntity == 'Ceiling':
        print("\n...You notice something happening to the ceiling in your peripherals. The ceiling morphs into a human face, and you can barely see the mouth begin to frown.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'umbrella':
                print("\nYou think of using the umbrella. It is ejected from your inventory.")
                print("\nThe umbrella is lifted above you, its canopy spanning across the width of your entire body. You hear crying erupt from above you, and watch as big, gross drops of liquid fall over the side of the umbrella.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'umbrella':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nYou can feel giant globs of liquid begin to rain down on you, as its crying echoes throughout the otherwise-silent room. The liquid burns on your skin.")
                print("You have taken 5 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(5)
                return inventory
        else:
            print("\nYou can feel giant globs of liquid begin to rain down on you, as its crying echoes throughout the otherwise-silent room. The liquid burns on your skin.")
            print("You have taken 5 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(5)
            return inventory


    elif chosenEntity == 'Mouse':
        print("\nFrom the darkness:")
        print("A mouse larger than one you've ever seen crawls speedily towards you, its squeaks strange.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'cheese':
                print("\nYou think of using the cheese. It is ejected from your inventory.")
                print("\nThe piece of cheese bounces across the floor towards the mouse. It flinches in surprise at first, but quickly realizes that the cheese is of no threat. It crawls to it, and nibbles happily on its new source of food.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'cheese':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nThe mouse chomps its incisors through one of your feet, and begins eating. It gnaws at your flesh for a while, and you are afraid bones may be visible through your feet.")
                print("You have taken 8 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(8)
                return inventory
        else:
            print("\nIt chomps its incisors through one of your feet, and begins eating. It gnaws at your flesh for a while, and you are afraid bones may be visible through your feet.")
            print("You have taken 8 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(8)
            return inventory


    elif chosenEntity == 'Eye':
        print("\nFrom the darkness:")
        print("A peculiar, singular eye floats in... Or, that is what you could assume from the half-second you were given, before, suddenly, you can no longer see.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'sunglasses':
                print("\nYou think of using the sunglasses. It is ejected from your inventory.")
                print("\nSwiftly, the sunglasses float up to your face facing the direction opposite of you, and is placed on the bridge of your nose. They are pushed as far back as they can go, wholly covering your eyes. Now, all you can observe in front of you is an eyeball, with its bright pupil seeming to erupt little solar flares.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'sunglasses':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nThe eye's too bright, and it burns your eyes. It feels like having looked directly at the sun for hours on end, and then some. Even with your eyes closed, the pain still persists.")
                print("You have taken 10 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(10)
                return inventory
        else:
            print("\nIt's too bright, and it burns your eyes. It feels like having looked directly at the sun for hours on end, and then some. Even with your eyes closed, the pain still persists.")
            print("You have taken 10 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(10)
            return inventory


    elif chosenEntity == 'Snake':
        print("\nFrom the darkness:")
        print("What slithers in is a tiny, little snake. It reminds you of a garter snake, but when its body gets to you, it slithers up to your leg, and sinks its fangs through the flesh.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'antivenom':
                print("\nYou think of using the antivenom syringe. It is ejected from your inventory.")
                print("\nThe needle is injected into you near the snake's bite mark on your body. Now all you can feel is the barely-painful, useless little bite of the snake.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'antivenom':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nYour brain quickly gets fuzzy, and you know you were injected with its venom. You feel so dizzy...")
                print("You have taken 15 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(15)
                return inventory
        else:
            print("\nYour brain quickly gets fuzzy, and you know you were injected with its venom. You feel so dizzy...")
            print("You have taken 15 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(15)
            return inventory


    elif chosenEntity == 'Scree':
        print("\nFrom the darkness:")
        print("Something human-like and pale walks on two legs, just barely into the visible light. The thing's mouth opens wide, then wider, then even wider. It looks like it jaw breaks.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'earplugs':
                print("\nYou think of using the earplugs. It is ejected from your inventory.")
                print("\nThe earplugs are twisted at the tips, then smushed into your ears by an unknown force. They sit comfortably within, as the creature in front of you persists. You can't hear a thing.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'earplugs':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nWhen the thing finally stops opening its freakish mouth, it calls out a loud scream that you immediately can't stand. It quickly turns into a high-pitched screech that sounds as loud as a gunshot, causing an immensely-splitting headache. You can feel wetness start dripping down from your ears.")
                print("You have taken 20 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(20)
                return inventory
        else:
            print("\nWhen it finally stops opening its freakish mouth, it calls out a loud scream that you immediately can't stand. It quickly turns into a high-pitched screech that sounds as loud as a gunshot, causing an immensely-splitting headache. You can feel wetness start dripping down from your ears.")
            print("You have taken 20 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(20)
            return inventory


    elif chosenEntity == 'Hug':
        print("\nFrom the darkness:")
        print("Someone you have loved for a long time appears. They walk in somberly with eyes that show red from sobbing, then those eyes notice you.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'teddy bear':
                print("\nYou think of using the teddy bear. It is ejected from your inventory.")
                print("\nThe person you love begins to run towards you, but stops when suddenly the teddy bear is thrown into their arms. \"A gift... F-For me...? Ohhhh...!!\" they sob, tears of joy rapidly running down their cheeks. They hug the stuffed toy like their life depends on it. \"I'll keep it and cherish it as a memory of you, even as the universe perishes...\"")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'teddy bear':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nThe person you love runs over to you whilst crying, and delivers you a firm and passionate hug when they finally arrive. \"It's been so long... I'm s-so happy to see you...\" they cry out with love. You begin feeling a horribly awful pain all over; where they embrace your body in the hug feels like you are being lit on fire.")
                print("You have taken 25 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(25)
                return inventory
        else:
            print("\nThey run over to you whilst crying, and deliver you a firm and passionate hug when they finally arrive. \"It's been so long... I'm s-so happy to see you...\" they cry out with love. You begin feeling a horribly awful pain all over; where they embrace your body in the hug feels like you are being lit on fire.")
            print("You have taken 25 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(25)
            return inventory


    elif chosenEntity == 'Spore':
        print("\nThroughout the room, you start seeing tiny little blue specks whimsically float and dance in the air. The unknown, blue substance floats to you, and you are hesitant to breathe it in, so you hold your breath.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'gas mask':
                print("\nYou think of using the gas mask. It is ejected from your inventory.")
                print("\nThe gas mask heads onto your face quickly, safening its straps snugly to your head. You can finally breathe without worry of the strange, floating particles.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'gas mask':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nEventually, you need oxygen, and take in the air once more. Your skin starts feeling prickly and tingly, and you can see and feel little sprouts rapidly start their quaint lives on your flesh. Any growing underneath clothing break through the fabric with ease. They rise bigger and bigger. Your flesh feels like an outlet for hell.")
                print("You have taken 30 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(30)
                return inventory
        else:
            print("\nEventually, you need oxygen, and take in the air once more. Your skin starts feeling prickly and tingly, and you can see and feel little sprouts rapidly start their quaint lives on your flesh. Any growing underneath clothing break through the fabric with ease. They rise bigger and bigger. Your flesh feels like an outlet for hell.")
            print("You have taken 30 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(30)
            return inventory


    elif chosenEntity == 'Mask':
        print("\nFrom the darkness...")
        print("A lone, white, smiling mask without a wearer floats through the air towards you. Once it comes close enough to you, it turns itself to face the opposite direction from you, then continues its trek to you.")
        if len(inventory) > 0:
            print("\n'THINK OF AN ITEM YOU HAVE TO WARD OFF THE ATTACK'")

            if len(inventory) == 1:
                print(f"\nYour inventory is: {inventory[0]}.")
            elif len(inventory) == 2:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}.")
            elif len(inventory) == 3:
                print(f"\nYour inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

            itemChoice = input("Which item in your inventory will you try to defend yourself with?: ").lower()

            while itemChoice not in itemList and itemChoice not in inventory:
                while itemChoice not in itemList:
                    itemChoice = input("\n'THAT ITEM DOES NOT EXIST. THINK OF SOMETHING BETTER.': ").lower()
                while itemChoice not in inventory:
                    itemChoice = input("\n'YOU DO NOT HOLD THAT ITEM. CHOOSE AN ITEM YOU ACTUALLY HAVE.': ").lower()

            if itemChoice == 'mannequin head':
                print("\nYou think of using the mannequin head. It is ejected from your inventory.")
                print("\nThe mannequin head floats in the air in front of your head, facing the direction opposite of you. As the mask floats forward, it touches the fake head and latches on to it, sparing your own face.")
                print("The entity disappears, along with your item.")
                inventory.remove(itemChoice)
                return inventory

            elif itemChoice != 'mannequin head':
                print(f"\nYou think of using the {itemChoice}, but nothing happens.")
                print("\nThe mask gets to your face, and latches itself on. Your skin starts to tingle, then burn. You can feel your skin begin to liquify. Your skin is melting off. You cry.")
                print("You have taken 35 damage.")
                print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
                damage = damage + int(35)
                return inventory
        else:
            print("\nIt gets to your face, and latches itself on. Your skin starts to tingle, then burn. You can feel your skin begin to liquify. Your skin is melting off. You cry.")
            print("You have taken 35 damage.")
            print("\nThe entity disappears, and the visual damage done to your entire being are no longer visible.")
            damage = damage + int(35)
            return inventory




def entity_system(inventory, health):
    global damage
    global chosenEntity
    damage = int(0)
    chosenEntity = ''

    if will_it_hurt() == False:
        print("\n...But nothing happens.")
        print("\nYou regain the ability to move. You turn around towards the front of the room once again.")
        return inventory, int(health)

    else:
        willReturn = random.randint(1, 100)
        if willReturn == 1:
            willReturn = True
        else:
            willReturn = False

        if willReturn == True:
            for i in range(2):
                if health > 0:
                    chosenEntity = ''

                    choose_entity()
                    inventory = entity_events(inventory)
                    health = health - damage
                    print(f"\nYour health is now at {health}/100.")
                    if i == 0:
                        if len(inventory) == 1:
                            print(f"Your inventory is: {inventory[0]}.")
                        elif len(inventory) == 2:
                            print(f"Your inventory is: {inventory[0]}, {inventory[1]}.")
                        elif len(inventory) == 3:
                            print(f"Your inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

                        print("\nYou try moving and struggle to do so. You appear to still be frozen in place.")

                    elif i == 1:
                        if len(inventory) == 1:
                            print(f"Your inventory is: {inventory[0]}.")
                        elif len(inventory) == 2:
                            print(f"Your inventory is: {inventory[0]}, {inventory[1]}.")
                        elif len(inventory) == 3:
                            print(f"Your inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

                        print("\nYou regain the ability to move. You turn around towards the front of the room once again. The very presence of the darkness still existing feels like it's mocking you.")

                elif health <= 0:
                    print("\n'SO LONG.'")

            return inventory, int(health)

        elif willReturn == False:
            choose_entity()
            inventory = entity_events(inventory)
            health = health - damage
            print(f"\nYour health is now at {health}/100.")

            if health > 0:
                if len(inventory) == 1:
                    print(f"Your inventory is: {inventory[0]}.")
                elif len(inventory) == 2:
                    print(f"Your inventory is: {inventory[0]}, {inventory[1]}.")
                elif len(inventory) == 3:
                    print(f"Your inventory is: {inventory[0]}, {inventory[1]}, {inventory[2]}.")

                print("\nYou regain the ability to move. You turn around towards the front of the room once again. The very presence of the darkness still existing feels like it's mocking you.")

            elif health <= 0:
                print("\n'SO LONG.'")

            return inventory, int(health)