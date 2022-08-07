def solution(a, b):
    if a<b:
        answer = sum([i for i in range(a,b+1)])
    else:
        answer = sum([i for i in range(b,a+1)])
    return answer

##다른 풀이
# def adder(a, b):
#     if a>b : a,b = b, a
#     return sum(range(a, b+1))
#
# def adder(a, b):
#     return (abs(a-b)+1)*(a+b)//2
#
# def adder(a, b):
#     return sum(range(min(a, b), max(a, b)+1))