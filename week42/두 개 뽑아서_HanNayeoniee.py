# 22.07.11
# 프로그래머스 - 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644


from itertools import combinations
def solution(numbers):
    combis = [sum(combi) for combi in list(combinations(numbers, 2))]
    combis = sorted(list(set(combis)))
    
    return combis