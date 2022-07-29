def solution(s):
    answer = False
    if s.isdigit() and (len(s)==4 or len(s)==6):
        answer = True
    return answer

#다른 방법
# def solution(s):
#     return s.isdigit() and len(s) in (4,6)