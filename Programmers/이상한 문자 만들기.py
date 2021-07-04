def solution(s):
    idx = 0
    s = list(s)
    for i, v in enumerate(s):
        if v==' ':
            idx = 0
            continue
        if idx%2==0:
            s[i] = v.upper()
        elif idx%2==1:
            s[i] = v.lower()
        
        idx += 1
        
    answer = ''.join(s)
    
    return answer