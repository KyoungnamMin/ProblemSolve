def solution(n,a,b):
    if a > b:
        a, b = b, a
    
    game = 0
    while a != b:
        game += 1
        a = a//2 if a%2==0 else (a+1)//2
        b = b//2 if b%2==0 else (b+1)//2
    
    return game