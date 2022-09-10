from collections import deque
def solution(queue1, queue2):
    answer = 0
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(que1)
    sum2 = sum(que2)
    
    for i in range(len(queue1) * 3):
        if sum1 > sum2:
            sum1 -= que1[0]
            sum2 += que1[0]
            que2.append(que1.popleft())
        elif sum1 < sum2:
            sum1 += que2[0]
            sum2 -= que2[0]
            que1.append(que2.popleft())
        else:
            return answer
        answer += 1
    return -1
