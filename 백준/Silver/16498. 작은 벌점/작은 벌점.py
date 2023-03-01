from sys import stdin
I = stdin.readline

a, b, c = map(int, I().split())
A = list(map(int, I().split()))
B = list(map(int, I().split()))
C = sorted(list(map(int, I().split())))
D = 200000000

for i in A:
    for j in B:
        M = max(i, j)
        m = min(i, j)
        
        if m > C[c-1]:
            d = M - C[c-1]
            
        elif M < C[0]:
            d = C[0] - m
            
        else:
            s = 0
            e = c - 1
            upper = 0
            while s <= e:
                mid = (s + e) // 2
                if C[mid] < m:
                    s = mid + 1
                else:
                    upper = mid
                    e = mid - 1

            s = 0
            e = c - 1
            lower = c - 1
            while s <= e:
                mid = (s + e) // 2
                if C[mid] > M:
                    e = mid - 1
                else:
                    lower = mid
                    s = mid + 1
                    
            d = max(M - m, min(C[upper] - m, M - C[lower]))
            
        if d < D:
            D = d
            
print(D)