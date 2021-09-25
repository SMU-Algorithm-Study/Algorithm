import sys
input = sys.stdin.readline
N = int(input()) # 시험장 개수
A = list(map(int, input().split())) # 응시자 수
B, C = map(int, input().split())
result = 0 # 최소한의 감독 수
for i in range(N):
    A[i] -= B # 총감독관 1명 필요
    # A[i]가 음수인 경우 0으로
    if (A[i] < 0): 
        A[i] = 0
    # 부감독관 배치
    result += ((A[i] // C) + 1)
    # 나머지가 존재하면 + 1(나머지 없으면 그대로)
    if (A[i] % C != 0):
        result += 1
print(result)
