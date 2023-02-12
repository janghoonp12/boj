def function(n):
    ans = 0
    P = [True for i in range(n + 1)]
    P[0] = P[1] = False
    cnt = 0
    arr = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        if P[i] == False:
            continue
        arr[cnt] = i
        cnt += 1
        for j in range(i, (n // i) + 1):
            P[i * j] = False
    
    s = e = 0
    k = arr[0]
    while e < cnt:
        if k == n:
            ans += 1
            k -= arr[s]
            s += 1
            e += 1
            k += arr[e]
        elif k < n:
            e += 1
            k += arr[e]
        else:
            k -= arr[s]
            s += 1

    print(ans)
    return


n = int(input())
function(n)