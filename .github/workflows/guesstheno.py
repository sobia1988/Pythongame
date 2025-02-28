import random
rand_bot = random.randint(1,100)

def GuessNo():  
 guess = 0   
 inp = None     
 while True:
        inp = int(input("Guess a number between 1 & 100: "))
        guess += 1
        if inp >rand_bot:
            print(f"Please select a no less than {inp}! Try again.")
            continue
        elif inp<rand_bot:
             print(f"Please Select a no greater than {inp}")
             continue
        elif rand_bot == inp:
         print(f"You guessed the correct no in {guess} guesses")
         break
        else:
             print("You Lose Try Again")
             continue
 with open(r"C:\Users\user\Desktop\Class python\guess.txt", "w") as file:
     file.write(str(f"attemps:{guess}"))
GuessNo()
 
