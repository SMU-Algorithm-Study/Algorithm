def solution(n):
    answer = []
    for i in range(len(str(n)), 0, -1):
        answer.append(int(str(n)[i-1]))

    return answer

##다른 풀이
# def solution(n):
#     return list(map(int, reversed(str(n))))
