"""def ojonerekok():
    while True:
        print('Ekhane apnar ekok ti din:')
        ekok = input()
        if ekok == '1gm':
            print('1gm = 1000 mg')
        elif ekok == '1kg':
            print('1kg = 1000 gm')
        elif ekok == '1kt':
            print('1kt(kuintal) = 100 kg (killogram)')
        elif ekok == '1mt':
            print('1mt(metrikton) = 10kt = 1000 kg')
            break
        else:
            print('wrong input')
ojonerekok()    """

class ojekok():
    print('Ei porgram er maddhome apni ojoner ekoj jante parben.\nApni jodi 1gram er ekok jante chan tahole input dite hobe 1gm\nEkoi vabe apni jodi 1kg  er ekok jante chan tahole apnake input dite hobe 1kg\n1 kuintal er jonno input dite hobe 1kt\n1 metrikton er jonno input dite hobe 1mt\nprogram ti upovog korun. :)')
    def ojonerekok():
        while True:
            print('Ekhane apnar ekok ti din:')
            ekok = input()
            if ekok == '1gm':
                print('1gm = 1000ml')
            elif ekok == '1kg':
                print('1kg = 1000gm')
            elif ekok == '1kt':
                print('1kt = 100kg')
            elif ekok =='1mt':
                print('1mt = 10kt or 1000kg')
                break
            else:
                print('Wrong input!!')
ojekok.ojonerekok()

class khetrofol():
    print('''
    1 eor er jonno input "1er"\n
    1 hector er jonno input "1hk"\n
    10,000 borgometer er jonno input "10kbg"\n
    100 borgo decimeter er jonno input "100bdm"\n
    1 borgo decameter er jonno input "1bdm"\n

    ''')
    def khetrofolerekok():
        while True:
            print('Ekhane apnar vule jawa ekok likhun:')
            kekok = input()
            if kekok == '1er':
             print('1er = 100 borgo meter')
            elif kekok == '1hk':
                print('1hk = 100 eyor')
            elif kekok == '10kbg':
                print('10kbg = 1 hector ')
            elif kekok == '100bdm':
                print('100bdm = 1 borgo meter ')
            elif kekok == '1bdm':
                print('1bdm = 1 eyor = 100 borgometer')
                break
            else:
                print('wrong input!!')
khetrofol.khetrofolerekok()
