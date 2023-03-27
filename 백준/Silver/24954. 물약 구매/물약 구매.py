def recur(cur, total):
    global ans
    
    if total > ans:
        return
    
    if cur == n:
        ans = min(ans, total)
        return
    
    for i in range(n):
        if visited[i]:
            continue
        
        visited[i] = True
        for j in range(len(arr[i])):
            cost[arr[i][j][0] - 1] -= arr[i][j][1]
        recur(cur + 1, total + max(cost[i], 1))
        visited[i] = False
        for j in range(len(arr[i])):
            cost[arr[i][j][0] - 1] += arr[i][j][1]
        


n = int(input())
cost = list(map(int, input().split()))
arr = [[] for i in range(n)]

for i in range(n):
    m = int(input())
    arr[i] = [list(map(int, input().split())) for i in range(m)]

ans = 10000
visited = [False for i in range(n)]

recur(0, 0)
print(ans)