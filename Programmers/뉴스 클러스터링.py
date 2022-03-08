def solution(str1, str2):
    jakad = 0
    str1 = str1.lower()
    str2 = str2.lower()

    A = []
    B = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            A.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            B.append(str2[i] + str2[i + 1])
    # 공집합
    if not A and not B:
        return 65536

    intersection = set(A) & set(B)
    union = set(A) | set(B)

    multi_intersection = sum(
        [min(A.count(inter), B.count(inter)) for inter in intersection]
    )
    multi_union = sum([max(A.count(uni), B.count(uni)) for uni in union])

    jakad = int(multi_intersection / multi_union * 65536)
    return jakad


"""
def make_set(s):
    sets = []
    for i in range(1, len(s)):
        if s[i-1].isalpha() and s[i].isalpha():
            sets.append(s[i-1]+s[i])
    
    return sets

def calc_set(A, B):
    from collections import Counter
    
    cnt_A = Counter(A)
    cnt_B = Counter(B)
    
    intersection = list((cnt_A & cnt_B).elements())
    union = list((cnt_A | cnt_B).elements())
    
    return intersection, union

def solution(str1, str2):
    A = make_set(str1.lower())
    B = make_set(str2.lower())
    inter_AB, union_AB = calc_set(A,B)
    
    if len(union_AB) == 0 and len(inter_AB) == 0:
        jakad = 65536
    else:
        jakad = int((len(inter_AB) / len(union_AB)) * 65536)
    
    return jakad
"""
