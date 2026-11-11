#Welcome the player
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
startingGold = int(startingGold) - 50
 
#Set starting values
startingHealth = 100
startingGold = 50
hasKey = False
 
#Display the character profile
print(f"Your character's name is {playerName},")
print(f"Your character is a {playerClass},")
print(f"Your character wields a {playerWeapon},")
print(f"Your character is {playerAge} years old.")
print(f"Your startingGold is {startingGold}.")
print(f"Welcome to the adventure, here is 50 gold to help you on your journey, {playerName}!")
print(f"has key")
print(f"Character Profile:\nName: {playerName}\nAge: {playerAge}\nClass: {playerClass}\nFavourite Weapon: {playerWeapon}\nGold: {startingGold}")

 
 #Begin the game
print(f"\n==={playerName}===, you awaken in a damp cell and you don't quite remember how you got here.")
print("Outside, you hear the sounds of guards patrolling the dungeons.")
print("Their voices bounce off the stone walls as water drips from the ceiling")
print("You check your pockets to find that all your gold has been taken but as you look around your cell")
print("You notice a small key hidden under a loose stone in the wall, the person who was here before you must have left it")
print("The mystery previous occupant of the cell appears to have left 50 gold behind as well.")
print("You shudder to think what could have happened")
print(f"Character Profile:\nName: {playerName}\nAge: {playerAge}\nClass: {playerClass}\nFavourite Weapon: {playerWeapon}\nGold: {startingGold}")


#Waking up in the cell
print("--- YOU BEGIN YOUR JOURNEY ---")
print(f"\n{playerName}, you look at the key and gold left behind the rock and consider things for a moment")
choice = input("Do you take the gold left behind? (yes/no) ").lower()

if choice == "yes":
    print("You don't feel good about it but, considering your gold was taken, you decide that this is a good idea")
    startingGold += 50
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

# Ask the player what they want to investigate
choice = input("Do you want to investigate the door, window or bed?: (door/window/bed) ").lower()
if choice == "door":
    print("You approach the door and try to open it, but it is locked.")
    if hasKey == True:
        print("You use the key you found to unlock the door and escape the cell!")
    else:
        print("You don't have a key, so you can't open the door.")
    choice = input("Do you want to investigate the window or bed?: (window/bed) ").lower()

if choice == "window":
    print("You look out the window and see a beautiful garden outside.")
    print("You also notice that the window is covered in iron bars, so you can't escape that way.")
    choice = input("Do you want to investigate the door or bed?: (door/bed) ").lower()

