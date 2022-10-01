def solution(cacheSize, cities):
    answer = 0
    i = 0 
    len_city = len(cities)
    cache = []
    for i in range(len_city): 
        cities[i] = cities[i].lower()
    for city in cities:
        if city in cache: 
            cache.remove(city) 
            cache.append(city)
            answer += 1
        else: 
            cache.append(city)
            answer += 5 
            if len(cache) == cacheSize + 1:
                cache.pop(0)
    return answer
