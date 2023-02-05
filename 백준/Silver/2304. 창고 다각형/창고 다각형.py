def function(n, arr):
    ans = 0
    prefix = 0
    p_max = 0
    p_prev = 0
    for i in range(n):
        prefix += p_max * (arr[i][0] - p_prev)
        p_max = max(p_max, arr[i][1])
        p_prev = arr[i][0]
    prefix += p_max

    suffix = 0
    s_max = 0
    s_prev = 1010
    for i in range(n):
        suffix += s_max * (s_prev - arr[n - i - 1][0])
        s_max = max(s_max, arr[n - i - 1][1])
        s_prev = arr[n - i - 1][0]
    suffix += s_max

    h = 0
    for i in range(n):
        h = max(h, arr[i][1])

    ans = prefix + suffix - h * (arr[n - 1][0] - arr[0][0] + 1)
    return ans


n = int(input())
arr = sorted([list(map(int, input().split())) for i in range(n)])
print(function(n, arr))