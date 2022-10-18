# def solution(s):
#     before = 0
#     for i in s:
#         if before != i:
#             s = s.replace(i+i, '')
#         if not s:
#             return 1
#         before = i
#     return 0
def solution(s):
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    if stack: return 0
    else: return 1



print(solution('baabaabaabaabaabaabaabaabaabaa'))
