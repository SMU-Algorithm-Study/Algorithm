# 배열의 크기
n, m = map(int, input().split())

# 배열 입력과 동시에 합을 구한다
sum_list = []
for r in range(n):  # r: 행
    input_list = list(map(int, input().split()))
    sum_list.append([])
    for c, now_num in enumerate(input_list):  # c: 열
        if r == 0 and c == 0:
            sum_rc = now_num
        elif r == 0:
            sum_rc = sum_list[r][c - 1] + now_num
        elif c == 0:
            sum_rc = sum_list[r - 1][c] + now_num
        else:
            sum_rc = sum_list[r - 1][c] + sum_list[r][c - 1] - sum_list[r - 1][c - 1] + now_num

        sum_list[r].append(sum_rc)

# 합 반환
k = int(input())  # 더하는 횟수

for _ in range(k):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i - 1, j - 1, x - 1, y - 1  # 1행 1열부터 시작
    if i == 0 and j == 0:
        print(sum_list[x][y])
    elif i == 0:
        print(sum_list[x][y] - sum_list[x][j - 1])
    elif j == 0:
        print(sum_list[x][y] - sum_list[i - 1][y])
    else:
        print(sum_list[x][y] - sum_list[i - 1][y] - sum_list[x][j - 1] + sum_list[i - 1][j - 1])
