def solution(n):
    f = [0, 1]
    for i in range(1, n):
        f.append(f[i-1] + f[i])
    print(f[n])

def solution2(n):
    answer = 0
    miner1 = 0
    miner2 = 1
    for i in range(1, n+1):
        answer = miner1 + miner2
        miner2 = miner1
        miner1 = answer
    return answer

solution(20)
print(solution2(20))
