# Insertion sort
# Time: O(n²) and Space: O(1)

B = [-5, 3, 1, 4, -3, -3, 7, -6, 2, 8]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break


insertion_sort(B)
print(B)