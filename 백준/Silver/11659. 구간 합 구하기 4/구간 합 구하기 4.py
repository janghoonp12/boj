def pfx(n, arr):
    prefix = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i]
    return prefix

def function(n, m, arr, arr2):
    arr = [0] + arr
    prefix = pfx(n, arr)
    for i, j in arr2:
        print(prefix[j] - prefix[i - 1])
    return


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [list(map(int, input().split())) for i in range(m)]
function(n, m, arr, arr2)