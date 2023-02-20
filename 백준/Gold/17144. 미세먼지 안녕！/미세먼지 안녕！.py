def spread():
    arr2 = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            arr2[i][j] = arr[i][j]
    
    for i in range(r):
        for j in range(c):
            if arr2[i][j] <= 0:
                continue
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if not (0 <= nx < r and 0 <= ny < c) or arr2[nx][ny] == -1:
                    continue
                arr[nx][ny] += arr2[i][j] // 5
                arr[i][j] -= arr2[i][j] // 5

    
def purify1():
    arr2 = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            arr2[i][j] = arr[i][j]
    
    x = ap1
    y = 1
    d = 0
    arr[x][y] = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == ap1 and ny == 0:
            break
        if not (0 <= nx < r and 0 <= ny < c):
            d = (d + 1) % 4
            continue
        arr[nx][ny] = arr2[x][y]
        x, y = nx, ny


def purify2():
    arr2 = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            arr2[i][j] = arr[i][j]
    
    x = ap2
    y = 1
    d = 0
    arr[x][y] = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx == ap2 and ny == 0:
            break
        if not (0 <= nx < r and 0 <= ny < c):
            d = (d + 3) % 4
            continue
        arr[nx][ny] = arr2[x][y]
        x, y = nx, ny



r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(r)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

ap1 = ap2 = 0
for i in range(r):
    if arr[i][0] == -1:
        ap1 = i
        ap2 = i + 1
        break

for _ in range(t):
    spread()
    purify1()
    purify2()

ans = 2
for i in range(r):
    for j in range(c):
        ans += arr[i][j]
print(ans)