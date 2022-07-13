# 2022.06.29
# 프로그래머스 - K번째수(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for com in commands:
        # i번째 숫자부터 j번째 숫자까지 자르고 정렬
        temp = sorted(array[com[0]-1:com[1]])
        
        # 자른 숫자 중 k번째 숫자 구하기
        answer.append(temp[com[2]-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]	
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
ans = solution(array, commands)
print('answer:', ans)