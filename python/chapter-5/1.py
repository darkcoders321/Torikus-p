birthdays = {'Alice':'apr 15','Bob':'March 15','Thor':'feb 12'}

while True:
    print('Enter a name:')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday date updated')
