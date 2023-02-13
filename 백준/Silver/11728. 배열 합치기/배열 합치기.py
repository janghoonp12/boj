def function(n, m, arr_a, arr_b):
    arr_a.append(10**9)
    arr_b.append(10**9)
    idx = s1 = s2 = 0
    arr = [0 for i in range(n + m)]
    while idx < n + m:
        if arr_a[s1] < arr_b[s2]:
            arr[idx] = arr_a[s1]
            s1 += 1
            idx += 1
        else:
            arr[idx] = arr_b[s2]
            s2 += 1
            idx += 1
    print(*arr)
    return


n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
function(n, m, arr_a, arr_b)