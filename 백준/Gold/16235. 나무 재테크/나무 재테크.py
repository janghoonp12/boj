from collections import deque


def spring_summer():
    for i in range(n):
        for j in range(n):
            dead_soil = 0
            for k in range(len(tree_arr[i][j])):
                if soil[i][j] < tree_arr[i][j][k]:
                    while len(tree_arr[i][j]) > k:
                        z = tree_arr[i][j].pop()
                        dead_soil += z // 2
                    break
                else:
                    soil[i][j] -= tree_arr[i][j][k]
                    tree_arr[i][j][k] += 1
            
            soil[i][j] += dead_soil


def fall_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree_arr[i][j])):
                if tree_arr[i][j][k] % 5 != 0:
                    continue
                
                for d in range(8):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    tree_arr[nx][ny].appendleft(1)
            
            soil[i][j] += arr[i][j]                


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
tree = [list(map(int, input().split())) for i in range(m)]

soil = [[5 for i in range(n)] for j in range(n)]
tree_arr = [[deque() for i in range(n)] for j in range(n)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for x, y, z in tree:
    tree_arr[x - 1][y - 1].append(z)

for _ in range(k):
    spring_summer()
    fall_winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree_arr[i][j])
print(ans)