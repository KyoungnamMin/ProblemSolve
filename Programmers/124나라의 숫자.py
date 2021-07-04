def solution(n):
    answer = ''
    rule = [1, 2, 4]
    
    while (n > 0):
        n -= 1
        answer = str(rule[n%3]) + answer
        n = n // 3
    
    return answer