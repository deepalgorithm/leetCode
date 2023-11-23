def dp_padovan_sequence(n):
    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    for n in range(4, n+1):
        dp[n] = dp[n -2] + dp[n -3]
        print(dp[n])
    #return dp[n]

#print(dp_padovan_sequence(10))

dp_padovan_sequence(12)