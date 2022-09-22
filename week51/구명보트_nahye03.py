def solution(people, limit):
    answer = 0
    people = sorted(people)
    i=0
    j=len(people)-1
    while i<j:
        if people[i]+people[j]>limit:
            j-=1
        else:
            i+=1
            j-=1
        if i==j:
            answer+=1
        answer += 1
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
