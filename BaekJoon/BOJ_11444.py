import sys
input = sys.stdin.readline

def fibo(n):
    if arr.get(n) != None:
        return arr[n]
    else:
        if n % 2:
            f = (fibo((n + 1) // 2) % 1000000007) ** 2 + (fibo(n // 2) % 1000000007) ** 2
        else:
            f1 = fibo(n // 2 - 1) % 1000000007
            f2 = fibo(n // 2) % 1000000007
            f = ((f1 + f2) * f2 + f2 * f1) % 1000000007
            
        arr[n] = f % 1000000007
        return f % 1000000007
        
n = int(input())
arr = {0: 0, 1: 1}
print(fibo(n))