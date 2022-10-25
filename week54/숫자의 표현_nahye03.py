def solution(n):
    answer=1
    num=0

    for i in range(1, n):
        for j in range(i, n):
            num+=j
            if num==n:
                answer+=1
                num=0
                break
            elif num>=n:
                num=0
                break

    return answer

n = 15
print(solution(n))