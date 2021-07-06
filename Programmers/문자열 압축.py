def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        prev = s[:i]
        count = 1
        result = ''
        for j in range(i, len(s)+1, i):
            now = s[j:j+i]
            if now == prev:
                count += 1
            else:
                if count != 1:
                    result += (str(count)+prev)
                else:
                    result += prev
                count = 1
            prev = now
        answer = min(answer, len(result))
    
    return answer