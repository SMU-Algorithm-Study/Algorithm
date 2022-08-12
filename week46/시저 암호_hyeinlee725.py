def solution(s, n):
    answer = ''
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    
    for i in s:
        if i in lower:
            index = lower.find(i) + n
            answer += lower[index % 26]
        elif i in upper:
            index = upper.find(i) + n
            answer += upper[index % 26]
        else:
            answer += " "
    return answer
