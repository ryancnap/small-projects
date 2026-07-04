import random

WORD_LIST = ['stallman', 'kernighan', 'ritchie', 'torvalds', 'djikstra']
word = random.choice(WORD_LIST)
word_mask = ['_' for char in word]
guess_cache = []

def show_score():
    print()
    print('_'.join(word_mask))
    print(f'<> Incorrect guesses: {incorrect_guesses} / {INCORRECT_GUESS_MAX}')
    print(f'<> Already guessed: {[i for i in guess_cache if i not in word]}')
    print()

def process_guess(guess, incorrect_guesses, guess_cache, word):
    if guess in guess_cache:
        print(f'* You already tried {guess.upper()}')

    elif guess not in word:
        incorrect_guesses += 1
        guess_cache.append(guess)
        print(f' ! {guess.upper()} does not appear in the word ! ')

    elif guess in word:
        guess_cache.append(guess)
        print(f' ! {word.count(guess)}x {guess.upper()} found in the word !')

    return incorrect_guesses

def check_won(word_mask):
    return '_' not in word_mask

def update_word_mask(guess, word, word_mask):
     for index, letter in enumerate(word):
        if letter == guess:
            word_mask[index] = guess

incorrect_guesses = 0
INCORRECT_GUESS_MAX = 6
solved = False
while not solved and incorrect_guesses < INCORRECT_GUESS_MAX:
    show_score()
    guess = input('\nSelect a letter > ').lower()
    incorrect_guesses = process_guess(guess, incorrect_guesses, guess_cache, word)

    update_word_mask(guess, word, word_mask)
    solved = check_won(word_mask)



        
    





