# 22.08.04
# 프로그래머스 - 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):            
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if answer else [-1]    