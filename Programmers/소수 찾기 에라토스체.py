def get_prime(n):
    prime = [True] * n
    for i in range(2, int(n**0.5) + 1):
        if prime[i] == True:
            for j in range(i+i, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

def solution(n):
    answer = len(get_prime(n+1))
    
    return answer