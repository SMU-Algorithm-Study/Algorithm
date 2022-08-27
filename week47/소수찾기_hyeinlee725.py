from itertools import permutations
def solution(numbers):
    num = []
    for i in range(1, len(numbers) + 1):
        per = list(permutations(numbers, i))
        for j in per:
            num.append(int(''.join(j)))
    num = list(set(num))
    answer = len(num)
    for n in num:
        if n < 2:
            answer -= 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                answer -= 1
                break
    return answer
