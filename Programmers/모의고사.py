def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    for idx, answer in enumerate(answers):
        if person1[idx%5] == answer: ans[0]+=1
        if person2[idx%8] == answer: ans[1]+=1
        if person3[idx%10] == answer: ans[2]+=1
    
    answer = list(idx+1 for idx, x in enumerate(ans) if max(ans)==x)
    
    return answer