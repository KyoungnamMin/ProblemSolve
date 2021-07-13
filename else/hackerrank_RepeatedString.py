
def repeatedString(s, n):
    # Write your code here
    from collections import Counter
    answer = 0
    if s=='a': return n
    if 'a' not in s: return 0

    if n > len(s):
        q, r = divmod(n, len(s))
        cnt = Counter(s).get('a')
        cnt *= q
        remain = Counter(s[:r]).get('a') if 'a' in s[:r] else 0
        answer = cnt + remain
    else:
        s = s[:n]
        answer = Counter(s).get('a')
    return answer

s = 'gfcaaaecbg'
n = 547602
print(repeatedString(s,n))