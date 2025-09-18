# Count Sort
# Time: O(K + N), k is the area of maxx
# Space: O(N)

F = [8, 3, 4, 6, 2, 8, 4, 5, 3, 4]

def count_sort(arr):
    n = len(arr)
    maxx = max(arr)
    count = [0] * (maxx + 1)

    for i in arr:
        count[i] += 1

    i = 0
    for c in range(maxx + 1):
        while count[c] > 0:
            arr[i] = c
            count[c] -= 1
            i += 1

count_sort(F)
print(F)