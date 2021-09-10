# 순열 : permutations 라이브러리
from itertools import permutations

# 연산자 - 3가지
def operation(num1, num2, oper):
    if (oper == '+'):
        return str(int(num1) + int(num2))
    if (oper == '-'):
        return str(int(num1) - int(num2))
    if (oper == '*'):
        return str(int(num1) * int(num2))

# 연산을 하는 함수
def calculate(exp, oper):
    result = []
    tmp = ""
    for e in exp:
        if (e.isdigit() == True): # exp값이 숫자이면
            tmp += i # tmp에 추가
        else: # 연산자이면
            result.append(tmp) # result에 tmp에 있는 값 추가
            result.append(e) # 연산자 추가
            tmp = "" # tmp 초기화
    result.append(tmp) # tmp에 남아있는 값을 추가해줌
    # result : [숫자, 연산자, 숫자, ..., 숫자]와 같은 상태
    for op in oper:
        stack = []
        while True:
            if (len(result) == 0): # result에 값이 없으면
                break # 연산 종료
            tmp = result.pop(0) # 매번 첫번째 원소를 pop
            if (tmp == op): # pop한 값이 현재 계산해야하는 op이면
                # 계산해서 stack에 append
                stack.append(operation(stack.pop(), result.pop(0), op))
            else:# pop한 값이 현재 계산해야하는 op가 아니면
                stack.append(tmp) # stack에 그대로 append
        result = stack # 최종 결괏값인지 알 수 없으므로
    return abs(int(result[0])) # 계산한 값의 절댓값

def solution(expression):
    answer = 0
    op = ['+', '-', '*'] # 모든 연산자
    op = list(permutations(op, 3))
    # 우선순위에 대해 계산 - 가장 큰 상금 금액
    for perm in op:
        answer = max(answer, calculate(expression, perm))
    return answer
