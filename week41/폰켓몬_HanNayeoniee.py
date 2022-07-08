# 2022.07.06
# 프로그래머스 - 폰켓몬(레벨1)
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 문제: N/2개 폰켓몬을 가져갈 때, 최대한 많은 종류의 폰켓몬을 선택하면 몇 종류인지 구하기
# 풀이: 겹치는 종류가 적어 N/2 > 전체 종류가 적으면 최대값인 unique_nums를 반환
#     겹치는 종류가 많아 N/2 <= 전체 종류이면 N/2 반환

def solution(nums):
    unique_nums = list(set(nums))  # 폰켓몬 종류
    
    if len(nums) / 2 < len(unique_nums):
        return len(nums) / 2
    return len(unique_nums)