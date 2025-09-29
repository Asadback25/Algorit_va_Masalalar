# Binary search

def binary_search(my_list, item):
    L = 0
    R = len(my_list) - 1
    while L <= R:
        mid = (R + L) // 2
        guess = my_list[mid]
        if guess == item:
            return item
        elif guess > item:
            R = mid - 1
        else:
            L = mid + 1
    return None

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(mylist, 11))