#keyword arguments:

def add(a,b):
    return a + b

x = add(a = 2, b = 3)
print(x)

y = add(b = 7, a = 11)
print(y)

total = add(b = x, a = y)
print(total)
