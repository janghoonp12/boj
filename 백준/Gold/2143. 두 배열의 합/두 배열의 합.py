def function(t, n, arr1, m, arr2):
    arr1 = [0] + arr1
    arr2 = [0] + arr2
    
    prefix1 = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix1[i] = prefix1[i - 1] + arr1[i]
    cnt1 = {} 
    for i in range(n):
        for j in range(i + 1, n + 1):
            k = prefix1[j] - prefix1[i]
            cnt1[k] = cnt1.get(k, 0) + 1
    
    ans = 0
    prefix2 = [0 for i in range(m + 1)]
    for i in range(1, m + 1):
        prefix2[i] = prefix2[i - 1] + arr2[i]
    for i in range(m):
        for j in range(i + 1, m + 1):
            k = prefix2[j] - prefix2[i]
            ans += cnt1.get(t - k, 0)
    
    return ans


t = int(input())
n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
print(function(t, n, arr1, m, arr2))