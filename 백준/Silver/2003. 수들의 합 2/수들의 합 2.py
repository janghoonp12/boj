def function(n, m, arr):
    ans = 0
    arr = arr + [0]
    s = 0
    e = 0
    k = arr[0]
    while e < n:
        if k == m:
            ans += 1
            k -= arr[s]
            s += 1
            e += 1
            k += arr[e]
        elif k < m:
            e += 1
            k += arr[e]
        else:
            k -= arr[s]
            s += 1
    print(ans)
    return


n, m = map(int, input().split())
arr = list(map(int, input().split()))
function(n, m, arr)