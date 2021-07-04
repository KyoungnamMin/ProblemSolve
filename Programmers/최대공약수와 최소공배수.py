def solution(n, m):
    if n>m:
        n, m = m, n
    lcm = m*n
    
    while n>0:
        n, m = m%n, n
    
    gcd = m
    
    answer = [gcd, lcm/gcd]
    
    return answer