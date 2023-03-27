def recur(cur, guitar):
    global cnt, ans
    
    if cur == n:
        num = 0
        for i in range(m):
            if music[i] != 0:
                num += 1
        if num > cnt:
            cnt = num
            ans = guitar
        if num == cnt:
            ans = min(ans, guitar)
        return
    
    for i in range(m):
        if arr[cur][1][i] == 'Y':
            music[i] += 1
    recur(cur + 1, guitar + 1)
    for i in range(m):
        if arr[cur][1][i] == 'Y':
            music[i] -= 1
    recur(cur + 1, guitar)


n, m = map(int, input().split())
arr = [list(input().split()) for i in range(n)]
music = [0 for i in range(m)]
cnt = 0
ans = -1

recur(0, 0)
print(ans)