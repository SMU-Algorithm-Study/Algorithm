import sys
import math
input = sys.stdin.readline
X, Y, D, T = map(int, input().split()) # input
dis = math.sqrt(X**2+Y**2) # 거리
if (dis >= D):
    # 걷기, 점프 뛰고 걷기, 점프 한번 더 뛰기 중 최솟값
    jump = dis // D # 점프 - T초에 D만큼 움직임
    time = min(dis, jump * T + dis % D, (jump + 1) * T)
else:
    # 걷기, 점프 한번하고 되돌아오기, 점프 2번 중 최솟값
    time = min(dis, T + D - dis, 2 * T)
print(time)
