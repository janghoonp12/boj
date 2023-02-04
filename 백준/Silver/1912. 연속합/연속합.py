def function(n, arr):
    arr = [0] + arr
    prefix = [0 for i in range(n + 1)]
    ans = arr[1]
    m = 0
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i]
        ans = max(ans, prefix[i] - m)
        m = min(m, prefix[i])
    return ans


n = int(input())
arr = list(map(int, input().split()))
print(function(n, arr))