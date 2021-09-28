# 배열의 크기 N, M
N, M = map(int, input().split())
# N개의 줄에 M개의 정수 - 배열
arr = [list(map(int, input().split())) for _ in range(N)]
# 부분의 개수 K
K = int(input())
dp = [[0] * (M+1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # dp[i - 1][j - 1]은 dp[i][j-1] + dp[i-1][j]할 때 더해져서 2번 더해짐
        # 따라서 dp[i - 1][j - 1]을 한 번 뺌
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j-1]
for _ in range(K):
    # K줄에 주어진 정수 i, j, x, y
    i, j, x, y = map(int, input().split())
    # dp[x][j - 1], dp[i - 1][y]에서 겹치는 dp[i - 1][j - 1]을 더해줌
    res = dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1]
    # K줄에 순서대로 배열의 합 출력
    print(res)
