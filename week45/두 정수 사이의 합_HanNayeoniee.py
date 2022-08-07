# 22.08.01
# 프로그래머스 - 두 정수 사이의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/12912

# 내 풀이
def solution(a, b):
    a, b = min(a, b), max(a, b)
    answer = 0
    for i in range(a, b+1):
        answer += i

    return answer


# 다른 풀이
def solution2(a, b):
    if a == b:
        return a
    else:
        if a > b: a, b = b, a
        return sum(range(a, b+1))
