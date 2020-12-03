

numbers = open("input_day1.txt","r").read().split('\n')
index=0
for num in numbers:
    for otherNum in numbers[index+1:]:
        if(int(num)+int(otherNum)==2020):
            print("first answer: ",int(num)*int(otherNum))
    index+=1

alreadyfound =list()
for a in numbers:
    for b in numbers:
        for c in numbers:
            if(int(a)+int(b)+int(c) == 2020 and int(a)*int(b)*int(c) not in alreadyfound):
                alreadyfound.append(int(a)*int(b)*int(c))

print("second answer: ",alreadyfound[0])
