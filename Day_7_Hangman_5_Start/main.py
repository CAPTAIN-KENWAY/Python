#Step 5

import random
import hangman_art as a
import hangman_words as w
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(w.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(a.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

guessed=""

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display or guess in guessed:
      print(f"You have already guessed the letter {guess}.")
      print(f"{' '.join(display)}")
      print(a.stages[lives])
      continue
    guessed+=guess
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"The letter {guess} is not in the chosen word. You lose a live.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}. Better luck next time.\n")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(a.stages[lives])