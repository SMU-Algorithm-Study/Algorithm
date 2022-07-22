# 22.07.21
# https://school.programmers.co.kr/learn/courses/30/lessons/12969?language=python3


# 별(*) 문자를 이용해 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력
n, m = map(int, input().split())
for _ in range(m):
    print(''.join(['*'] * n))