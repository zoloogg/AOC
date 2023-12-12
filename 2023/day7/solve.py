import functools


inn = open('001.in', 'r')
lines = inn.readlines()

FIVE_OF_KIND = 0
FOUR_OF_KIND = 1
FULL_HOUSE = 2
THREE_OF_KIND = 3
TWO_PAIR = 4
ONE_PAIR = 5
HIGH_CARD = 6

results = [[],[],[],[],[],[],[]]

points = {
    "A":10**12, "K":10**11, "Q":10**10, "J":1, "T":10**8, "9":10**7, "8":10**6, "7":10**5, "6":10**4, "5":10**3, "4":10**2, "3":10**1, "2": 9
}

def point_of_cards(s):
    point = 0

    for c in s:
        point += points[c]

    return point

def get_card_counts(s):
    cards = {}

    for c in s:
        if(c in cards.keys()):
            cards[c] += 1
        else:
            cards[c] = 1

    sss = dict(sorted(cards.items(), key=lambda item: item[1]))
    return sss

def first_sorter(a,b):
    aa = a.split(' ')[0]
    bb = b.split(' ')[0]

    scoreA = point_of_cards(aa)
    scoreB = point_of_cards(bb)

    return scoreB - scoreA

def second_sorter(a,b):
    cardsA = get_card_counts(a.split(' ')[0])
    cardsB = get_card_counts(b.split(' ')[0])

    aFirstKey = list(cardsA.keys())[0]
    aSecondKey = list(cardsA.keys())[1]

    bFirstKey = list(cardsB.keys())[0]
    bSecondKey = list(cardsB.keys())[1]

    if(points[aSecondKey] != points[bSecondKey]):
        return points[bSecondKey] - points[aSecondKey]
    
    return points[bFirstKey] - points[aFirstKey]
    
def third_sorter(a,b):
    cardsA = get_card_counts(a.split(' ')[0])
    cardsB = get_card_counts(b.split(' ')[0])


    aFirstKey = list(cardsA.keys())[0]
    aSecondKey = list(cardsA.keys())[1]
    aThirdKey = list(cardsA.keys())[2]

    bFirstKey = list(cardsB.keys())[0]
    bSecondKey = list(cardsB.keys())[1]
    bThirdKey = list(cardsB.keys())[2]

    ## Three of the kind
    if(cardsA[aThirdKey] == 3):
        if(aThirdKey != bThirdKey):
            return points[bThirdKey] - points[aThirdKey]
    
        pointA = points[aSecondKey] + points[aFirstKey]
        pointB = points[bSecondKey] + points[bFirstKey]

        return pointB - pointA
    
    # Two pairs
    pointA = points[aThirdKey] + points[aSecondKey]
    pointB = points[bThirdKey] + points[bSecondKey]

    if(pointA != pointB):
        return pointB - pointA

    return points[bFirstKey] - points[aFirstKey]

def fourth_sorter(a,b):
    cardsA = get_card_counts(a.split(' ')[0])
    cardsB = get_card_counts(b.split(' ')[0])

    aKey = list(cardsA.keys())[3]
    bKey = list(cardsB.keys())[3]

    if(aKey != bKey):
        return points[bKey] - points[aKey]
    
    pointA = 0
    pointB = 0

    for c in cardsA.keys():
        if(c != aKey):
            pointA += points[c]

    for c in cardsB.keys():
        if(c != bKey):
            pointB += points[c]

    return pointB - pointA

def stupid_sorter(a,b):
    for x in range(0,5):
        if(points[b[x]] != points[a[x]]):
            return points[b[x]] - points[a[x]]
        

def determine(line):
    cards = {}

    r = line.split(' ')

    cards = get_card_counts(r[0])

    r2 = r[0]
    lastKey = list(cards.keys())[-1]
    if(lastKey == 'J'):
        if(len(cards.keys()) == 1):
            lastKey = 'A'
        else:
            lastKey = list(cards.keys())[-2]
    print(r2, lastKey)

    ddd = []
    for x in range(0,5):
        if(r2[x] == 'J'):
            ddd.append(lastKey)
        else:
            ddd.append(r2[x])


    print(ddd)

    cards = get_card_counts(''.join(ddd))

    # Five of the kinds
    if(len(cards) == 1):
        return FIVE_OF_KIND
    
    # Four of the kinds OR fullhouse
    if(len(cards) == 2):
        firstKey = list(cards.keys())[0]
        secondKey = list(cards.keys())[1]

        if(cards[firstKey] == 4 or cards[secondKey] == 4):
            return FOUR_OF_KIND

        if(cards[firstKey] == 3 or cards[secondKey] == 3):
            return FULL_HOUSE
        
    if(len(cards) == 3):
        firstKey = list(cards.keys())[0]
        secondKey = list(cards.keys())[1]
        thirdKey = list(cards.keys())[2]

        if(cards[firstKey] == 3 or cards[secondKey] == 3 or cards[thirdKey] == 3):
            return THREE_OF_KIND
        
        return TWO_PAIR
    
    if(len(cards) == 4):
        return ONE_PAIR
    
    return HIGH_CARD
        
for l in lines:
    ttt = determine(l)

    results[ttt].append(l)


# results[0] = sorted(results[0], key=functools.cmp_to_key(first_sorter))
# results[1] = sorted(results[1], key=functools.cmp_to_key(second_sorter))
# results[2] = sorted(results[2], key=functools.cmp_to_key(second_sorter))
# results[3] =sorted(results[3], key=functools.cmp_to_key(third_sorter))
# results[4] = sorted(results[4], key=functools.cmp_to_key(third_sorter))
# results[5] = sorted(results[5], key=functools.cmp_to_key(fourth_sorter))
# results[6] = sorted(results[6], key=functools.cmp_to_key(fourth_sorter))

print(results)
results[0] = sorted(results[0], key=functools.cmp_to_key(stupid_sorter))
results[1] = sorted(results[1], key=functools.cmp_to_key(stupid_sorter))
results[2] = sorted(results[2], key=functools.cmp_to_key(stupid_sorter))
results[3] =sorted(results[3], key=functools.cmp_to_key(stupid_sorter))
results[4] = sorted(results[4], key=functools.cmp_to_key(stupid_sorter))
results[5] = sorted(results[5], key=functools.cmp_to_key(stupid_sorter))
results[6] = sorted(results[6], key=functools.cmp_to_key(stupid_sorter))

print(results)

totalPoint = 0

current = len(lines)

for c in results:
    for d in c:
        rrr = d.split(' ')
        totalPoint += int(rrr[1]) * current

        current -= 1

print(totalPoint)
