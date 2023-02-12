def function(n, arr, x):
    ans = 0
    arr.sort()
    s = 0
    e = n - 1

    while s < e:
        k = arr[s] + arr[e]
        if k == x:
            ans += 1
            s += 1
            e -= 1
        elif k < x:
            s += 1
        else:
            e -= 1
    print(ans)
    return


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
function(n, arr, x)