if choice == "bed":
    print("You check under the bed and find a small note.")
    print("The note reads: 'If you are reading this, you are not alone.")
    print("'I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
    if hasKey == True:
        print("You are glad you listened to your instincts and took the key")
    elif hasKey == False:
        print("You realise you should have taken the key and gold and are glad to have found the note")

        choice = input("Do you want to investigate the window, bed, or rock in the wall?: (window/bed/rock) ").lower()
    
    if choice == "rock":
     print("You check behind the rock and find the small key and some gold again.")
    print("You take the key and gold and feel a little more confident in your escape attempt.")
    hasKey = True
    startingGold += 50

    choice = input("Do you want to investigate the door, window, or bed?: (door/window/bed) ").lower()
    
    if choice == "door":
        print("You approach the door and try to open it, but it is locked.")
        if hasKey == True:
            print("You use the key you found to unlock the door and escape the cell!")
            print("==YOU ESCAPED YOUR CELL==")
        else:
            print("You don't have a key, so you can't open the door.")

            choice = input("Do you want to investigate the bed or window? (bed/window) ").lower()
    
    if choice == "window":
        print("You look out the window and see a beautiful garden outside.")
        print("You also notice that the window is covered in iron bars, so you can't escape that way.")

    if choice == "bed":
        print("You check under the bed and find a small note.")
    print("The note reads: 'If you are reading this, you are not alone.")
    print("I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
    if hasKey == True:
        print("You are glad you listened to your instincts and took the key")
    elif hasKey == False:
        print("You realise you should have taken the key and gold and are glad to have found the note")
        
        choice = input("Do you want to investigate the window, bed, or rock in the wall?: (window/bed/rock) ").lower()
    else:
        print("You hesitate")
        raise SystemExit("==GAME OVER== You hesitate too long and the guards notice you, ending your escape attempt.")

if choice == "rock":
    print("You check behind the rock and find the small key and some gold again.")
    print("You take the key and gold and feel a little more confident in your escape attempt.")
    hasKey = True
    startingGold += 50

    choice = input("Do you want to investigate the door, window, or bed?: (door/window/bed) ").lower()

if choice == "door":
    print("You approach the door and try to open it, but it is locked.")
    if hasKey == True:
        print("You use the key you found to unlock the door and escape the cell!")
    else:
        print("You don't have a key, so you can't open the door.")
    choice = input("Do you want to investigate the window or bed?: (window/bed) ").lower()

if choice == "window":
    print("You look out the window and see a beautiful garden outside.")
    print("You also notice that the window is covered in iron bars, so you can't escape that way.")
    choice = input("Do you want to investigate the door or bed?: (door/bed) ").lower()

if choice == "bed":
    print("You check under the bed and find a small note.")
    print("The note reads: 'If you are reading this, you are not alone.")
    print("'I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
    if hasKey == True:
        print("You are glad you listened to your instincts and took the key")
    elif hasKey == False:
        print("You realise you should have taken the key and gold and are glad to have found the note")
    choice = input("Do you want to investigate the window, bed, or rock in the wall?: (window/bed/rock) ").lower()
if choice == "rock":
        print("You check behind the rock and find the small key and some gold again.")
        print("You take the key and gold and feel a little more confident in your escape attempt.")
        hasKey = True
        startingGold += 50

        choice = input("Do you want to investigate the door, window, or bed?: (door/window/bed) ").lower()
    
if choice == "door":
        print("You approach the door and try to open it, but it is locked.")
        if hasKey == True:
            print("You use the key you found to unlock the door and escape the cell!")
            print("==YOU ESCAPED YOUR CELL==")
        else:
            print("You don't have a key, so you can't open the door.")
            choice = input("Do you want to investigate the bed or window? (bed/window) ").lower()
    
if choice == "window":
        print("You look out the window and see a beautiful garden outside.")
        print("You also notice that the window is covered in iron bars, so you can't escape that way.")

if choice == "bed":
        print("You check under the bed and find a small note.")
print("The note reads: 'If you are reading this, you are not alone.")
print("'I have left the key to the cell and some gold behind a stone in the wall. Good luck!'")
if hasKey == True:
        print("You are glad you listened to your instincts and took the key")
elif hasKey == False:
        print("You realise you should have taken the key and gold and are glad to have found the note")
        choice = input("Do you want to investigate the window, bed, or rock in the wall?: (window/bed/rock) ").lower()
else:
        print("You hesitate")
        raise SystemExit("==GAME OVER== You hesitate too long and the guards notice you, ending your escape attempt.")

if choice == "rock":
        print("You check behind the rock and find the small key and some gold again.")
        print("You take the key and gold and feel a little more confident in your escape attempt.")
        hasKey = True
        startingGold += 50

        choice = input("Do you want to investigate the door, window, or bed?: (door/window/bed) ").lower()

 # ACT 2: Moving onto the corridor
# Introduce the scene
print("You enter a long, dark corridor")
print("You notice an old wooden cabinet")
 
choice = input("Do you open the cabinet? (yes/no): ")
 
if choice == "yes":
    print("You open the cabinet")
    print("Inside, you find a {playerWeapon}!")
 
    inventory.append("{playerWeapon}")
 
    print("You pick up the {playerWeapon}")
 
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