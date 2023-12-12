import copy 


inn = open('001.in', 'r')
lines = inn.readlines()

emptyCount = -1

mmm = [[],[],[],[],[],[],[]]

lineCount = 0

for l in lines:
    lineCount += 1

    if(lineCount < 2):
        continue


    if(l == '\n'):
        emptyCount += 1
        continue

    if('map:' in l):
        continue

    ll = l.replace('\n','').split()
    mmm[emptyCount].append([int(ll[0]),int(ll[1]),int(ll[2])])

seeds = lines[0].split(':')[1].strip().split(' ')

# for s in seeds:
#     if(ccc % 2 == 1):
#         continue

#     print(ccc)

#     for c in range(int(s),int(s)+int(seeds[ccc+1]) +1):
#         n = int(c)

#         idx = 0

#         # print("seed", n)
        
#         while(idx < 7):
#             sss = n
#             for cur in mmm[idx]:
#                 if(sss >= cur[1] and sss <= cur[1] + cur[2]):
#                     n = cur[0] - cur[1] + sss
#                     # print("good", idx, cur , n)
#                     # break

#             idx += 1

#         # print(n, ans)
#         if(ans == -1):
#             ans = n
#         else:
#             ans = min(ans, n)

#     ccc += 1

# print(ans)

# 57075758
# 131650022

seedRanges = []
idx = -1
for s in seeds:
    idx += 1
    if(idx % 2 == 1):
        continue

    seedRanges.append([int(s),int(s) + int(seeds[idx+1])])

print(seedRanges)

def get_range(inn,out):
    start = max(inn[0], out[0])
    end = min(inn[1], out[1])

    if(start > end):
        return None
    
    return [start,end]

ans = None
for s in seedRanges:
    newInputRanges = [s]

    idx = 0
    endRanges = []
    while(idx < 7):
        inputRanges = newInputRanges
        newInputRanges = []
        for inputRange in inputRanges:
            for c in mmm[idx]:
                rrr = get_range(inputRange,[c[1],c[1]+c[2]])

                if(rrr is not None):
                    newInputRanges.append([c[0]-c[1]+rrr[0],c[0]-c[1]+rrr[1]])

        idx +=1

        if(idx == 7):
            endRanges = newInputRanges

            for e in endRanges:
                if(ans == None or e[0] < ans):
                    ans = e[0]
                    print(e)


    print("END:" , endRanges)

print(ans)