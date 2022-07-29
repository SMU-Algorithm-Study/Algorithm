def solution(s):
    if len(s)%2==0:
        answer = s[len(s)//2-1]+ s[len(s)//2]
    else:
        answer = s[len(s)//2]
    return answer

s = 'qwer'
print(solution(s))

## 다른 방법
# def solution(s):
#     return str[(len(s)-1)//2:len(s)//2+1]