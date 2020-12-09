

instructions = open("input_day8.txt","r").read().split("\n")



def iterate(instructions):
    acc=0
    current=0
    visited=list()
    infinite=False
    while(True):
        #print("visited: ",visited)
        #print("currently on: ", current)
        if(current==len(instructions)):
            break
        i = instructions[current]
        visited.append(current)
        instruction = i.split(' ')[0]
        operator = i.split(' ')[1][0]
        value = int(i.split(' ')[1][1:])


        if(instruction=="acc"):
            if(operator=='+'):
                acc+=value
            elif(operator=='-'):
                acc-=value
        elif(instruction=="jmp"):
            if(operator=='+'):
                if(current+value in visited):
                    #print("already been here!")
                    infinite=True
                    break
                else:
                    current+=value
            elif(operator=='-'):
                if(current-value in visited):
                    #print("already been here!")
                    infinite=True
                    break
                else:
                    current-=value
            continue
        #print(instruction,operator, value)
        current+=1
    return (infinite,acc)


#find all places where we jmp
jmpIndexes=list()
count=0
for i in instructions:
    if(i.split(' ')[0] == "jmp"):
        jmpIndexes.append(count)
    count+=1
nopIndexes=list()
count2=0
for i in instructions:
    if(i.split(' ')[0] == "nop"):
        nopIndexes.append(count2)
    count2+=1

for index in jmpIndexes:
    newInstructions = open("input_day8.txt","r").read().split("\n")
    oldValue = newInstructions[index].split(' ')[1]
    newInstructions[index] = "nop" + " " + oldValue
    print(iterate(newInstructions))
print("done with first")
for index in nopIndexes:
    newInstructions = open("input_day8.txt","r").read().split("\n")
    oldValue = newInstructions[index].split(' ')[1]
    newInstructions[index] = "jmp" + " " + oldValue
    print(iterate(newInstructions))












