# 22.07.13
# 프로그래머스 - 최소 직사각형 (완전 탐색)
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

# 입력으로 들어온 명함 크기를 가로/세로 상관없이 더 긴 길이가 왼쪽에 오도록 정렬한다.
# 긴 변에서 최대값, 짧은 변에서 최대값을 구해 곱하면 가장 작은 지갑의 크기를 구할 수 있다. 

def solution(sizes):
    for size in sizes:
        size[0], size[1] = max(size[0], size[1]), min(size[0], size[1])

    # *는 unpack하는 기호로 list나 tuple을 풀어 준다.
    w1 = max(list(zip(*sizes))[0])
    w2 = max(list(zip(*sizes))[1])
    
    return w1 * w2

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
res = solution(sizes)
print('result: ', res)