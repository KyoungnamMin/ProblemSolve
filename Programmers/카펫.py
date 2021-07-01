def solution(brown, yellow):
    answer = []
    capets = brown + yellow
    for h in range(3, capets):
        if capets % h == 0:
            w = capets//h
            if (h-2)*(w-2) == yellow:
                answer.append(w)
                answer.append(h)
                break
    
    return answer
    