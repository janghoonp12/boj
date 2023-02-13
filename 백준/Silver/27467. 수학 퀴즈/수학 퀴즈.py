n = int(input())
arr = list(map(int, input().split()))
p = q = 0
for i in range(n):
    if arr[i] % 3 == 0:
        q += 1
    elif arr[i] % 3 == 1:
        p += 1
    else:
        p -= 1
        q -= 1
print(p, q)