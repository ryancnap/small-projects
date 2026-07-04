import random

attempts = 0
number_appearances = 0
incorrect_guesses = 0
incorrect_guess_max = 6
blank_character = '_'

wordlist = ['stallman', 'kernighan', 'ritchie', 'torvalds', 'djikstra']
word = random.choice(wordlist)
word_mask = ['_' for char in word]

def check_won():
    return blank_character not in word_mask

solved = False
while not solved and incorrect_guesses < incorrect_guess_max:
    attempts += 1
    print(word_mask)
    guess = input('\nSelect a letter > ').lower()

    if guess not in word:
        incorrect_guesses += 1
        print(f'{guess} does not appear in the word.')

    if guess in word:
        print(f' * {word.count(guess)}x {guess.upper()} found in the word!')

        for index, letter in enumerate(word):
            if letter == guess:
                word_mask[index] = guess

        solved = check_won()

        
    





