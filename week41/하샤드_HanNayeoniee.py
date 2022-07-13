# 2022.07.05
# 프로그래머스 - 하샤드 수(레벨 1)
# https://school.programmers.co.kr/learn/courses/30/lessons/12947

# x가 하샤드 수라면 x % (x의 자리수의 합) == 0
def solution(x):
    total = sum([int(num) for num in str(x)])  # 각 자리수의 총합 구하기
    
    return True if x % total == 0 else False
