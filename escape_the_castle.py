import random
#Global calls
playerName = ""
playerClass = ""
playerWeapon = ""
playerAge = ""
startingGold = 0
startingHealth = 100
inventory = []
hasKey = False
goldTaken = False
escaped = False


#Functions for when it gets too messy
def next_part():
    print("================================================================================")


def wrong_answer():
    print("Sorry, you must have typed that wrong")


def wrong_answer2():
    print("You hesitate too long, a guard finds you and brings you back to your cell")
    cell_escape()


#Cell choices
def cell_door_choice():
    global hasKey, escaped
    print("You approach the door and try to open it, but it is locked.")
    if hasKey:
        print("You use the key you found to unlock the door and escape the cell!")
        escaped = True
    else:
        print("You don't have a key, so you can't open the door.")


def bed_choice():
    print("You check under the bed and find a small note.")
    print("The note reads: 'If you are reading this, you are not alone.")
    print("I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
    if hasKey:
        print("You are glad you listened to your instincts and took the key")
    else:
        print("You realise you should have taken the key and gold and are glad to have found the note")


def window_choice():
    print("You look out the window and see a beautiful garden outside.")
    print("You also notice that the window is covered in iron bars, so you can't escape that way.")


def rock_choice():
    global hasKey, startingGold, goldTaken
    if hasKey and goldTaken:
        print("You check behind the rock again but there is nothing left.")
    else:
        print("You check behind the rock and find the small key and some gold again.")
        if not goldTaken:
            startingGold += 50
            goldTaken = True
        hasKey = True
        print("You take the key and gold and feel a little more confident in your escape attempt.")


#Let us begin our quest
def intro():
    print("====ESCAPE THE CASTLE====")
    print("Welcome, Adventurer! You have been captured and are being held in the dungeons of a castle.")
    print("You must navigate your way through, find items, and avoid being detected by the guards")
    print("But first")
    print("Who are you?")


def create_character():
    global playerName, playerClass, playerWeapon, playerAge, startingGold

    print("===CREATE YOUR CHARACTER===")
    playerName = input("What is your character's name? ")
    playerClass = input("What is your character's class? ")
    playerWeapon = input("What is your favourite weapon? ")
    playerAge = input("What is your character's age? ")
    startingGold = int(input("How much gold do you have? "))
    next_part()

    #Display the character profile
    print(f"Your character's name is {playerName},")
    print(f"Your character is a {playerClass},")
    print(f"Your character wields a {playerWeapon},")
    print(f"Your character is {playerAge} years old.")
    print(f"Your starting gold is {startingGold}.")
    print(f"Welcome to the adventure, {playerName}!")
    next_part()


def beginning():
    global startingGold
    print(f"\n==={playerName}===, you awaken in a damp cell and you don't quite remember how you got here.")
    print("Outside, you hear the sounds of guards patrolling the dungeons.")
    print("Their voices bounce off the stone walls as water drips from the ceiling")
    print("You check your pockets to find that all your gold has been taken but as you look around your cell")
    startingGold = 0
    print("You notice a small key hidden under a loose stone in the wall, the person who was here before you must have left it")
    print("The mysterious previous occupant of the cell appears to have left 50 gold behind as well.")
    print("You shudder to think what could have happened")
    next_part()


def loose_rock():
    global startingGold, goldTaken, hasKey

    print("--- YOU BEGIN YOUR JOURNEY ---")
    print(f"\n{playerName}, you look at the key and gold left behind the rock and consider things for a moment")
    choice = input("Do you take the gold left behind? (yes/no) ").lower()

    if choice == "yes":
        print("You don't feel good about it but, considering your gold was taken, you decide that this is a good idea")
        startingGold += 50
        goldTaken = True
    elif choice == "no":
        print("You think on it a moment and decide that you don't want to take the gold, but you consider the key again")
    else:
        print("You stand there confused until the guards come back and you are caught")
        raise SystemExit("==GAME OVER== The guards catch you before you can escape the cell.")

    choice = input("Do you take the key? (yes/no) ").lower()
    if choice == "yes":
        print("You decide the key may be helpful in the future and quickly pocket it")
        hasKey = True
    elif choice == "no":
        print("You decide against taking the key, but it plays a little on your mind")
        hasKey = False
    else:
        print("You hesitate")
        raise SystemExit("==GAME OVER== You hesitate too long and the guards notice you, ending your escape attempt.")


# ACT 1: Escaping the cell
def cell_escape():
    global escaped
    print("You look around the cell and also spot a door, a window, and an old bed.")

    escaped = False
    while not escaped:
        choice = input("Do you want to investigate the door, window, bed or rock? (door/window/bed/rock) ").lower()
        if choice == "door":
            cell_door_choice()
        elif choice == "bed":
            bed_choice()
        elif choice == "window":
            window_choice()
        elif choice == "rock":
            rock_choice()
        else:
            wrong_answer()


# ACT 2: Moving onto the corridor
def corridor():
    print("You enter a long, dark corridor")
    print("You notice an old wooden cabinet")

    choice = input("Do you open the cabinet? (yes/no): ").lower()

    if choice == "yes":
        print("You open the cabinet")
        print(f"Inside, you find a {playerWeapon}!")
        inventory.append(playerWeapon)
        print(f"You pick up the {playerWeapon}")
    elif choice == "no":
        print("You leave the cabinet closed.")

    print(f"\nYour Inventory: {inventory}")
    corridor_doors()


def corridor_doors():
    print("You continue down the corridor and notice three doors, each painted a different color: red, blue, and green.")
    door = input("Which door do you open? ").lower()

    if door == "red":
        print("You enter a room full of treasure!")
        action = input("Do you take the treasure or leave it? (take/leave) ").lower()
        if action == "take":
            print("You fill your bag with gold. You feel rich, but a little guilty.")
        elif action == "leave":
            print("You walk away. A wise choice... or was it?")
        else:
            print("You stand there confused until the treasure room fades away.")
    elif door == "blue":
        print("You enter a room with a sleeping dragon.")
        print("Do you stay to fight the dragon or do you try to sneak past it? (fight/sneak)")
        action = input("What do you do? ").lower()
        if action == "fight":
            print("You fearlessly launch yourself at the dragon and engage it in battle!")
        elif action == "sneak":
            print("You carefully sneak past the dragon. Flinching with each snore as you tiptoe")
        else:
            print("You stand there confused until the dragon wakes up.")
            print("The dragon looks at you and pauses, it seems strangely friendly.")
            print("After an awkward amount of time spent sussing one another out, the dragon goes back to sleep")
    elif door == "green":
        print("You discover a secret garden.")
        print("Do you explore the garden or have a restful nap among the beautiful flowers? (explore/nap)")
        action = input("What do you do? ").lower()
        if action == "explore":
            print("You wander through the garden, admiring the beautiful flowers.")
        elif action == "nap":
            print("You find a comfortable spot and take a peaceful nap, and awaken feeling incredibly refreshed.")
        else:
            print("You stand there admiring the beauty of the garden.")
    else:
        print("That door doesn't exist.")
next_part()

#Enemy encounter
def enemy_encounter():
    print(f"{playerName}, as you move forward on your quest, you hear what sounds like an enemy around the corner")
    print("You gather yourself, ready to take on whatever comes your way")

    enemies = ["Dark knight", "Sphinx", "Creeping void"]
    enemy = random.choice(enemies)
    print(f"The enemy is a {enemy}.")

    if enemy == "Dark knight":
        print("A Dark knight spots you and rushes to draw his comedically oversized sword of darkness")
        action = input("What do you do? (flee/wait/attack) ").lower()
        if action == "flee":
            print("You run back the way you came and return to the corridor")
            corridor_doors()
        elif action == "wait":
            print("You wait, hoping this has all been a huge misunderstanding. The Dark knight chops your head off.")
            raise SystemExit("==GAME OVER== You don't have a head anymore (well, you do. It's just on the floor)")
        elif action == "attack":
            print(f"You draw your {playerWeapon} and brace yourself for battle.")
            print("Right before you both clash violently in battle, you notice some stairs to your left and stick your leg out")
            print("Blind with wrath the Dark knight fails to see your leg and he trips over it, crashing down the stairs")

    elif enemy == "Sphinx":
        print("A Sphinx spots you and whips her tail in annoyance, pauses, then smirks eerily")
        print("She says 'What is your name adventurer?'")
        print(f"You answer her, a little uncertain if this is a good idea or not 'My name is {playerName}.'")
        print(f"'Well, {playerName}, you can pass unscathed as long as you answer one of my riddles. Deal?'")
        action = input("Do you guess the Sphinx's riddle or draw your weapon for battle? (attack/guess) ").lower()
        if action == "attack":
            print(f"You draw your {playerWeapon} as a maniacal grin spreads across the Sphinx's entire face")
            print("Before you even have a chance to move forward, the Sphinx crushes you with her left paw")
            raise SystemExit("==GAME OVER== You have been pancaked")
        elif action == "guess":
            print(f"A wise choice, {playerName}. Here is my riddle")
            print("Mutate and grow")
            print("I hide")
            print("Disguised")
            print("I pretend to be you")
            print("I'm not")
            print("I lie")
            print("I steal from you")
            print("I drain your health")
            print("If you attack me")
            print("You attack yourself")
            guess = input("What am I? ").lower().strip()

            if guess == "cancer":
                print("'WHAT!' The Sphinx looks clearly annoyed with you guessing her riddle correctly. She tuts to herself")
                print(f"Well played, {playerName}, I guess you can leave. Quickly, before I change my mind")
            else:
                print("The Sphinx smiles. 'Wrong.'")
                raise SystemExit("==GAME OVER== The Sphinx does not take kindly to wrong answers")

    elif enemy == "Creeping void":
        print("The darkest shadow you have ever seen starts to creep towards you")
        print("A void so thick you simply cannot believe this is happening.")
        print("What do you do?")
        print("Where do you go?")
        print("............")
        action = input("How do you even fight it? (attack/surrender) ").lower()
        if action == "attack":
            print(f"You draw your {playerWeapon} and prepare to fight the Void creeping towards you")
            print("As you slash back and forth hoping to at least do something, you sense something before you feel yourself dying")
            print("The void wasn't an enemy, and the fact you have attacked it has angered it immensely")
            print("You have no idea how, as all you saw was total darkness, but the void transports you back to your cell")
            cell_escape()
        elif action == "surrender":
            print("You surrender to the oncoming darkness, accepting your fate with no fear")
            print("As the darkness envelops you, you feel a somewhat familiar warmth")
            print("Multiple voices that sound like they come from hundreds of different people whisper to you in the dark")
            print(f"In a messy and chaotic cacophony they chant 'password, password' "
                  f"'{playerName} needs the password' and they giggle")
            print("You wonder how they know your name")
            print("All of a sudden they unify into one terrifying whisper of a thousand voices")
            print(f"{playerName}, the password is 'TRIFLE TOWER'")


#Run the game
def main():
    intro()
    create_character()
    beginning()
    loose_rock()
    cell_escape()
    corridor()
    enemy_encounter()
    print("\n==TO BE CONTINUED==")


main()
