import math
from itertools import permutations


def is_prime_number(n):
    """소수판별 함수"""
    if n==0 or n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True

    
def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))
        for j in range(len(arr)):
            n = int(''.join(map(str,arr[j])))
            if is_prime_number(n):                
                answer.append(n)
                
    answer = list(set(answer))
    return len(answer)
