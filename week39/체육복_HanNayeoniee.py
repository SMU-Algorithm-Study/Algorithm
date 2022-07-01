# 2022.06.25
# 프로그래머스 - 체육복(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/42862#


def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()

    # lost와 reserve에 동일한 학생이 있는 경우
    # 체육복을 도난당했지만 여분을 가져온 학생은 본인이 사용하고, 다른 학생에게는 빌려줄 수 없음
    for i in range(len(reserve)):
        if reserve[i] in lost:
            j = lost.index(reserve[i])
            reserve[i] = -1
            lost[j] = -1
            answer += 1

    prev = 0
    for loss in lost:
        i = prev

        while i < len(reserve):
            if abs(reserve[i] - loss) == 1:
                print(loss, reserve[i], reserve)
                reserve[i] = -1
                answer += 1
                prev = i
                break
            else:
                i += 1
    
    return answer

### 테스트 케이스
n = 5
lost = [1, 2]
reserve = [2, 3]

# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]

# n = 5
# lost = [3, 4]
# reserve = [3]
answer = solution(n, lost, reserve)
print('answer:', answer)