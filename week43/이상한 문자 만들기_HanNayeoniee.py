# 22.07.20
# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):    
    res = ''
    words = s.split(' ')
    
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                res += word[i].upper()
            else:
                res += word[i].lower()
        res += ' '
    
    return res[:-1]


s = "try hello world"
res = solution(s)
print('res:', res)