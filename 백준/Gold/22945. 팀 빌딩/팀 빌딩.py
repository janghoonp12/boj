def function(n, arr):
    s = 0
    e = n - 1
    ans = (n - 2) * min(arr[s], arr[e])
    while s < e:
        t1 = arr[s]
        t2 = arr[e]

        if t1 < t2:
            while arr[s] <= t1:
                s += 1
            
            if s == e:
                break
            
            ans = max(ans, (e - s - 1) * min(arr[s], arr[e]))
        
        elif t1 > t2:
            while arr[e] <= t2:
                e -= 1
            
            if s == e:
                break
            
            ans = max(ans, (e - s - 1) * min(arr[s], arr[e]))
        
        else:
            t3 = s
            t4 = e

            while arr[s] <= t1 and s < e:
                s += 1
            
            if s == e:
                break
            
            ans = max(ans, (e - s - 1) * min(arr[s], arr[e]))

            s = t3
            while arr[e] <= t2:
                e -= 1
            
            if s == e:
                break
            
            ans = max(ans, (e - s - 1) * min(arr[s], arr[e]))

    print(ans)
    return


n = int(input())
arr = list(map(int, input().split()))
function(n, arr)