from itertools import combinations

def solution(numbers):
    answer = sorted(list(set(x+y for x, y in combinations(numbers, 2))))
    return answer