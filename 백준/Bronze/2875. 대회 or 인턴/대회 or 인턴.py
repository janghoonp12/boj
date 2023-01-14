n, m, k = map(int, input().split())

ans = 0
for i in range(1, m + 1):
    if n >= 2 * i and 3 * i + k <= n + m:
        ans = max(ans, i)
    else:
        break
print(ans)