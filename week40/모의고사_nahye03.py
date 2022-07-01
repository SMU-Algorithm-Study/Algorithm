import numpy as np

def solution(answers):
    dic = {}

    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    #전체 문제답 길이에 맞게 수포자의 정답 리스트 만들기
    count = len(answers)
    answer1 = man1 * (count // len(man1)) + man1[:count % len(man1)]
    answer2 = man2 * (count // len(man2)) + man2[:count % len(man2)]
    answer3 = man3 * (count // len(man3)) + man3[:count % len(man3)]

    #배열 비교를 활용하여 정답확인
    dic[1] = sum(np.equal(np.array(answers), np.array(answer1)))
    dic[2] = sum(np.equal(np.array(answers), np.array(answer2)))
    dic[3] = sum(np.equal(np.array(answers), np.array(answer3)))

    #정답 개수가 많은 수포자 고르기
    result = [x for x in dic if dic[x] == max(dic.values())]

    return result

#다른 풀이
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         print(idx, answer)
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result
#
# answers =[1,2,3,4,5]
# solution(answers)