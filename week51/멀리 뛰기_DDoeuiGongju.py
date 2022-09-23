def solution(n):
    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = 1, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[n] % 1234567
    # if n < 3:
    #     return n % 1234567
    # else:
    #     return solution(n-1)+solution(n-2)

print(solution(1))