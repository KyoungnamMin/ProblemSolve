def solution(n):
    battery=0
    while n>0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            battery+=1
        
    return battery

# 이진법으로도 풀 수 있었음
# return bin(n).count('1')