# Selection sort
# Time: O(n²) and Space: O(1)

C = [-5, 3, 1, 4, -3, -3, 7, -6, 2, 8]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(C)
print(C)