# Using readlines()
inn = open('001.in', 'r')
lines = inn.readlines()

currentLine = 0
N = 200
M = 200
gears = [ [1] * N for _ in range(M)]
gearsCounts =  [ [0] * N for _ in range(M)]

def determine_is_good(cc, rr, lll,nnn):
    global gears, gearsCounts
    gearLocations = []

    for x in range(cc-1,cc+2):
        for y in range(rr - lll -1, rr+1):
          

            # print(x,y)

            if(x >= 0 and y >= 0 and x < len(lines) and y < len(lines[0])):
                if(lines[x][y] == '*' and ((x*100000+y) not in gearLocations)):
                    # print(x,y,nnn)
                    gearLocations.append((x*100000+y))
                    gears[x][y] *= nnn
                    gearsCounts[x][y] += 1
            
                try:
                    if(lines[x][y] not in ['0','1','2','3','4','5','6','7','8','9','.','\n']):
                        return True
                except:
                    continue
            
    return False
    
ans = 0
currentLine= 0
for l in lines:
    current = 0
    currentRow = 0

    for c in l:
        if(c >= '0' and c<='9'):
            current = current * 10 + int(c)
        elif(current != 0):
            isGood = determine_is_good(currentLine, currentRow, len(str(current)), current)

            # print(current,isGood)
            
            if(isGood):
                ans += current
                # print(current)s
            current = 0

        currentRow += 1

    currentLine += 1

print(ans)


ans2 = 0
for x in range(N):
    for y in range(M):
        if(gearsCounts[x][y] == 2):
            ans2 += gears[x][y]

print(ans2)