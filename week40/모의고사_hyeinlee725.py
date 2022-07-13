def solution(answers):
    answer = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count1, count2, count3 = 0, 0, 0

    # 각 수포자가 얼마나 맞았는지 count
    for i in range(len(answers)):
        if answers[i] == p1[i % 5]:
            count1 += 1
        if answers[i] == p2[i % 8]:
            count2 += 1
        if answers[i] == p3[i % 10]:
            count3 += 1

    # 가장 많이 맞춘 수    
    max_count = max(count1, count2, count3)
    if max_count == count1:
        answer.append(1)
    if max_count == count2:
        answer.append(2)
    if max_count == count3:
        answer.append(3)
    return answer
