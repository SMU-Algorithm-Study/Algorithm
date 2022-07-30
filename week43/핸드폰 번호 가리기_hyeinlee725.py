def solution(phone_number):
    answer = ''
    # 길이 - 4
    num = len(phone_number) - 4
    # num만큼 *을 넣고, 뒤에 4자라도 넣어줌
    answer = '*' * num + phone_number[num:]
    return answer
