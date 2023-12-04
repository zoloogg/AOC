inn = open('001.in', 'r')
lines = inn.readlines()

ans = 0

copies = []
def process(dd,line):
    global ans
    ans += 1

    # print(dd, line)
    g = line.split(':')
    gg = g[1].split('|')
    nums = gg[0].strip().split(' ')
    nums2 = gg[1].strip().split(' ')

    score = 0
    for cur in nums2:
        if(cur != '' and cur in nums):
            score += 1

    # print("score", dd, line, score)

    if(score > 0):
        for c in range(1,score + 1):
            process(dd+c,lines[dd+c])

ccc = 0
for l in lines:
    process(ccc,l)
    ccc += 1

print(ans)
