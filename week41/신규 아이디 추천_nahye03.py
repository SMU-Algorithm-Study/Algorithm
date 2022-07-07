def solution(new_id):
    #1단계 소문자 치환
    a = new_id.lower()
    print(a)

    #2단계 특수문자 제거
    special_str = '~!@#$%^&*()=+[]{}:?,<>/'
    for i in range(len(special_str)):
        a = a.replace(special_str[i],'')
    print(a)

    #3단계 마침표 연속 제거
    while ('..' in a):
        a = a.replace('..','.')
    print(a)

    #4단계 마침표 앞뒤 제거
    a = a.strip('.')
    print(a)

    #5단계 빈문자열 대입
    if not a:
        a = 'a'
    print(a)

    #6단계 문자열 길이 조정, 마침표 제거
    if len(a)>=16:
        a = a[:15].strip('.')
    print(a)

    #7단계 길이 조절
    if len(a)<=2:
        while len(a)<3:
            a = a+a[-1]
    print(a)