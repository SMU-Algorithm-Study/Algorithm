def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper():
            ##chr((ord(i)-ord('A')+n)%26+ord('A'))
            if ord(i) + n > 90:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)
        else:
            ##chr((ord(i)-ord('a')+n)%26+ord('a'))
            if ord(i) + n > 122:
                answer += chr(ord(i) + n - 26)
            else:
                answer += chr(ord(i) + n)

    return answer