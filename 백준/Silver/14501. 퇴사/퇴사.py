import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
ans = 0

def recur(cur, total):
    global ans
    
    if cur > N:
        return

    if cur == N:
        ans = max(ans, total)
        return

    recur(cur + arr[cur][0], total + arr[cur][1])
    recur(cur + 1, total)

recur(0, 0)
print(ans)