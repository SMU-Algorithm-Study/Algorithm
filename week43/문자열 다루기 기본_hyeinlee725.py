def solution(s):
    # 길이가 4,6 and 숫자이면
    if (len(s) == 4 or len(s) == 6) and s.isdigit():        
        return True
    else:        
        return False
