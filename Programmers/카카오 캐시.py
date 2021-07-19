from collections import deque


def solution(cacheSize, cities):
    if not cacheSize:
        return len(cities) * 5

    cities = [city.lower() for city in cities]
    lru_que = deque()

    answer = 0
    for idx, city in enumerate(cities):
        # cache hit
        if city in lru_que:
            lru_que.remove(city)
            lru_que.append(city)
            answer += 1
        # cache miss
        else:
            if len(lru_que) == cacheSize:
                lru_que.popleft()
            lru_que.append(city)
            answer += 5

    return answer
