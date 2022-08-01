# 22.07.25
# 프로그래머스 - 가운데 글자 가져오기
# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    n, m = divmod(len(s), 2)
    if m: 
        return s[n]
    else: 
        return s[n-1:n+1]
