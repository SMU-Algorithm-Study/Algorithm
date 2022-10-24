def solution(s):
    stack = [s[0]]

    for i in range(1, len(s)):
        if not stack or stack[-1]!=s[i]:
            stack.append(s[i])
        else:
            del stack[-1]

    if not stack:
        answer = 1
    else:
        answer = 0

    return answer

s = 'baabaa'
print(solution(s))