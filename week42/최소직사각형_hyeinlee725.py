def solution(sizes):
    answer = 0
    max_w, max_h = 0, 0
    for wh in sizes:
        w, h = min(wh), max(wh)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    answer = max_w * max_h
    return answer
