import math

def solution(w,h):
    return w*h - (w+h-math.gcd(w,h))

w=100000000
h=999999999
print(solution(w,h))