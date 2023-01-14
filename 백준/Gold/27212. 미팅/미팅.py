N, M, C = map(int, input().split())
W = [list(map(int, input().split())) for i in range(C)]
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr = [[0 for i in range(M + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        arr[i][j] = W[arr_A[i - 1] - 1][arr_B[j - 1] - 1]
    
dp = [[0 for i in range(M + 1)] for j in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j - 1] + arr[i][j], dp[i - 1][j], dp[i][j - 1])

print(dp[N][M])