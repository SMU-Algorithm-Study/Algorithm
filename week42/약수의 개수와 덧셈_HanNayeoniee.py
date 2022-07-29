# 22.07.11
# 프로그래머스 - 약수의 개수와 덧셈(소수)
# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):

    # 각 숫자의 약수의 개수 구하기
    def sosu(num):
        cnt = 0
        divisor = 1
        while divisor <= num:
            if num % divisor == 0:
                cnt += 1
            divisor += 1
        return cnt
    
    answer = 0
    
    while left <= right:
        cnt = sosu(left)
        # 약수가 짝수개이면 더하고
        if cnt % 2 == 0:
            answer += left
        # 약수가 홀수개이면 뺀다
        else:
            answer -= left
        left += 1    
    
    return answer