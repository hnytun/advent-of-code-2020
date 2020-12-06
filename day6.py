
from collections import Counter


answers = open("input_day6.txt","r").read().split("\n\n")
sum=0
everybody=0
for i in answers:
    sum+=len(set(i.replace('\n','')))
    allAnswered=0
    uniquePersons = len(i.split('\n'))
    for wordCount in dict(Counter(i)).values():
        if(wordCount == uniquePersons):
            allAnswered+=1
    everybody+=allAnswered

print("part one: ", sum)
print("part two: ", everybody)






