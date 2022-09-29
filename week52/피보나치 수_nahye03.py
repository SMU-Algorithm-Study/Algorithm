def solution(n):
    a,b=0,1
    for i in range(n-1):
        answer = a+b
        a=b
        b=answer
        #한줄로 하면....
        #a, b=b, a+b
    return answer%1234567