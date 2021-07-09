from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for crs in course:
        tmp = []
        for order in orders:
            combi = combinations(sorted(order), crs)
            tmp += combi
        counter = Counter(tmp)
        if len(counter) and max(counter.values()) > 1:
            answer +=[''.join(x) for x in counter if counter[x]==max(counter.values())]
    
    
    return sorted(answer)