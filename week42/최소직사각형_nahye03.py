def solution(sizes):
    max_ = list(map(max, sizes))
    min_ = list(map(min, sizes))

    answer = max(max_) * max(min_)
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))