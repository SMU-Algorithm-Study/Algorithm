def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
    return answer

x = 2
n = 5
print(solution(x, n))

#다른 풀이
# def solution(x, n):
#     return [i*x+x for i in range(n)]