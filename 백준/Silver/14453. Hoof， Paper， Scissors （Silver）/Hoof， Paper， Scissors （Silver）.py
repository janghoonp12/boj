def function(n, arr):
    ans = 0
    prefix = [[0 for i in range(n + 1)] for j in range(3)]
    for i in range(n):
        for j in range(3):
            prefix[j][i + 1] = prefix[j][i]
        if arr[i] == 'H':
            prefix[0][i + 1] += 1
        elif arr[i] == 'P':
            prefix[1][i + 1] += 1
        elif arr[i] == 'S':
            prefix[2][i + 1] += 1
    for i in range(1, n + 1):
        for j in range(3):
            for k in range(3):
                ans = max(ans, prefix[j][i] + prefix[k][n] - prefix[k][i])
    return ans


n = int(input())
arr = [input() for i in range(n)]
print(function(n, arr))