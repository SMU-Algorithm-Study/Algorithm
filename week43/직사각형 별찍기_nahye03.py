a, b = map(int, input().strip().split(' '))
for i in range(b):
    str = '*'*a
    print(str)

#다른 방법
# answer = ('*'*a +'\n')*b