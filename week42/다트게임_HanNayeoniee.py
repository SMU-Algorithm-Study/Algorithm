# 22.07.15
# 프로그래머스 - 다트 게임()
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

import math

def star(arr):
    # 숫자 1개면 해당 숫자만 2배
    if len(arr) == 1:
        arr[0] = arr[0] * 2

    # 숫자 2개면 해당 숫자, 이전 숫자 2배
    if len(arr) == 2:
        arr[0] = arr[0] * 2
        arr[1] = arr[1] * 2
    if len(arr) == 3:
        arr[1] = arr[1] * 2
        arr[2] = arr[2] * 2
    return arr

def sharp(arr):
    # 해당 숫자만 -1배
    arr[-1] = arr[-1] * -1
    return arr

def solution(dart):
    arr = []
    for i in range(len(dart)):
        if dart[i] == 'S':
            # 숫자가 10인 경우
            if len(dart[:i]) >= 2 and dart[i-1] == '0' and dart[i-2] == '1':
                score = int(dart[i-2:i])
            else:
                score = int(dart[i-1])
            arr.append(score)  # 숫자 + SDT 조합으로 점수 계산

        if dart[i] == 'D':
            if len(dart[:i]) >= 2 and dart[i-1] == '0' and dart[i-2] == '1':
                score = int(dart[i-2:i]) ** 2
            else:
                score = int(dart[i-1]) ** 2
            arr.append(score)
        if dart[i] == 'T':
            if len(dart[:i]) >= 2 and dart[i-1] == '0' and dart[i-2] == '1':
                score = math.pow(int(dart[i-2:i]), 3)
            else:
                score = math.pow(int(dart[i-1]), 3)
            arr.append(score)

        # '*' award가 존재하는 경우
        if dart[i] == '*':
            arr = star(arr)
        # '#' award가 존재하는 경우
        if dart[i] == '#':
            arr = sharp(arr)

    return int(sum(arr))