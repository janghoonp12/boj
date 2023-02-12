def function(n, arr):
    ans = [0, 0]
    s = 0
    e = n - 1
    m = 10 ** 10
    while s < e:
        k = arr[s] + arr[e]
        if abs(k) <= m:
            m = abs(k)
            ans[0] = arr[s]
            ans[1] = arr[e]
        if k == 0:
            break
        elif k < 0:
            s += 1
        else:
            e -= 1

    print(ans[0], ans[1])
    return


n = int(input())
arr = list(map(int, input().split()))
function(n, arr)