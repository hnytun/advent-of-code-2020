
passes = open("input_day5.txt","r").read().split("\n")
def findrow(boarding):
    rows = list(range(0,128))
    columns = list(range(0,8))
    for action in boarding:
        if(action == 'F'):
            rows = rows[:len(rows)//2]
        if(action == 'B'):
            rows = rows[len(rows)//2:]
        if(action == 'L'):
            columns = columns[:len(columns)//2]
        if(action == 'R'):
            columns = columns[len(columns)//2:]

    return rows[0]*8+columns[0]

ids=list()
highest=0
for i in passes:
    if(findrow(i)>highest):
        highest=findrow(i)
print("highest id: ", highest)

for i in passes:
    ids.append(findrow(i))

ids.sort()
currentId=ids[0]-1
for i in ids:
    if(i-currentId != 1):
        print("missing id: ", i-1)
    currentId = i














