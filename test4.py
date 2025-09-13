# Traditional Binary searching

A = [-4, -3, 0, 2, 7, 8]

def binary(arr, target):
    N = len(A)
    L = 0
    R = N-1

    while L <= R:
        M = L + ((R - L) // 2)

        if arr[M] == target:
            return True
        elif arr[M] < target:
            L = M + 1
        else:
            R = M - 1

    return False

binary(A, 9)