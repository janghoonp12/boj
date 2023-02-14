from sys import stdin
I = stdin.readline

N, d, k, c = map(int,I().split())
li = []
for i in range(N):
    li.append(int(I()))
li += li[:k-1]

ct = [0] * (d + 1)
ct[c] = 1


s = 0
e = k-1
for i in range(k):
    ct[li[i]] += 1

C = 0
for i in ct:
    if i:
        C += 1
if C == k + 1:
    print(C)
    quit()
M = C

while s < N - 2:
    ct[li[s]] -= 1
    if ct[li[s]] == 0:
        C -= 1
    s += 1
    e += 1
    if ct[li[e]] == 0:
        C += 1
    ct[li[e]] += 1

    if C == k + 1:
        print(C)
        quit()
    elif C > M:
        M = C
        
print(M)