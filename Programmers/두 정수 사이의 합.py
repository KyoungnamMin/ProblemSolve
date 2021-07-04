def solution(a, b):
    if a > b:
        a, b = b, a
    answer = [v for v in range(a, b+1)]
    
    return sum(answer)