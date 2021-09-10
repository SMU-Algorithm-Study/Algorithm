#[프로그래머스] 수식 최대화

from itertools import permutations
# 연산하기
def compute(num1, num2, op):
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2

# 계산 
def cal(expr, oper):
    exp = list(expr) # 이렇게 안하면 solution에 있는 expr 리스트 값이 cal함수에서 리스트를 수정한대로 변해서 이유를 잘 모르겠음
    
    for op in oper:
        while op in exp: # 연산자가 안에 있다면 계산하기
            loc = exp.index(op) # 연산자의 위치
            exp.pop(loc) # 연산자 리스트에서 빼기
            # 앞의 숫자 (연산자) 뒤의 숫자 / 리스트에서 계산한 숫자 빼기
            val = compute(int(exp.pop(loc - 1)), int(exp.pop(loc - 1)), op)
            exp.insert(loc - 1, val) # 계산한 값 추가
    
    return abs(exp[0]) # 계산한 값 절대값

def solution(expression):
    opers = list(permutations('+-*', 3)) # 연산자 모든 경우의 수
    # 각 연산자와 숫자사이에 공백을 줘서 split로 문자를 나눔
    expr = expression.replace('+',' + ').replace('-',' - ').replace('*', ' * ').split() 
    # 여러 문자를 기준으로 문자를 나누고 싶었는데 어떻게 하는지 못 찾음
    maxi = 0

    # 모든 우선순위로 계산
    for oper in opers:
        maxi = max(maxi, cal(expr, oper)) # 가장 큰 상금 금액

    return maxi
