def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(n):
        if citations[n-1] >= n: return n
        if citations[i] <= i:
            answer = i
            break
    
    return answer