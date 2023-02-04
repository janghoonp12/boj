def function(n, k, arr):
    new_arr = [0] + arr
    prefix = [0 for i in range(n + 1)]
    cnt = {0 : 1}
    ans = 0
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + new_arr[i]
        ans += cnt.get(prefix[i] - k, 0)
        cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1
    return ans


n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(function(n, k, arr))