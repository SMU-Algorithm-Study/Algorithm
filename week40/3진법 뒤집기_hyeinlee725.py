def solution(n):
    answer = 0
    tmp = ''
    while (n >= 1):
        # 3진법으로 변환
        re = n % 3 # 나머지
        n = n // 3 # 몫
        tmp += str(re) # 나머지를 순차적으로
    # 10진법으로 변환
    answer = int(tmp, 3)
    return answer
