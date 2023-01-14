a, b, c, n = map(int, input().split())

for i in range(n):
    if a * i > n:
        break
    for j in range(n):
        if a * i + b * j > n:
            break
        if (n - a * i - b * j) % c == 0:
            print(1)
            quit()
print(0)