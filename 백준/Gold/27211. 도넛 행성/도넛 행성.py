from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            continue
        
        cnt += 1
        que = deque()
        que.append((i, j))
        arr[i][j] = 1
        while len(que) > 0:
            x, y = que[0]
            que.popleft()
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx == -1:
                    nx += N
                if ny == -1:
                    ny += M
                if nx == N:
                    nx -= N
                if ny == M:
                    ny -= M
                
                if arr[nx][ny]:
                    continue
                
                que.append((nx, ny))
                arr[nx][ny] = 1
print(cnt)