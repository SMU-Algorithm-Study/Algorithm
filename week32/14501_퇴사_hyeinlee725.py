import sys
input = sys.stdin.readline
N = int(input()) # 남은 일 수
T, P = [], [] # 상담을 완료하는데 걸리는 기간 T, 상담을 했을 때 받을 수 있는 금액 P
answer = [0 for i in range(N + 1)]
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)
for i in range(N - 1, -1, -1):
    # 퇴사일을 넘어가는 경우
    if (T[i] + i > N):
        answer[i] = answer[i + 1]
    else: # i일에 상담하는 것 or 안하는 것 중 큰 값
        answer[i] = max(P[i] + answer[i + T[i]], answer[i + 1])
print(answer[0])
