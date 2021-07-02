def solution(n, lost, reserve):
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    
    for rest in set_reserve:
        if rest-1 in set_lost:
            set_lost.remove(rest-1)
        elif rest+1 in set_lost:
            set_lost.remove(rest+1)
            
    return n-len(set_lost)