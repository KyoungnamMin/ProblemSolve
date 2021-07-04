def solution(progresses, speeds):
    answer = []
    complete_days = [(100-p)//s if (100-p)%s==0 else (100-p)//s+1 for p, s in zip(progresses, speeds)]
    
    count = 1
    ref = complete_days[0]
    for i in range(1, len(complete_days)):
        if ref >= complete_days[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            ref = complete_days[i]
            
    answer.append(count)        
    
    return answer