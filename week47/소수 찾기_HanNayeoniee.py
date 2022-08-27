# 22.08.17 
# 프로그래머스 - 소수찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    else:
        end = int(math.sqrt(num)) + 1
        for i in range(2, end):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    numbers = list(numbers)
    res = []
    cnt = 0
    total_combis = []

    # 1. 만들 수 있는 모든 경우의 숫자 구하기
    for i in range(1, len(numbers)+1):
        combis = list(permutations(numbers, i))
        total_combis += [int(''.join(combi)) for combi in combis]  # 각 tuple을 합치면서 int형으로 변환
        # print('combis:', combis)

    total_combis = list(set(total_combis))  # 중복 제거
    
    for combi in total_combis:
        if is_prime(combi):
            res.append(combi)
            cnt += 1
                
    return cnt