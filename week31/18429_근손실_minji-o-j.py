from itertools import permutations

N, K = map(int, input().split())  # N: 일수, K: 하루마다 줄어드는 중량
A = list(map(int, input().split()))  # 운동 키트의 중량 증가량

kit_order = list(permutations(A, N))  # 사용 가능한 운동 키트 조합
answer = len(kit_order)

for order in kit_order:
    standard = 500
    for kit in order:
        standard -= K  # 중량 감소
        standard += kit  # 운동 키트 사용
        if standard >= 500:
            pass
        else:
            answer -= 1
            break

print(answer)
