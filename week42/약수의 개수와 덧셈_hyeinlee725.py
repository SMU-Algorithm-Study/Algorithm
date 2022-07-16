def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        div = 0 # 약수의 개수
        for j in range(1, i + 1):	
            if i % j == 0:
                div += 1
        if div % 2 == 0: # 짝수면 +, 홀수면 -
            answer += i
        else:
            answer -= i
    return answer
