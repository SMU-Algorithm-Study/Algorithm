# 22.07.26
# 프로그래머스 - 나머지가 1이 되는 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):    
    for x in range(1, n):
        if n % x == 1:
            return x