from collections import Counter

n = int(input())
cardList = sorted(list(map(int, input().split())))
m = int(input())
targetCard = list(map(int, input().split()))

counting = Counter(cardList)

for target in targetCard:
    print(counting[target], end=' ')