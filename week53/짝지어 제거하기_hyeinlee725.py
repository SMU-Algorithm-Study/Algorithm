def solution(s):
    stack = []
    for i in :
        if not stack:
            stack.append(i)
        else:
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i) 
    if stack : 
        return 0 
    else : 
        return 1   
