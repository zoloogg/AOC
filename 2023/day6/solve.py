times = [40,92,97,90]
distance = [215, 1064, 1505, 1100]

ans = 1
idx = 0
for x in times:
    possibles = 0
    for y in range(0, x+1):
        if((x-y)*y > distance[idx]):
                possibles += 1

    ans *= possibles
    idx += 1

print(ans)

# Part 2
ttt = 40929790
distance = 215106415051100

x*(40929790-x) > 215106415051100

a = 6192350.99727
b = 34737439.0027

print(b-a)