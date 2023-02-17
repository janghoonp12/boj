def get_line():
    global line
    
    line = [0 for i in range(n * n + 1)]
    visited = [[False for i in range(n)] for j in range(n)]
    x = y = d = 0
    
    for i in range(n * n):
        line[n * n - 1 - i] = arr[x][y]
        visited[x][y] = True
        
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
            d = (d + 1) % 4
        
        x = x + dx[d]
        y = y + dy[d]


def get_arr():
    global arr

    arr = [[0 for i in range(n)] for j in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    x = y = d = 0
    
    for i in range(n * n):
        arr[x][y] = line[n * n - 1 - i]
        visited[x][y] = True
        
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
            d = (d + 1) % 4
        
        x = x + dx[d]
        y = y + dy[d]


def blizzard(d, s):
    x = y = n // 2

    for i in range(s):
        x += dx2[d]
        y += dy2[d]
        arr[x][y] = 0
    get_line()


def move():
    global line

    line2 = [0 for i in range(n * n + 1)]
    for i in range(n * n):
        line2[i] = line[i]

    line = [0 for i in range(n * n + 1)]
    idx = 1
    for i in range(n * n):
        if line2[i] == 0:
            continue

        line[idx] = line2[i]
        idx += 1
    get_arr()


def explode():
    cnt = 0
    b = 0
    for i in range(n * n + 1):
        if line[i] == b:
            cnt += 1
            continue
        
        if cnt >= 4:
            for j in range(cnt):
                line[i - j - 1] = 0
            ex_cnt[b] += cnt
        b = line[i]
        cnt = 1
    get_arr()


def new_bubble():
    global line
    
    line2 = [0 for i in range(n * n + 1)]
    for i in range(n * n):
        line2[i] = line[i]
    
    line = [0 for i in range(n * n + 1)]
    idx = 1
    cnt = 1
    b = line2[1]
    for i in range(2, n * n + 1):
        if line2[i] == b:
            cnt += 1
            continue
        
        line[idx], line[idx + 1] = cnt, b
        idx += 2
        cnt = 1
        b = line2[i]
        if b == 0 or idx >= n * n:
            break
    get_arr()


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

line = [0 for i in range(n * n + 1)]
ex_cnt = [0 for i in range(4)]
ans = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dx2 = [0, -1, 1, 0, 0]
dy2 = [0, 0, 0, -1, 1]

get_line()

for _ in range(m):
    d, s = map(int, input().split())
    blizzard(d, s)
    while True:
        line3 = [0 for i in range(n * n + 1)]
        for i in range(n * n):
            line3[i] = line[i]
        move()
        explode()
        if line3 == line:
            break
    new_bubble()

for i in range(4):
    ans += i * ex_cnt[i]
print(ans)