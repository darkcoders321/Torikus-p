#using python args variable in function Definitions

#sum_integers_list.py

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1,2,3]
print(my_sum(list_of_integers))
