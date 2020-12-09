
numbers = open("input_day9.txt","r").read().split("\n")

subIndex=0
index=25
answer=0

while(index<len(numbers)):
    existsOne=False
    for i in numbers[subIndex:index]:
        for j in numbers[subIndex:index]:
            if(int(i)+int(j) == int(numbers[index])):
                existsOne=True
    if(not existsOne):
        answer=int(numbers[index])
    subIndex+=1
    index+=1


def findAnswer(answer,numbers):
    for i in range(0,1000):
        for j in range(1,1000):
            sum=0
            for num in numbers[i:j]:
                sum+=int(num)
            if(sum == answer):
                return (i,j)

indexes=findAnswer(answer,numbers)

smallest=int(numbers[indexes[0]:indexes[1]][0])
biggest=int(numbers[indexes[0]:indexes[1]][0])

for i in numbers[indexes[0]:indexes[1]]:
    if(int(i)<smallest):
        smallest=int(i)
    if(int(i)>biggest):
        biggest=int(i)


print("part one: ", answer)
print("part 2: ", smallest+biggest)







