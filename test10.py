# Quick Sort
# Time: O(n log n)
# Space: O(log n)

E = [-5, 3, 1, 4, -3, -3, 7, -6, 2, 8]

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    p = arr[-1]

    L = [x for x in arr[:-1] if x <= p]
    R = [x for x in arr[:-1] if x > p]

    L = quick_sort(L)
    R = quick_sort(R)

    return L + R

quick_sort(E)
print(E)