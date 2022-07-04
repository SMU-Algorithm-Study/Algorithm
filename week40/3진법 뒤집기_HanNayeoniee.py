# 2022.06.29
# 프로그래머스 - 3진법 뒤집기(레벨1)
# https://programmers.co.kr/learn/courses/30/lessons/68935


# 10진법 -> q진법 변환
def convert(n, q):
    base = ''
    
    while n > 0:
        res = divmod(n, q)
        base += str(res[1])
        n = res[0]

    return base[::-1]


# 방법 1 - 10진법 -> n진법 변환 함수를 따로 선언해 사용
# 3진법으로 만든 후 뒤집어야 하므로, 기존 변환 함수에서 만든 str값을 그대로 반환하면 됨
def solution(n):

    def convert(n, q):
        base = ''
        
        while n > 0:
            res = divmod(n, q)
            base += str(res[1])
            n = res[0]

        return base

    converted = convert(n, 3)
    res = int(converted, 3)

    return res

res = solution(45)
print('res:', res)


# 방법2 - 따로 함수 선언하지 않고 한 번에
def solution2(n):
    base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        base += str(mod)

    return int(base, 3)
