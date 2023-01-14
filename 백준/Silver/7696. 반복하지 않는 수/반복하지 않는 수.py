db = [0 for i in range(1000001)]
idx = 1
k = 0
while idx < 1000001:
    k += 1
    t = k
    arr = []
    while t != 0:
        r = t % 10
        arr.append(r)
        t //= 10
    if len(arr) == len(set(arr)):
        db[idx] = k
        idx += 1

while True:
    n = int(input())
    if n == 0:
        break
    print(db[n])