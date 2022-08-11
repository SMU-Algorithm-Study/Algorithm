# 22.08.08
# 프로그래머스 - 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    return list(map(int, str(n)))[::-1]

n = 12345
res = solution(n)
print(res)