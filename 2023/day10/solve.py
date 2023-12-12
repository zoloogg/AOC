inn = open('day10_input.txt', 'r')
lines = inn.readlines()

def find_start():
    for x in range(0,len(lines)):
        for y in range(0, len(lines[0])):
            if(lines[x][y] == 'S'):
                return (x,y)

def find_next_direction(x,y, coming):
    # print("cur ", lines[x][y])
    if(lines[x][y] == '|'):
        if(coming == 3):
            return (x-1,y,3)
        
        return (x+1,y,1)
    
    if(lines[x][y] == '-'):
        if(coming == 0):
            return (x,y+1,0)
        
        return (x,y-1,2)
    
    if(lines[x][y] == 'L'):
        if(coming == 1):
            return (x,y+1,0)
        
        return (x-1,y,3)
    
    if(lines[x][y] == 'J'):
        if(coming == 0):
            return (x-1,y,3)
        
        return (x,y-1,2)
    
    if(lines[x][y] == '7'):
        if(coming == 0):
            return (x+1,y,1)
        
        return (x,y-1,2)
    
    if(lines[x][y] == 'F'):
        if(coming == 2):
            return (x+1,y,1)
        
        return (x,y+1,0)


# x = 0
# y = 1
# dir = 2
# for zzz in range(0,10):
#     print(x,y,dir)
#     x,y,dir = find_next_direction(x,y,dir)
#     print("res: ",x,y,dir)

start = find_start()
print(start)

x = start[0]+1
y = start[1]
dir = 1

cnt = 0

while True:
    x,y,dir = find_next_direction(x,y,dir)

    print("next: ", x,y,dir)
    if(lines[x][y] == 'S'):
        break

    cnt += 1

print(cnt / 2 + 1)