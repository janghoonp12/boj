def function(n, m, arr):
    arr.append(0)
    s = e = 0
    k = arr[0]
    ans = n
    flag = False
    while e < n:
        if k >= m:
            ans = min(ans, e - s + 1)
            k -= arr[s]
            s += 1
            flag = True
        else:
            e += 1
            k += arr[e]
    if flag == False:
        ans = 0
    print(ans)
    return


n, m = map(int, input().split())
arr = list(map(int, input().split()))
function(n, m, arr)