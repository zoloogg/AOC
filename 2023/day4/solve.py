inn = open('000.in', 'r')
lines = inn.readlines()

tot = 0

ans = 0
for l in lines:
    g = l.split(':')
    gg = g[1].split('|')
    nums = gg[0].strip().split(' ')
    nums2 = gg[1].strip().split(' ')

    score = 0
    for cur in nums2:
        if(cur != '' and cur in nums):
            print(cur)
            if(score == 0):
                score = 1
            else:
                score *= 2

    ans += score

print(ans)
