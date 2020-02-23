
print("[#] Coded by: Torikus Sadik Raihan.")
print('[#] Noob programmer of python.')
print('[#] special Thanks to intellegence404 team.')
print()
print()

import random

guessesTaken = 0

print('Vaya/Afa apnar nam ki?')
myName = input()

number = random.randint(1,20)
print('Acca,' + myName + ', afa/vaya ami 1 theke 20 er moddhe ekta number niya cinta kortechilam ar ki.')

for guessesTaken in range(6):
    print('Guess koren to ami thik kon bumber ta niya cinta kortechilam?') #Four spaces in front of print
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Apnar guess er obostha khub kharap!!')
    if guess > number:
        break 
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('wow!! oboseshe,' + myName + ' ! apni amar cinta kora number   ' + guessesTaken + ' ber korei fellen!!')
if guess != number:
    number = str(number)
    print('Holo nah!!. Ami je number ta niya cinta kortechilam seta hocce: ' + number + '.')