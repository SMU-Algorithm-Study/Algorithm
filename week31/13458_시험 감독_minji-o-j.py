"""
N: 시험장의 개수
A: 각 시험장에 있는 응시자의 수
B: 총감독관이시험장에서 감독할 수 있는 응시자의 수
C: 부감독관이 시험장에서 감시할 수 있는 응시자의 수
"""
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

supervisor = N  # 총감독관 한명씩 필요
for people in A:
    people -= B
    if people > 0:
        q, r = divmod(people, C)  # q: quotient, r: remainder
        if r == 0:
            supervisor += q
        else:
            supervisor += q + 1

print(supervisor)
