n, k = map(int, input().split())
arr = list(map(int, input().split()))
p_sum = [0 for i in range(n - k + 1)]
for i in range(n - k + 1):
    for j in range(k):
        p_sum[i] += arr[i + j]
ans = max(p_sum)
print(ans)