# 2022.07.02
# 프로그래머스 - 예산(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/12982

# 부서별 신청 금액이 가장 작은 부서부터 지원한다
from unittest import result


def solution(d, budget):
    answer = 0
    d.sort()  # 지원금 오름차순 정렬
    
    for price in d:
        # 신청 금액이 예산 이내이면 지원
        if price <= budget:
            answer += 1
            budget -= price
    
    return answer

# test case
d = [1, 3, 2, 5, 4]
budget = 9
result = solution(d, budget)
print('result:', result)