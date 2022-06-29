def solution(N, stages):
    dic={}
    for i in range(1,N+1):
        not_clear = 0
        come_stage = 0
        for j in stages:
            if j>=i : come_stage+=1
            if j==i: not_clear+=1
        if come_stage == 0:
            dic[i] = 0
        else:
            dic[i] = not_clear/come_stage

    high_fail = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    answer = dict(high_fail).keys()
    return list(answer)
    ##위의 3줄을 이렇게 한줄로도 가능....
    # return sorted(dic, key=lambda x:dic[x], reverse=True)

# N=5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
#
# print(solution(N, stages))
#
# ##다른 방법
# def solution(N, stages):
#     result = {}
#     come_stage = len(stages)
#     for stage in range(1, N+1):
#         if come_stage !=0:
#             not_clear = stages.count(stage)
#             result[stage] = not_clear/come_stage
#             come_stage -= not_clear
#         else:
#             result[stage] =0
#     return sorted(result, key=lambda x:result[x], reverse=True)