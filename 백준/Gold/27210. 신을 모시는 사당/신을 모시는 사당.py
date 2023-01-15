N = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(N + 1):
    if arr[i] == 2:
        arr[i] = -1

prefix = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + arr[i]

ans = max(prefix) - min(prefix)
print(ans)