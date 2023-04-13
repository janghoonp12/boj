n = int(input())
arr = [i + 1 for i in range(n)]

idx = 0
for t in range(1, n):
    idx += (t**3) - 1
    idx %= len(arr)
    arr.pop(idx)
print(arr.pop())