inn = open('001.in', 'r')
lines = inn.readlines()

def solve(cur):
    nums = [[]]
    cur = cur.replace('\n','').split(' ')
    for c in cur:
        nums[0].append(int(c))

    print(nums)

    idx = 0
    while True:
        nums.append([])

        isGood = True
        for c in range(1,len(nums[idx])):
            print(nums[idx][c], nums[idx][c-1])
            nnn = nums[idx][c] - nums[idx][c-1]
            nums[idx+1].append(nnn)

            if(nnn != 0):
                isGood = False

        idx += 1
        
        if(isGood):
            break

    print(nums,idx)

    while(idx > 0):
        nums[idx-1].insert(0,nums[idx-1][0] - nums[idx][0])
        idx -= 1

    print(nums)

    return nums[0][0]

ans = 0
for l in lines:
    ans += solve(l)

print(ans)