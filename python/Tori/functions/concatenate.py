#concatenate

def concatenate (**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result
print(concatenate(a = 'python ',b = 'is ', c = 'great'))
