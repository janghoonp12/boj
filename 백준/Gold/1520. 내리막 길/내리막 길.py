import sys
sys.setrecursionlimit(10000)

def count(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < M and 0 <= ny < N) or arr[nx][ny] <= arr[x][y]:
            continue
        dp[x][y] += count(nx, ny)
    
    return dp[x][y]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(M)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dp = [[-1 for i in range(N)] for j in range(M)]
dp[0][0] = 1

ans = count(M - 1, N - 1)

print(ans)