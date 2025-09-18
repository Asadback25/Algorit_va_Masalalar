# Buble sort
# Time: O(n²) and Space O(1)

A = [-5, 3, 1, 4, -3, -3, 7, -6, 2, 8]

def buble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                flag = True
                arr[i], arr[i - 1] = arr[i - 1], arr[i]



buble_sort(A)
print(A)
