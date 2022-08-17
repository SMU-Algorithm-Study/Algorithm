# 22.08.11
# 프로그래머스 - 소수 찾기 (에라토스테네스의 체)
# https://school.programmers.co.kr/learn/courses/30/lessons/12921

# 숫자 n을 입력받아 1부터 n 사이에 존재하는 소수 개수 반환하기
import math

def solution(n):
    arr = [True] * (n+1)
    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:  # 소수인 경우
            # 자기 자신을 제외한 배수 삭제
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    
    return sum([1 for res in arr[2:] if res == True])