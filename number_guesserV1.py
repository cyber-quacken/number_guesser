import random

#computer picks number
secret_number = random.randint(1, 10)
#hard_secret_number = random.randint(1, 100)

#guess counter
guess = None
attempts = 0
#level = None

#Computer talks and gets info
user = str(input("what's your name?"))
#level = str(input("Do you want it easy or hard?"))
#if level == "easy" or "Easy":
    #print(f"{user} I'm thinking of a number between 1 and 10 can you guess it?")
#else:
print(f"{user} I'm thinking of a number between 1 and 100 can you guess it?")
    
#starts the game
while guess != secret_number:

    guess = int(input("Take your best guess: "))
    attempts += 1
    
    #Hint after 5 guesses
    if attempts == 5 and guess != secret_number:
        print(f"Here is a hint {secret_number - 2} try that")
        
    #game logic
    if guess < secret_number:
        print(f"Try a little higher, {user}")
    elif guess > secret_number:
        print(f"WOAH! {user} too high")
    else:
        print(f"You nailed it {user} and it only took {attempts} tries")
           
