import math

def solution(n):
    sum = 0
    for i in range(n//2+1):
        sum += math.comb(n-i,i)
    return sum%1234567

n = 3
print(solution(n))
