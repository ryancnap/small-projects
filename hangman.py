import random


WORD_LIST = ['stallman', 'kernighan', 'ritchie', 'torvalds', 'djikstra']
INCORRECT_GUESS_MAX = 6


def show_score(word, word_mask, incorrect_guesses, cache):
    print()
    print('_'.join(word_mask))
    print(f'<> Incorrect guesses: {incorrect_guesses} / {INCORRECT_GUESS_MAX}')
    print(f'<> Already guessed: {[i for i in cache if i not in word]}')
    print()

def process_guess(guess, incorrect_guesses, cache, word):
    if guess in cache:
        print(f'* You already tried {guess.upper()}')

    elif guess not in word:
        incorrect_guesses += 1
        cache.append(guess)
        print(f'! {guess.upper()} does not appear in the word ! ')

    else:
        cache.append(guess)
        print(f'! {word.count(guess)}x {guess.upper()} found in the word !')

    return incorrect_guesses

def update_word_mask(word, guess, word_mask):
     for index, letter in enumerate(word):
        if letter == guess:
            word_mask[index] = guess

def check_won(word_mask):
    return '_' not in word_mask

def winning_stats(word, incorrect_guesses):
    print('#'*50)
    print(f'# Your word was {word}.')
    print(f'# You guessed incorrectly {incorrect_guesses} times.')
    print('#'*50)

def play():
    word = random.choice(WORD_LIST)
    word_mask = ['_' for _ in word]
    incorrect_guesses = 0
    cache = []
    solved = False

    while not solved and incorrect_guesses < INCORRECT_GUESS_MAX:
        show_score(word, word_mask, incorrect_guesses, cache)
        guess = input('\nSelect a letter > ').strip().lower()

        incorrect_guesses = process_guess(guess, incorrect_guesses, cache, word)
        update_word_mask(word, guess, word_mask)
        solved = check_won(word_mask)
        if solved or incorrect_guesses == INCORRECT_GUESS_MAX: winning_stats(word, incorrect_guesses) 

play()


        
    





