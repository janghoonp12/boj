def function(n, arr1, arr2):
    ans = 0
    arr1 = [0] + arr1
    arr2 = [0] + arr2
    arr = [arr1[i] - arr2[i] for i in range(n + 1)]
    
    cnt = {0 : 1}
    prefix = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        prefix[i] = arr[i] + prefix[i - 1]
        ans += cnt.get(prefix[i], 0)
        cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1
    return ans
    

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(function(n, arr1, arr2))