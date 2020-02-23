#The global statement

def spam():
    global eggs
    eggs = 'torikus'

eggs = 'global'
spam()
print(eggs)

