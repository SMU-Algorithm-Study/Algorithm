# 22.07.13
# 프로그래머스 - 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

# 내 풀이
def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        binary1 = format(arr1[i], 'b')  # 지도1 이진수로 변환
        binary2 = format(arr2[i], 'b')  # 지도2 이진수로 변환

        # n자리수가 되도록 맞추기
        # if len(binary1) < n:
        #     binary1 = '0' * (n - len(binary1)) + binary1
        # if len(binary2) < n:
        #     binary2 = '0' * (n - len(binary2)) + binary2

        # 위와 동일한 코드
        binary1 = binary1.zfill(n)
        binary2 = binary2.zfill(n)

        arr = ''
        for j in range(n):
            # 공백
            if binary1[j] == '0' and binary2[j] == '0':
                arr += ' '
            # 벽
            else:
                arr += '#'
        ans.append(arr)
    
    return ans

# 다른 풀이
def solution2(n, arr1, arr2):
    answer = []
    num1 = [bin(arr1[i])[2:].zfill(n) for i in range(n)]
    num2 = [bin(arr2[i])[2:].zfill(n) for i in range(n)]
    
    for i in range(n):
        line = [' ' if (num1[i][j] == '0' and num2[i][j] == '0') else '#' for j in range(n)]
        answer.append(''.join(line))
    return answer


# test case
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
ans = solution(n, arr1, arr2)
print('ans: ', ans)