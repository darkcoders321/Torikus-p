


import random
hangman_pics = ['''

+---+
    |
    |
    |
   ===''', '''
   +---+
   0   |
       |
       |
      ===''', '''
   +---+
   0   |
   |   |
       |
      ===''','''
   +---+
   0   |
  /|   |
       |
      ===''','''
   +---+
   0   |
  /|\  |
       |
      ===''','''
   +---+
   0   |
  /|\  |
  /    |
      ===''','''
   +---+
   0   |
  /|\  |
  / \  |
      ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizerd llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep shunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getrandomword(wordlist):
    #This function returns a random string from the passed list of string

    wordindex = random.randint(0, len(wordlist)-1)
    return wordlist[wordindex]


def displayboard(missedletters,correctletters,secretword):
    print(hangman_pics[len(missedletters)])
    print()

    blanks = '_' * len(secretword)


    for i in range(len(secretword)): #Replace blanks with correctly guessed letters.
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    
    for letter in blanks: #show the secret word with spaces in between each letter.
        print(letter, end='')
        print()

def getguess(alreadyguessed):
    #Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.

    while True:
        print('Guess a letter')
        giess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyguessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a letter.')
        else:
            return guess

def playagain():
    #This is function returns Tre if the player wants to play again; otherwise it returns False.

    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')



print('H A N G M A N')
missedletters=''
correctletters=''
secretword= getrandomword(words)
gameisdone = False

while True:
    displayboard(missedletters, correctletters, secretword)

    # let the plyer enter a letter.
    
    guess = getguess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess

        #Check if the player has won,

        foundallletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundallletters = False
                break

            if foundallletters:
                print('Yes! The secret word is "' + secretword + '" ! you have own!')
                gameisdone = True
    else:
        missedletters = missedletters + guess

        #check if player has guessed too many times and lost.

    if len(missedletters) == len(hangman_pics) - 1:
        displayboard(missedletters, correctletters, secretword)
        print('You have run out of guesses!\nAfter ' + str(len(correctletters)) + secretword + '"')
        gameisdone = True

         #Ask the player if they want to play again (but only if the game is done)

    if gameisdone:
        if playagain():
            missedletters=''
            correctletters=''
            gameisdone=False
            secretword = getrandomword(words)
        else:
            break