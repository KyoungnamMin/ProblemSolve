def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    j = len(people) - 1
    i = 0
    while i<=j:
        if (people[i]+people[j]) <= limit:
            j-=1
        answer+=1
        i+=1
    
    return answer