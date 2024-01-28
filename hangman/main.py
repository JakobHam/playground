import time
import os

name1 = input('What is your name?  ')
print('Hello ' + name1 + ', lets play Hangman!!!')
time.sleep(1)
print('You need to select a word which the other player guesses!')
time.sleep(.5)
word = input('choose a word: ')
os.system('clear')
print('KEEP IT SECRET!!!')
print('')
print('Now hand off the device to the other player.')
time.sleep(2)

name2 = input('What is your name? ')
print('Hello ' + name2 + ', lets play Hangman!!!')
time.sleep(.5)
print(name1 + ' has already chosen a word for you to guess.')


turns = 10
num_guess = ''

while turns > 0:
    num_guess =+ 1
    turns =+ 1
    
    
    #doesnt work from here on or mybe even earlier just gets stuck :(
    
    
print(turns)
print(num_guess)    
print('does it work??')