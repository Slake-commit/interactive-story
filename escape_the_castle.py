import random

def next_part():
    print("================================================================================")


def wrong_answer():
    print("You hesitate")
    raise SystemExit("==GAME OVER== You hesitate too long and the guards notice you, ending your escape attempt.")


def door_choice():
    global hasKey, escaped
    print("You approach the door and try to open it, but it is locked.")
    if hasKey == True:
        print("You use the key you found to unlock the door and escape the cell!")
        escaped = True
    else:
        print("You don't have a key, so you can't open the door.")


def bed_choice():
    print("You check under the bed and find a small note.")
    print("The note reads: 'If you are reading this, you are not alone.")
    print("'I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
    if hasKey == True:
        print("You are glad you listened to your instincts and took the key")
    else:
        print("You realise you should have taken the key and gold and are glad to have found the note")


def window_choice():
    print("You look out the window and see a beautiful garden outside.")
    print("You also notice that the window is covered in iron bars, so you can't escape that way.")


def rock_choice():
    global hasKey, startingGold, goldTaken
    if hasKey == True and goldTaken == True:
        print("You check behind the rock again but there is nothing left.")
    else:
        print("You check behind the rock and find the small key and some gold again.")
        if goldTaken == False:
            startingGold += 50
            goldTaken = True
        hasKey = True
        print("You take the key and gold and feel a little more confident in your escape attempt.")


print("====ESCAPE THE CASTLE====")
print("Welcome, Adventurer! You have been captured and are being held in the dungeons of a castle.")
print("You must navigate your way through, find items, and avoid being detected by the guards")
print("But first")
print("Who are you?")

#Get player name, age and character class
print("===CREATE YOUR CHARACTER===")
playerName = input("What is your character's name?")
playerClass = input("What is your characters class?")
playerWeapon = input("What is your favourite weapon?")
playerAge = input("What is your character's age?")
startingGold = input("How much gold do you have?")
startingGold = int(startingGold)

#Set starting values
startingHealth = 100
inventory = []
hasKey = False
goldTaken = False

next_part()

#Display the character profile
print(f"Your character's name is {playerName},")
print(f"Your character is a {playerClass},")
print(f"Your character wields a {playerWeapon},")
print(f"Your character is {playerAge} years old.")
print(f"Your startingGold is {startingGold}.")
print(f"Welcome to the adventure, {playerName}!")

next_part()

#Begin the game
print(f"\n==={playerName}===, you awaken in a damp cell and you don't quite remember how you got here.")
print("Outside, you hear the sounds of guards patrolling the dungeons.")
print("Their voices bounce off the stone walls as water drips from the ceiling")
print("You check your pockets to find that all your gold has been taken but as you look around your cell")
startingGold = 0
print("You notice a small key hidden under a loose stone in the wall, the person who was here before you must have left it")
print("The mystery previous occupant of the cell appears to have left 50 gold behind as well.")
print("You shudder to think what could have happened")

next_part()

#Waking up in the cell
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
    raise SystemExit("==GAME OVER==The guards catch you before you can escape the cell.")


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
print("You look around the cell and also spot a door, a window, and an old bed.")

escaped = False

# Keep asking until the player escapes through the door
while escaped == False:
    choice = input("Do you want to investigate the door, window, bed or rock?: (door/window/bed/rock) ").lower()
    if choice == "door":
        door_choice()
    elif choice == "bed":
        bed_choice()
    elif choice == "window":
        window_choice()
    elif choice == "rock":
        rock_choice()
    else:
        wrong_answer()

next_part()

# ACT 2: Moving onto the corridor
print("You enter a long, dark corridor")
print("You notice an old wooden cabinet")

choice = input("Do you open the cabinet? (yes/no): ").lower()

if choice == "yes":
    print("You open the cabinet")
    print(f"Inside, you find a {playerWeapon}!")
    inventory.append(f"{playerWeapon}")
    print(f"You pick up the {playerWeapon}")

elif choice == "no":
    print("You leave the cabinet closed.")

print(f"\n Your Inventory: {inventory}")

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
        print("You fearlessly launch yourself at the dragon and engage the it in battle!")
    elif action == "sneak":
        print("You carefully sneak past the dragon. Flinching with each snore as you tip toe")
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
print(f"{playerName}, as you move forward on your quest, you hear what sounds like an enemy around the corner")
print("You gather yourself, ready to take on whatever comes your way")
