def function(n, m, arr):
    ans = 0
    newarr = [[0 for i in range(m + 1)]] + [[0] + i for i in arr]
    prefix = [[0 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = newarr[i][j] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

    ans = newarr[1][1]
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                for l in range(j + 1, m + 1):
                    ans = max(ans, prefix[k][l] - prefix[k][j] - prefix[i][l] + prefix[i][j])
    return ans


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
print(function(n, m, arr))