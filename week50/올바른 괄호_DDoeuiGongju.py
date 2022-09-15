def solution(s):
    num = 0
    for i in range(len(s)):
        if num < 0:
            return False
        if s[i] == '(':
            num += 1
        else:
            num -= 1
    return num == 0

s="())("
print(solution(s))