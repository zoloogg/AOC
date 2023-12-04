# Using readlines()
inn = open('001.in', 'r')
lines = inn.readlines()
 
def find_number(stt, color):
    pos = stt.find(color)

    if(pos == -1):
        return 0
    
    dd = stt.strip().split(' ')[0]
    
    return int(dd)

ans = 0
ans2 = 0
cnt = 0
for line in lines:
    cnt += 1
    print(line)

    d = line.split(':')

    print(d)

    d2 = d[1].split(';')

    print(d2)

    isGood = True

    r2,g2,b2 = 0,0,0
    for d3 in d2:
        d4 = d3.split(',')
        print(d4)

        gg,rr,bb = 0,0,0
        for d5 in d4:
            gg = max(gg,find_number(d5, 'green'))
            rr = max(rr,find_number(d5,'red'))
            bb = max(bb,find_number(d5,'blue'))

        r2 = max(r2,rr)
        b2 = max(b2,bb)
        g2 = max(g2,gg)


        if(rr > 12 or gg > 13 or bb > 14):
            isGood = False

    if(isGood):
        ans += cnt

    ans2 += r2*g2*b2

print(ans)
print(ans2)