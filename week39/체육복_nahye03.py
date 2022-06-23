def solution(n, lost, reserve):
    lost_ = set(lost)-set(reserve)
    reserve_ = set(reserve)-set(lost)

    for j in reserve_:
        if j-1 in lost_:
            lost_.remove(j-1)
        elif j+1 in lost_:
            lost_.remove(j+1)

    return n-len(lost_)

# n = 7
# lost = [2,3,5,8]
# reserve = [1,3,6,8]
#
# print(solution(n,lost,reserve))