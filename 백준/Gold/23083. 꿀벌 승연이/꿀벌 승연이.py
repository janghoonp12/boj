n, m = map(int, input().split())
k = int(input())
holes = [[1 for i in range(m + 1)] for j in range(n + 1)]
for i in range(k):
    x, y = map(int, input().split())
    holes[x][y] = 0

dx = [[-1, 0, 1], [-1, -1, 0]]
dy = [[0, -1, -1], [0, -1, -1]]

arr = [[0 for i in range(m + 1)] for j in range(n + 1)]
arr[1][1] = 1
for y in range(1, m + 1):
    for x in range(1, n + 1):
        for k in range(3):
            nx = x + dx[y % 2][k]
            ny = y + dy[y % 2][k]
            if not (nx <= n and ny <= m):
                continue

            arr[x][y] += holes[nx][ny] * arr[nx][ny]

print(arr[n][m] % (10**9 + 7))