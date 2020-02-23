#return value and return statement:

import random

def getanswer(ansnumber):
    if ansnumber == 1:
        return 'It is certain'
    elif ansnumber == 2:
        return 'It is dedicaly so'
    elif ansnumber == 3:
        return 'Why so serious?'
    elif ansnumber == 4:
        return 'Angry??? ha ha h! '
    elif ansnumber == 5:
        return 'Have a nice day'
    elif ansnumber == 6:
        return 'Are you crying?'
    elif ansnumber == 7:
        return 'How is your bestfried'
    elif ansnumber == 8:
        return 'Huh why so serious?'
    elif ansnumber == 9:
        return 'go forward'
    
r = random.randint(1,9)
fortune = getanswer(r)
print(fortune)