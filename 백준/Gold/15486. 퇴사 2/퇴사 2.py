import sys
input = sys.stdin.readline


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [0 for i in range(N + 1)]

for i in range(N + 1):
    for j in range(1, 51):
        if i - j < 0 or arr[i - j][0] != j:
            continue
        dp[i] = max(dp[i], dp[i - j] + arr[i - j][1])
    if i != 0:
        dp[i] = max(dp[i - 1], dp[i])

print(dp[-1])