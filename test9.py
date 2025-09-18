# Merge Sort
# Time: O(n long n)
# Space: O(n)

D = [-5, 3, 1, 4, -3, -3, 7, -6, 2, 8]

def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    mid = n//2

    L = arr[:mid]
    R = arr[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    l, r = 0, 0
    l_Len, r_Len = len(L), len(R)

    sorted_merge = [0] * n
    i = 0

    while i < l_Len and i < r_Len:
        if L[i] < R[i]:
            sorted_merge[i] = L[i]
            l += 1
        else:
            sorted_merge[i] = R[i]
            r += 1

        i += 1

    while i < l_Len:
        sorted_merge[i] = L[l]
        l += 1
        i += 1

    while i < r_Len:
        sorted_merge[i] = R[r]
        r += 1
        i += 1

    return sorted_merge

merge_sort(D)
print(D)