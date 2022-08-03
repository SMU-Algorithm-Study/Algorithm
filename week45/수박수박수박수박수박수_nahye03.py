def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer+='수'
        else:
            answer+='박'
    return answer

#다른 풀이
# return "수박"*(n//2) + "수"*(n%2)