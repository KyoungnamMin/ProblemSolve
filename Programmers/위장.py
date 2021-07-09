def solution(clothes):
    answer = 1
    dic = {}
    
    for value, key in clothes:
        if key in dic:
            dic[key].append(value)
        else: 
            dic[key] = [value]
    
    for key in dic.keys():
        answer = answer * (len(dic[key])+1)
    
    return answer-1