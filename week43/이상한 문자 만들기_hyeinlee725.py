def solution(s):
    answer = []
    for s in s.split(' '): # 띄어쓰기로 구분
        res = ''
        for i in range(len(s)):
            if i % 2 == 0: # 짝수 : 대문자
                res += s[i].upper()
            elif i % 2 == 1: # 홀수: 소문자
                res += s[i].lower()
        answer.append(res)
    return ' '.join(answer)
