#소수 판별 함수
def is_prime(num):
    for i in range(2, int(num*0.5)+1):
        if num % i == 0:
            return False
    return True

#숫자 3개 선택한 합이 소수인지 판별하는 함수
def solution(nums):
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for l in range(j+1, len(nums)):
                nums_sum = nums[i]+nums[j]+nums[l]
                if(is_prime(nums_sum)):
                    answer.append(nums_sum)

    return len(answer)

##다른 방법
# def solution(nums):
#     from itertools import combinations as cb
#     answer = 0
#     for a in cb(nums, 3):
#         sum_a = sum(a)
#         for j in range(2, sum_a):
#             if sum_a%j ==0:
#                 break
#         else:
#             answer +=1
#
#     return answer

# nums = [1,2,3,4]
# print(solution(nums))



