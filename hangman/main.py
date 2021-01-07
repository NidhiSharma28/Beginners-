import random
import hangman_words
import hangman_art

lives = 6
stages = hangman_art.stages
print(hangman_art.logo)
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
count = len(chosen_word)
print(f"The chosen word is :{chosen_word}")
display = []
end_of_game = False
for i in chosen_word:
  display.append("_")
while end_of_game == False:
  print(display)
  guess = input("Guess the letter in the word")
    #checking if the guess is right or not 
  if guess in display:
    print("You already have guessed this letter.")
    continue
  if guess in chosen_word:
      for i in range(count):
        if guess == chosen_word[i]:
          display[i] = guess    
  else:
    lives -=1
    print(stages[lives])
  if lives == 0:
    print("Sorry!you lost,please try again.")     
    end_of_game = True
  if "_" not in display:
    print("Congratulations!! You won.")
    end_of_game = True
