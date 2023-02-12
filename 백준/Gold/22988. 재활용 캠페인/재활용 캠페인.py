def function(n, x, arr):
    ans = 0
    arr.sort()
    s = 0
    e = n - 1
    cnt = n

    while arr[e] == x and e >= 0:
        ans += 1
        cnt -= 1
        e -= 1

    while s < e:
        if (arr[s] + arr[e]) * 2 >= x:
            ans += 1
            s += 1
            e -= 1
            cnt -= 2 
        else:
            s += 1

    ans += cnt // 3
    
    print(ans)
    return


n, x = map(int, input().split())
arr = list(map(int, input().split()))
function(n, x, arr)