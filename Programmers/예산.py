def solution(d, budget):
    d.sort()
    sum_price = 0
    answer = 0
    
    for price in d:
        if sum_price + price <= budget:
            sum_price += price
            answer += 1
        else:
            break
    
    
    return answer