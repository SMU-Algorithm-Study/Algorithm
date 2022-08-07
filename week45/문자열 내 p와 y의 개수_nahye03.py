def solution(s):
    s = s.lower()
    return (True if s.count('p')==s.count('y') else False)
    #그냥 s.count('p') == s.count('y')