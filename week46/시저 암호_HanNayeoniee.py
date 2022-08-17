# 22.08.09
# 프로그래머스 - 시저 암호
# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    answer = ''
    for word in s:
        # 공백인 경우 그대로 공백
        if not word.isalpha():
            answer += ' '
        else:
            res = ord(word) + n
            # z 또는 Z라서 n만큼 밀었을 떄 알파벳 범위를 벗어나는 경우 조정
            if (65 <= ord(word) <= 90 and res > 90) or (97 <= ord(word) <= 122 and res > 122):
                res -= 26
            answer += str(chr(res))

    return answer