def function(n, arr):
    ans = 0
    arr = [-10**9 - 1] + arr + [10**9 + 1]
    prefix = [0 for i in range(n + 2)]
    for i in range(1, n + 2):
        prefix[i] = arr[i] - arr[i - 1]
    cnt = 0
    idx = 0
    for i in range(1, n + 1):
        if prefix[i] < 0:
            cnt += 1
            idx = i
    
    if cnt == 0:
        ans = n
    elif cnt > 1:
        ans = 0
    else:
        ans = 0
        if arr[idx] >= arr[idx - 2]:
            ans += 1
        if arr[idx + 1] >= arr[idx - 1]:
            ans += 1

    return ans


n = int(input())
arr = list(map(int, input().split()))
print(function(n, arr))