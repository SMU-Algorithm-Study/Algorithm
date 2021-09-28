N, K = map(int, input().split()) # N일, 중량 K
A = list(map(int, input().split())) # 운동 키트의 중량 증가량
check = [0 for _ in range(N)]
result = 0 # 운동 기간동안 항상 중량이 500이상인 경우의 수

def dfs(day, weight):
    global result
    # 중량이 500 미만인 경우 더이상 탐색할 필요 X
    if (weight < 0):
        return
    # 운동 일수(day)가 N이면 result + 1
    if (day == N):
        result += 1
        return
    # 중량 + 운동 키트의 중량 - K가 0 이상이면 재귀함수 호출
    for i in range(N):
        if (check[i] or weight + A[i] - K < 0):
            continue
        check[i] = 1
        dfs(day + 1, weight + A[i] - K)
        check[i] = 0
dfs(0, 0)
print(result)
