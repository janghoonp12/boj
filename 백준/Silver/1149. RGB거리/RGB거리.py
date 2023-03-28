import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [[-1 for i in range(3)] for j in range(N)]

def recur(cur, prv):
    if cur == N:
        return 0
    
    if dp[cur][prv] != -1:
        return dp[cur][prv]

    ret = 1<<30
    for i in range(3):
        if i == prv:
            continue
        ret = min(ret, recur(cur + 1, i) + arr[cur][i])
    
    dp[cur][prv] = ret
    return ret

ans = float('inf')
for i in range(3):
    ans = min(ans, recur(0, i))
print(ans)