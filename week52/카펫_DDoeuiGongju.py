def solution(brown, yellow):
    total = brown + yellow
    for width in range(1, brown):
        height = total / width
        if total % width == 0 and width >= height and (width - 2) * (height - 2) == yellow:
            return width, height


print(solution(24, 24))
