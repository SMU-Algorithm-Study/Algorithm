# 22.08.08
# 프로그래머스 - 제일 작은 수 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min_idx = arr.index(min(arr))
        return arr[:min_idx] + arr[min_idx+1:]