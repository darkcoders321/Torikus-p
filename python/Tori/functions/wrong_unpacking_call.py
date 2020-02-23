# Unpacking with the asterisk operators * & **

# wrong_unpacking_call

def my_sum(a,b,c):
    print(a + b + c)

my_list = [1,2,3,4]
my_sum(*my_list)


