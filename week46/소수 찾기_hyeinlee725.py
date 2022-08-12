def solution(n):
    num = [True] * (n + 1)
    answer = 0
    for i in range(2, int(n ** 0.5) + 1):
        if num[i] == True: # 소수면
            for j in range(i + i, n + 1, i):
                num[j] = False
    for i in range(2, n + 1):
        if num[i]:
            answer += 1
    return answer
