def function(h, w, arr):
    ans = 0
    prefix = arr[0]
    suffix = arr[-1]
    m = max(arr)
    for i in range(w):
        prefix = max(prefix, arr[i])
        suffix = max(suffix, arr[w - i - 1])
        ans += prefix + suffix - arr[i] - m
    return ans


h, w = map(int, input().split())
arr = list(map(int, input().split()))
print(function(h, w, arr))
