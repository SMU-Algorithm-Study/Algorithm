# 22.08.01
# 프로그래머스 - 문자열 내 p와 y의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/12916


def solution(s):
    s = s.lower()
    return True if s.count('p') == s.count('y') else False