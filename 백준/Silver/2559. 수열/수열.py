def function(n, k, arr):
    ans = 0
    arr = [0] + arr
    prefix = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix[i] = arr[i] + prefix[i - 1]
    ans = (-10**8)
    for i in range(n - k + 1):
        ans = max(ans, prefix[i + k] - prefix[i])
    
    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(function(n, k, arr))