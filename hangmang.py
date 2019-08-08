import os
import time
import random
import laserprinter
from clear_screen import clear


laser = laserprinter.Laser()

re_op = ' > ' # Redirection Operator

chances = 6

failed_attempts = 0

attempts = 0

guesses = 0

guessed = ''

correct = 0

wrong = 0


def get_word():

    words = ['titties']

    return random.choice(words)

def statistics():
    laser.center('------- Statistics -------')
    laser.gap(1)
    laser.center('Guesses: {} ({})'.format(guessed, guesses))
    laser.center('Correct: {}'.format(correct))
    laser.center('Wrong: {}'.format(wrong))
    laser.center('Chances Remaining: {}'.format(chances))
    laser.center('Failed Attempts: {}'.format(failed_attempts))
    laser.center('Total Attempts: {}'.format(attempts))
    laser.gap(1)
    laser.center('--------------------------')

def word_display():
    display = ''
    for place in place_holder:
        display = display + ' ' + place
    laser.center(display)

def panel():
    laser.gap(1)
    laser.center('------------------------------------------')
    laser.center('Guesses: {} ({}) - Correct: {} - Wrong: {}'.format(guessed, guesses, correct, wrong))
    laser.center('------------------------------------------')
    laser.gap(1)

menu = True

while menu:
    clear()
    laser.center('------- Hangmang Menu -------')
    laser.gap(1)
    laser.center('Start')
    laser.gap(1)
    laser.center('Exit')
    laser.gap(1)
    laser.center('-----------------------------')
    
    laser.gap(2)
    
    option = laser.get('Select an option from the menu above')

    if option == 'start':
        clear()
        laser.center('Starting game...')
        time.sleep(1)

        letter = ''

        word = get_word()

        letters = list(word)

        letter_count = len(letters)

        count_check = 0

        place_holder = []

        for letter in letters:
            place_holder.append('_')

        clear()

        laser.gap(2)

        laser.center('Guess')

        word_display()

        laser.gap(1)

        choosing = True

        while choosing:

            guesses += 1

            letter_check = True

            while letter_check:
                attempts += 1
                letter = laser.get('Choose a letter between A ~ Z')

                if len(letter) < 1 or len(letter) > 1:
                    failed_attempts += 1
                    if len(letter) < 1:
                        laser.center('You did not pick a letter!')
                    if len(letter) > 1:
                        laser.center('You picked too many characters!')
                elif letter.isdigit() == True:
                    failed_attempts += 1
                    laser.center('You cannot pick numbers!')
                elif letter.isalpha() == False:
                    failed_attempts += 1
                    laser.center('You cannot pick special characters!')
                elif letter in guessed:
                    failed_attempts += 1
                    laser.center('You already picked the letter {} - Guesses: {}'.format(letter, guessed))

                else:
                    letter_check = False

            guessed = guessed + letter
            if letter in letters:
                correct += 1
                clear()
                laser.center('Correct!')
                laser.center('--------')
                laser.gap(1)
                laser.center('You have {} letters remaining'.format(len(letters)))
                laser.gap(1)
                

                x = letters.count(letter)
                while (x):
                    count_check += 1
                    y = letters.index(letter)
                    place_holder.pop(y)
                    place_holder.insert(y, letter)
                    letters.pop(y)
                    letters.insert(y, '')
                    x = letters.count(letter)

                if count_check == letter_count:
                    clear()
                    laser.center('You won!')
                    laser.center('--------')
                    laser.gap(2)
                    statistics()
                    laser.gap(1)
                    choosing = False
                    laser.get('Press the [ENTER] key to continue...')

            else:
                wrong += 1
                chances -= 1
                clear()
                laser.center('Wrong!')
                laser.center('------')
                laser.gap(1)
                laser.center('You have {} chances left!'.format(chances))
                laser.gap(1)

                if (chances == 0):
                    laser.center('You lost!')
                    laser.center('---------')
                    laser.gap(2)
                    statistics()
                    laser.gap(1)
                    choosing = False
                    laser.get('Press the [ENTER] key to continue...')
                else:
                    pass
            
            word_display()
            panel()
            

    elif option == 'exit':
        clear()
        laser.center('Exiting...')
        time.sleep(1)
        menu = False
        clear()


    else:
        laser.center('Option does not exist!')
        time.sleep(1)
