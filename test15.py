# Liner search

def lin(x,y):
    for i in x:
        if i == y:
            return i
    else:
        return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lin(x=my_list,y=15))