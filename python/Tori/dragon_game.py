print('[#] This game is renewing by : Torikus sadik Raihan, Shakil babu, Fahim morshed and Arafat hossain.')
print('[#] Noob python programmer.')

import random
import time

def displayintro():
    print('''  Mone korun dragon e poripurno akta field a apni daray acen. Apnar samone duto guha dekhte pelen. Prothom guhay je dragon ta ace se apnar khoti korbe na se apnar bondhu hobe ebong tar kache thaka gupto dhon gulo apnar sathe vagavagi korbe. opor dike ditiyo guhay je dragon ta ace seta onek lovi se to apnake or gupto dhon dibei na borong apnake kheya felbe.''')
    print()

def choosecave():
    cave =''
    while cave !='1' and cave !='2':
        print('Apni kon guhar moddhe jaben? (1 na 2)')
        cave = input()
    return cave

def checkcave(choosencave):
    print('Apni guhar moddhe probesh korcen...')
    time.sleep(2)
    print('Guha ti ondhokar ebong voyongkor...')
    time.sleep(2)
    print('Ekti boro dragon  apnar samone aslo ebong ha korlo ebong...')
    print()
    time.sleep(2)


    friendlycave = random.randint(1,2)

    if choosencave == str(friendlycave):
        print('Apnake guptodhon diye dilo.!!')
    else:
        print('Apnake ek kamore mukher moddhe niye nilo ebong gile fello!!!')
playagain = 'ha'
while playagain == 'ha' or playagain == 'h':
    displayintro()
    cavenumber = choosecave()
    checkcave(cavenumber)

    print('Apni ki abar khelte can? (ha othoba na)')
    playagain = input()