# 2022.06.25
# 프로그래머스 - 소수 만들기(레벨 1)
# https://programmers.co.kr/learn/courses/30/lessons/12977

import math
from itertools import combinations

def is_prime_number(n):
    if n < 2:
        return False
    else:
        end = int(math.sqrt(n)) + 1
        for i in range(2, end):
            if n % i == 0:
                return False
        return True

def solution(nums):
    cnt = 0
    
    # 1. nums 중 숫자 3개를 조합해 만들 수 있는 모든 경우 구하기
    combis = [sum(combi) for combi in list(combinations(nums, 3))]
    # combis = list(set(combis))  # 숫자 3개의 합이 동일해 중복되는 숫자라도, 숫자 3개의 조합이 다르기 때문에 중복을 제거하면 안 됨!
    
    # 2. 소수인 숫자 개수 세기
    for combi in combis:
        if is_prime_number(combi):
            cnt += 1

    return cnt