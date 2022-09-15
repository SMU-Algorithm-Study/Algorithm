def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i, j in zip(A, B):
        answer+=i*j
    return answer

A, B = [1, 4, 2], [5, 4, 4]
print(solution(A, B))