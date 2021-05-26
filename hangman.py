import random
import os #clear screen
from art import logo,stages
print(logo)
# creating word_list
with open("words.txt") as f:
    word_list = f.read().splitlines()

chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
end_of_game = False
lives = 6
# print(f'Pssst, the solution is {chosen_word}.')
for _ in range(word_length):
        display += "_"
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("cls") # clear screen
    if guess in display:
        print(f"You've already guess the letter {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in word.You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou Lose :(")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win")
    # from art import stages
    print(stages[lives])