def solution(strings, n):
    answer= sorted(sorted(strings), key=lambda x:x[n])
    return answer

strings =["abce", "abcd", "cdx"]
n = 2
print(solution(strings,n))