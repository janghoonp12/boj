def function(n, k, arr):
    arr.append(1)
    s = e = 0
    cnt = arr[0] % 2
    ans = 0
    while e < n:
        ans = max(ans, e - s + 1 - cnt)
        if cnt <= k:
            e += 1
            cnt += arr[e] % 2
        else:
            cnt -= arr[s] % 2
            s += 1
    print(ans) 
    return


n, k = map(int, input().split())
arr = list(map(int, input().split()))
function(n, k, arr)