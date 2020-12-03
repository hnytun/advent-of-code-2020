
def CheckTrees(map,x,y):
    currentx=0
    tree=0
    for area in map[0::y]:
        if(currentx>=len(area)):
            currentx=currentx%len(area) #if we hit the edge, we wrap around cause repeating patterns yo
        if(area[currentx] == '#'):
            tree+=1
        currentx+=x
    return tree

map = open("input_day3.txt","r").read().split('\n')

slopes=[(1,1),(3,1),(5,1),(7,1),(1,2)]
sum=1
for slope in slopes:
    sum*=CheckTrees(map,slope[0],slope[1])

print("part one: ", CheckTrees(map,3,1))
print("part two: ", sum)
