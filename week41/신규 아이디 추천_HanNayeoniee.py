# 22.07.08
# 프로그래머스 - 신규 아이디 추천(구현)
# https://school.programmers.co.kr/learn/courses/30/lessons/72410
import re

def solution(new_id):

    # 1단계
    new_id = new_id.lower()

    # 2단계: 알파벳 소문자, 숫자, -, _, .를 제외한 모든 문자 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if not new_id:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    #7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    
    return new_id

# test case
new_id = "=.="
res = solution(new_id)
print('res:', res)