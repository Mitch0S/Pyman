title = """
______                            
| ___ \                           
| |_/ /   _ _ __ ___   __ _ _ __  
|  __/ | | | '_ ` _ \ / _` | '_ \ 
| |  | |_| | | | | | | (_| | | | |
\_|   \__, |_| |_| |_|\__,_|_| |_|
       __/ |                      
      |___/    By Mitch Naake, Mitch0S                    
====================================================================                                
"""

import random

print(title)
showWord = ""
guesses = [" "]
amtWords = 0
attempts_remaining = 6
guessed_letters = []
guess = ""
allowed_values = "ABCDEFGHIJKLMNOPQRSTUBWXYZ' '"
a = " "

words = ["CAT", "DOG", "APPLE", "CAR", "TWO WORDS", "THREE LETTER WORD"]

try:
    for i in words:
        amtWords = amtWords + 1
    if amtWords < 1:
        print("Please enter words into the 'words' array.")
except Exception as e:
    print("Please enter words into the 'words' array.")
    exit()

word = random.randint(1, amtWords-1)   # Generates a random number to select a word
word = (words[word])
wordLength = len(word)
for i in word:
    if i == " ":
        wordLength = wordLength - 1

start = str("This is a {} letter word.").format(wordLength)
print(start) # I bet you're happy about this :)

for i in word:
    a = a+i+" "
for letter in word:
    if letter in guesses:
        showWord = showWord + letter
        if letter == " ":
            wordLength = wordLength-1
    else:
        showWord = showWord + "_"

while True:  # This is the actual game code.
    if attempts_remaining > 0:
        print("\n"+showWord)
        guess = input("Please enter a letter\n> ").upper()
        if len(guess) > 1:
            input('Your input was greater than one digit, please try again. [PRESS ENTER]')
            guess = ""
        showWord = ""
        if guess not in allowed_values:
            input("Please only use the Alphanumeric alphabet. [PRESS ENTER]")
        else:
            if guess in word:  # Function for writing the found letters
                showWord = ""
                guesses.append(guess)
                for letter in word:
                    if letter in guesses:
                        showWord = showWord + letter
                    else:
                        showWord = showWord + "_"
            else:
                print('Incorrect guess, '+ str(attempts_remaining - 1)+" guesses remaining.\n\n")
                attempts_remaining = attempts_remaining - 1
                showWord = ""
                guesses.append(guess)
                for letter in word:
                    if letter in guesses:
                        showWord = showWord + letter
                    else:
                        showWord = showWord + "_"

        if showWord == word:
            print("\nYou WIN!, the answer was: "+word)
            #print(guessed_letters)
            exit()
    else:
        print("You lose, the answer was "+ word.strip())
        exit()
else:
    "You found my secret message :)"
