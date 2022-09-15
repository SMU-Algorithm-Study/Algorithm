def solution(A,B):
    a = sorted(A)
    b = sorted(B, reverse=True)
    answer = sum([a[i]*b[i] for i in range(len(a))])

    return answer

A = [1,4,2]
B = [5,4,4]
print(solution(A, B))

#다른 풀이
# sum(a*b for a, b in zip(sorted(A), sorted(B, reverse=True)))