N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

d = 0
for i in range(1, N - 1):
    temp = abs(arr[i - 1][0] - arr[i][0]) + abs(arr[i - 1][1] - arr[i][1]) + abs(arr[i + 1][0] - arr[i][0]) + abs(arr[i + 1][1] - arr[i][1]) - abs(arr[i - 1][0] - arr[i + 1][0]) - abs(arr[i - 1][1] - arr[i + 1][1])
    d = max(d, temp)

ans = -d
for i in range(1, N):
    ans += abs(arr[i - 1][0] - arr[i][0]) + abs(arr[i - 1][1] - arr[i][1])

print(ans)