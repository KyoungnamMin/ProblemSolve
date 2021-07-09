from collections import Counter
import re

def solution(s):
    p = re.compile('\d+')
    s = Counter(p.findall(s))
    
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
    
    '''answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    
    for i in s:
        val = i.split(',')
        for j in val:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer'''