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

 
 #Begin the
print(f"\n==={playerName}===, you awaken in a damp cell and you don't quite remember how you got here.")
print("Outside, you hear the sounds of guards patrolling the dungeons.")
print("Their voices bounce off the stone walls as water drips from the ceiling")
print("You check your pockets to find that all your gold has been taken but as you look around your cell")
print("You notice a small key hidden under a loose stone in the wall, the person who was here before you must have left it")
print("The mystery previous occupant of the cell appears to have left 50 gold behind as well.")
print("You shudder to think what could have happened")
print(f"Character Profile:\nName: {playerName}\nAge: {playerAge}\nClass: {playerClass}\nFavourite Weapon: {playerWeapon}\nGold: {startingGold}")


#Exploring the dungeon cell
print("--- YOU BEGIN YOUR JOURNEY ---")
print(f"\n{playerName}, you look at the key and gold left behind the rock and consider things for a moment")
input("Do you take the key and gold left behind? (yes/no)").lower()

if answer == "yes":
    print("You don't feel good about it but, considering your gold was taken, you decide that this is a good idea")
    hasKey = True
elif answer == "no":
    print("You think on it a moment and decide that you don't want to take the gold, but you consider the keuy again")

else:
    print("You stand there confused until the guards come back and you are caught")

    input("Do you take the key? (yes/no)").lower()
    if answer == "yes":
        print("You decide the ley may be helpful in the future and quickly pocket it")
        hasKey = True
    elif answer == "no":
        print("You decide against taking the key, but it plays a little on your mind")

        
 