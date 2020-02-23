#concatenate-2

def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    
    return result
print(concatenate(a = 'Python', b ='is', c = 'great'))
