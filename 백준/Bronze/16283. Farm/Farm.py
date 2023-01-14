a, b, n, w = map(int, input().split())

cnt = 0
sheep = 0
for i in range(1, n):
    if a * i + (n - i) * b == w:
        cnt += 1
        sheep = i
if cnt == 1:
    print(sheep, n - sheep)
else:
    print(-1)