def solution(numbers):
    num_str = list(map(str, numbers))
    #문자열은 숫자 비교할때 한자리씩 비교하기 때문에 가능
    num_str.sort(key=lambda x:x*4, reverse=True) #*4인 이유? 원소가 1000이하
    answer = str(int("".join(num_str)))

    return answer


numbers = [0,0,0,0]
print(solution(numbers))