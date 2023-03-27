def recur(cur, total):
    visited[total] = True
    if cur == n:
        return
    
    recur(cur + 1, total + arr[cur])
    recur(cur + 1, total)


n = int(input())
arr = sorted(list(map(int, input().split())))
visited = [False for i in range(2000001)]
visited[0] = True

recur(0, 0)

for i in range(2000001):
    if visited[i] != True:
        print(i)
        break