from itertools import combinations
import math


def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def solution(nums):
    combination = list(combinations(nums, 3))
    answer = [ans for ans in combination if is_prime(sum(ans))]
    
    return len(answer)
    