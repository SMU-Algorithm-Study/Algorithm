# 22.08.02
# 프로그래머스 - 수박수박수박수박수박수?
# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    a, b = divmod(n, 2)
    answer = '수박' * a

    return answer + '수' if b else answer