#[14501] 퇴사
n = int(input())
time = []
price = []
profit = [0] * (n + 1)

# 입력
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    price.append(p)

for i in range(n - 1, -1, -1):
    # 남은 일이 없으면
    if time[i] + i > n:
        profit[i] = profit[i + 1]
    else:
        profit[i] = max(price[i] + profit[i + time[i]], profit[i + 1])
        # max((현재 보상 + 현재 다음 보상), 상담을 받지 않는 경우 )

print(profit[0])