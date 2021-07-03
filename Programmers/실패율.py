def solution(N, stages):
    answer = []
    fail_rate = []
    person = len(stages)
    
    for i in range(1, N+1):
        fail_person = stages.count(i)
        if fail_person == 0:
            fail_rate.append((0, i))
            continue
        fail_rate.append((fail_person/person, i))
        person -= fail_person
    
    fail_rate.sort(key = lambda x: (-x[0], x[1]))
    
    for i in range(N):
        value, idx = fail_rate[i]
        answer.append(idx)
    
    return answer