ans = 0
ribbons = 0
with open("001.in") as file:
    lll = file.readlines()

    for l in lll:

        c = l.replace('\n','').split('x')

        print(c)

        s1 = int(c[0])
        s2 = int(c[1])
        s3 = int(c[2])

        c1,c2,c3 = s1*s2,s1*s3,s2*s3

        print(c1,c2,c3)

        cur = min(c1,c2,c3)+2*(c1+c2+c3)

        ans += cur

        # part 2 
        sides = [s1,s2,s3]
        sides.sort()
        print(sides)

        ribbons += 2*(sides[0] + sides[1]) + s1*s2*s3
        
print(ans)

print(ribbons)