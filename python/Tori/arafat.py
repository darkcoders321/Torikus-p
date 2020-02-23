print('[***] Here is the ###Updated Program...\n')
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
    time.sleep(1)
    print('Guha ti ondhokar ebong voyongkor...')
    time.sleep(1)
    print('Ekti boro dragon  apnar samone aslo ebong ha korlo ebong...')
    print()
    time.sleep(2)


    friendlycave = random.randint(1, 2);

    if choosencave == friendlycave:
        print('Apnake guptodhon diye dilo.!!\n')
        time.sleep(1)
        print('Apni ki guptodhon vagavagi krte chan?')
        ans = str(input())
        while ans == 'ha' or ans == 'h':
                    time.sleep(2)
                    print('\nApni sotti e akjn honest man\n Apni ki janen?\n"Honesty is the best policy." ebong apnr shei "Honesty" ta ase...\n"Congratulations!!!"\n')
                    break
        else:
            time.sleep(2)
            print('\nAi jonnoi oi Dragonta apnake ek kamore mukher moddhe niye nilo ebong gile fello!!!\n')
            time.sleep(0.5)
            print('Apni obossoy janen na j, "Honesty is the best policy."\n')
            print('\nTobe apni ata obossoy janben j, \n-----"Loove paap, Paape mrittu."')
                   
    else:
        print('Apnake ek kamore mukher moddhe niye nilo ebong gile fello!!!')
        
playagain = 'ha'
while playagain == 'ha' or playagain == 'h':
    displayintro()
    cavenumber = choosecave()
    checkcave(cavenumber)

    print('Apni ki abar khelte can? (ha othoba na)')
    playagain = input()
