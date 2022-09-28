def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache: #cache hit
            cache.remove(city)
            cache.append(city)
            answer+=1
        else: #cache miss
            if len(cache)<cacheSize:
                cache.append(city)
            else:
                cache.append(city)
                cache.pop(0)
            answer+=5
    return answer

cacheSize = 3
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(cacheSize, cities))

#다른풀이
# import collections
# def solution(cacheSize, cities):
#     cache = collections.deque(maxlen=cacheSize)
#     time=0
#     for i in cities:
#         s = i.lower()
#         if s in cache:
#             cache.remove(s)
#             cache.append(s)
#             time+=1
#         else:
#             cache.append(s)
#             time+=5
#     return time