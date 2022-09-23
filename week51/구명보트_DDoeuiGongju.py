people = [70, 30, 50, 20, 20,100]
limit = 100


# people.sort(reverse=True)
# cnt = 1
# for i in people:
#     if limit_w - i < 0:
#         limit = 100
#         cnt+=1
#     limit_w -= i
# print(cnt)

people.sort()
cnt = 0
i = 0
j = len(people)-1

while i <= j:
    cnt += 1
    if people[i] + people[j] <= limit:
        i += 1
    j -= 1
