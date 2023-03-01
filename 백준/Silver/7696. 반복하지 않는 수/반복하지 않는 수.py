import sys

L = []
while True:
    n = int(sys.stdin.readline())
    L.append(n)
    if n == 0:
        break

M = max(L)
nums = [0] * (M + 1)
i = 1
idx = 1
while idx <= M:
    check = []
    d = 10
    k = i
    while(k>0):
        check.append(k%d)
        k = k//d


    # print(check)
    if len(set(check)) == len(check):
        nums[idx] = i
        idx += 1
    i += 1


for l in L:
    if l == 0:
        break
    print(nums[l])