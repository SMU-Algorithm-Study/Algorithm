def solution(d, budget):
    answer = 0
    d.sort() # 오름차순 정렬
    
    for i in range(len(d)):
        # 예산보다 작으면 구매 가능
        # d를 빼고 개수 + 1
        if budget >= d[i]:
            budget -= d[i]
            answer += 1
    return answer
