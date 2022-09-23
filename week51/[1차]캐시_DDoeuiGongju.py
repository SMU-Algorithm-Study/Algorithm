cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco",
          "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize = 5
cnt=0
db = []
for city in cities:
    city = city.upper()
    if cacheSize:
        if city not in db:
            if len(db) == cacheSize:
                db.pop(0)
            db.append(city)
            cnt += 5
        else:
            db.remove(city)  # 이 부분
            db.append(city)  # 왜 있어야 하지,,?
            cnt += 1
    else:
        cnt += 5

print(cnt)