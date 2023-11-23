def dp_2n_tile(n):
    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2
    for n in range(3, n+1):
        dp[n] = dp[n -1] + dp[n -2]
    return dp[n]

print(dp_2n_tile(9))