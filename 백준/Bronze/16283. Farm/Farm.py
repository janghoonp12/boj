a, b, n, w = map(int, input().split())
s = g = cnt = 0
for i in range(1, n):
    if a * i + b * (n - i) == w:
        s, g = i, n - i
        cnt += 1
if cnt == 1:
    print(s, g)
else:
    print(-1)