from hangman_words import word_list
from hangman_art import logo, stages
import random

print(logo)
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6
#Testing code
#print(f'the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"\nYou've already chosen the letter '{guess}'")
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])
      print(f"There is no letter '{guess}' in the word.")
      
    print(f"\n\n{' '.join(display)}\n\n")
  
    if lives == 0:
      print(f"You lose! The word was '{chosen_word}'")
      end_of_game = True   

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

   