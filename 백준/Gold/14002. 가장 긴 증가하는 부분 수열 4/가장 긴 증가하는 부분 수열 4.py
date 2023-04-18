n = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(n)]
prv = [-1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] <= arr[j]:
            continue
        
        if dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prv[i] = j

ml = 0
idx = 0
for i in range(n):
    if dp[i] > ml:
        ml = dp[i]
        idx = i
ans = []
while idx != -1:
    ans.append(arr[idx])
    idx = prv[idx]

print(ml)
print(*ans[::-1])