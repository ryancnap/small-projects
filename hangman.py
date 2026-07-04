import random

wordlist = ['stallman', 'kernighan', 'ritchie', 'torvalds', 'djikstra']
word = random.choice(wordlist)
word_mask = ['_' for char in word]
guess_cache = []

def show_score():
    print()
    print('_'.join(word_mask))
    print(f'<> Incorrect guesses: {incorrect_guesses} / {incorrect_guess_max}')
    print(f'<> Already guessed: {[i for i in guess_cache if i not in word]}')
    print()

def process_guess(guess, incorrect_guesses):
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

def check_won():
    return '_' not in word_mask

def update_word_mask(guess):
     for index, letter in enumerate(word):
        if letter == guess:
            word_mask[index] = guess

incorrect_guesses = 0
incorrect_guess_max = 6
solved = False
while not solved and incorrect_guesses < incorrect_guess_max:
    show_score()
    guess = input('\nSelect a letter > ').lower()
    incorrect_guesses = process_guess(guess, incorrect_guesses)

    update_word_mask(guess)
    solved = check_won()



        
    





