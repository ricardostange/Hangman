# This is a game of hangman.
# First the computer will pick a random word from a list of words.

import random
import PySimpleGUI
import requests

# list of words
url_words = 'https://raw.githubusercontent.com/powerlanguage/word-lists/master/1000-most-common-words.txt'
words = requests.get(url_words).text.split()

# choose a random word from the list
word = random.choice(words)

# create an empty list of the same length as the word
guesses = ['_'] * len(word)

fails = 0
letters_guessed = []
max_fails = 6

# create a window
layout = [
    [PySimpleGUI.Text('Guess the word:')],
    [PySimpleGUI.Text(' '.join(guesses),  key='guess')],
    [PySimpleGUI.Text('Wrong letters:')],
    [PySimpleGUI.Text(' '.join(letters_guessed), key='letters')],
]

window = PySimpleGUI.Window('Hangman', layout, return_keyboard_events=True)


def reset():
    global word, guesses, fails, letters_guessed
    word = random.choice(words)
    guesses = ['_'] * len(word)
    fails = 0
    letters_guessed = []
    window['guess'].update(' '.join(guesses))
    window['letters'].update(' '.join(letters_guessed))


# uses keyboard module to listen for key presses
while True:
    event, values = window.read()
    print(event, values)
    if event == PySimpleGUI.WIN_CLOSED:
        break
    if event in letters_guessed:
        continue
    if event in word:
        for i, letter in enumerate(word):
            if letter == event:
                guesses[i] = letter
        window['guess'].update(' '.join(guesses))
        if '_' not in guesses:
            PySimpleGUI.popup('You win!', ' '.join(guesses))
            reset()
    else:
        fails += 1
        letters_guessed.append(event)
        window['letters'].update(' '.join(letters_guessed))
    if fails == max_fails:
        PySimpleGUI.popup('You lose, the word was:', word, ' '.join(guesses))
        reset()
    


