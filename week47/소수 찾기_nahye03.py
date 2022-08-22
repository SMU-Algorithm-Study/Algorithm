from itertools import permutations

def is_prime(num):
    if num<=1:
        return False
    elif num ==2:
        return True
    else:
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                return False
    return True

def solution(numbers):
    answer = []
    num = []
    perm =[]

    ##이거 그냥 list(numbers)하면 끝...int도 필요없...
    for i in numbers:
        num.append(int(i))

    for i in range(1, len(numbers)+1):
        perm.extend(list(permutations(num, i)))

    for i in perm:
        tmp=''
        for j in range(len(i)):
            tmp+= str(i[j])

        if is_prime(int(tmp)):
            answer.append(int(tmp))

    return len(set(answer))

numbers='011'
print(solution(numbers))

#다른 방법
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i+1))))
#     a -= set(range(0,2))
#     for i in range(2, int(max(a)**0.5)+1):
#         a -= set(range(i*2, max(a)+1, i))
#     return len(a)