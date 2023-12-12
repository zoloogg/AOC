import math


inn = open('001.in', 'r')
lines = inn.readlines()

mmm = {}

cnt = -1

for l in lines:
    cnt += 1
    if(cnt < 2):
        continue

    cur = l[0:3]
    lll = l[7:10]
    rrr = l[12:15]

    mmm[cur] = [lll,rrr]

# step = 0
# cur ='AAA'

lines[0] = lines[0].strip().replace('\n','')

# while True:
#     if(cur == 'ZZZ'):
#         print(step)
#         break

#     nnn = lines[0][(step) % len(lines[0])]

#     cur = mmm[cur][0 if nnn == 'L' else 1]

#     step += 1

c2 = []

for m in mmm.keys():
    if(m[2] == 'A'):
        c2.append(m)

nums = []
for ccc in c2:
    current = [ccc]
    step = 0
    while True:
        nnn = lines[0][(step) % len(lines[0])]

        nextPath = []
        for c in current:
            nextPath.append(mmm[c][0 if nnn == 'L' else 1])


        current = nextPath

        # print(nextPath)

        step += 1

        isGood = True

        for c in nextPath:
            if(c[2] != 'Z'):
                isGood = False
                break

        if(isGood):
            print(step)
            nums.append(step)
            break

print(nums)
print(print(math.lcm(*nums)))