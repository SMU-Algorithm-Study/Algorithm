from itertools import combinations

def solution(numbers):
    answer = []

    for i in list(combinations(numbers, 2)):
        answer.append(sum(i))

    return sorted(list(set(answer))) #sort를 사용하면 none 값이 나옴

numbers = [2,1,3,4,1]
solution(numbers)