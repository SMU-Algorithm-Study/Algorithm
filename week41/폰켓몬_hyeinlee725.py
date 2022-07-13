def solution(nums):
    answer = 0
    num = len(nums) // 2 # 뽑을 개수
    mon = list(set(nums)) # 중복 제외한 폰켓몬

    # mon에서 뽑을 개수보다 작은 만큼 +1
    for m in mon:
        if(answer < num):
            answer += 1
    return answer
