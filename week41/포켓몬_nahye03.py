def solution(nums):
    set_nums = set(nums) #중복 제거
    if len(set_nums) <= len(nums)/2:
        answer = len(set_nums)
    else:
        answer = len(nums)/2

    return answer

#다른 방법
# def solution(nums):
#     return min(len(set(nums)), len(nums)/2)