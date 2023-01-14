N = int(input())

cnt = 0
for i in range(1, N - 4):
    for j in range(i + 2, N - i -1):
        k = N - i - j
        if k % 2 != 0:
            continue
        else:
            cnt += 1
print(cnt)