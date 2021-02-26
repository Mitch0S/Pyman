title = """
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   By Mitch Naake   
====================================================================                                
"""


print(title)
showWord = ""
guesses = []

import random

words = {      # Put words here in the text boxes.
    1: "ONE",
    2: "TWO",
    3: "THREE",
    4: "FOUR"
}

attempts_remaining = 6
guessed_letters = []
guess = ""
allowed_values = "ABCDEFGHIJKLMNOPQRSTUBWXYZ"
a = " "

word = random.randint(1, 4)   # Generates a random number to select a word
word = (words[word])
wordLength = len(word)
start = str(wordLength * "_"+ " - {} letter word."+"\n" )
print(start.format(wordLength)) # I bet you're happy about this :)

for i in word:
    a = a+i+" "

while True:  # This is the actual game code.
    if attempts_remaining > 0:
        guess = input("Please enter a letter\n> ").upper()
        if len(guess) > 1:
            input('Your input was greater than one digit, please try again. [PRESS ENTER]')
            guess = ""
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
                print('Incorrect guess, '+ str(attempts_remaining - 1)+" guesses remaining.")
                attempts_remaining = attempts_remaining - 1
                guessed_letters.append(guess)

            if word != showWord:
                print("\n"+showWord)
        if showWord == word:
            print("\nYou WIN!, the word was: "+word)
            print(guessed_letters)
            exit()
    else:
        print("You lose, the word was "+ word.strip())
        exit()
else:
    "You found my secret message :)"
