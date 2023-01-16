n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

ans = 0
for i in range(100):
    for j in range(100):
        for k in range(n):
            if (arr[k][0] <= i < arr[k][0] + 10) and (arr[k][1] <= j < arr[k][1] + 10):
                ans += 1
                break
print(ans)