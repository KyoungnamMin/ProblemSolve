from math import gcd


def solution(w,h):
    answer = w * h - ((w + h) - gcd(w, h))
    
    return answer


'''
# math에 gcd 함수가 구현되어 있었음!!
# lcm도 구현되어 있음!!

def gcd(a, b):
    return gcd(b, a%b) if b else a
'''