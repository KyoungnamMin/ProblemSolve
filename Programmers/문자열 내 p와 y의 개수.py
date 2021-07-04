def solution(s):
    s = s.lower()
    pc = s.count('p')
    sc = s.count('y')
    print(pc, sc)
    answer = True if pc==sc else False
    
    return answer