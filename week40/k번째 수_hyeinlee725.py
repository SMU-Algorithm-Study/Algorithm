def solution(array, commands):
    answer = []
    
    for comm in commands:
        arr = array[comm[0] - 1 : comm[1]]
        arr.sort()
        # k번째 수를 찾아 answer에 저장
        answer.append(arr[comm[2]-1])
    return answer
