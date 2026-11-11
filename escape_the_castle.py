#Welcome the player
print("====ESCAPE THE CASTLE====")
print("Welcome, Adventurer! You have been captured and are being held in the dungeons of a castle.")
print("You must navigate your way through, find items, and avoid being detected by the guards")
print("But first") 
print("Who are you?")
 
#Get player name, age and character class
print("CREATE YOUR CHARACTER")
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

 
 
#Begin the story
print(f"\n==={playerName}===, you awaken in a damp cell and you don't quite remember how you got here.")
print("Outside, you hear the sounds of guards patrolling the dungeons.")
print("Their voices bounce off the stone walls as water drips from the ceiling")
print("You check your pockets to find that all your gold has been taken but as you look around your cell")
print("You notice a small key hidden under a loose stone in the wall, the person who was here before you must have left it")
print("The mystery previous occupant of the cell appear to have left 50 gold behind as well.")
print("you shudder to think what could have happened")
