# 22.07.18
# https://school.programmers.co.kr/learn/courses/30/lessons/12948

# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수
def solution(phone):
    return '*' * (len(phone) - 4) + phone[-4:]

phone = "01033334444"
res = solution(phone)
print('res:', res)