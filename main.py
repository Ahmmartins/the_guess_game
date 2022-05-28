word_list = ["apple", "rice", "beans"]
import random
choose_word = random.choice(word_list)
#print(f"the chosen word is {choose_word}")



lives = 6



display = []
for letter in choose_word:
    display += "_"

print(display)

end_of_game = False

while not end_of_game:
    guess = input("guess a random letter: ").lower()

    if guess in display:
        print(f"you've already guessed {guess}")


    for position in range(len(choose_word)):
        letter = choose_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in choose_word:
        print(f"you've guess the wrong letter{guess}, you loose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you loose")

    print(f"{''.join(display)}")
    if"_" not in display:
        end_of_game = True
        print("you win")
