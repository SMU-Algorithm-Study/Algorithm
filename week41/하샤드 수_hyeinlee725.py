def solution(x):
    # 각 자리수로 나눠서 list에 담기
    arr = list(map(int, str(x)))
    if (x % sum(arr)) == 0:
        return True
    else:
        return False
