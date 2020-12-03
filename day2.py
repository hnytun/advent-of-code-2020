
amtvalid=0
amtvalid2=0
for line in open("input_day2.txt","r").read().split('\n'):
    minmax=line.split(' ')[0]
    min=int(minmax.split('-')[0])
    max=int(minmax.split('-')[1])
    letter=line.split(':')[0].split(' ')[1]
    word=line.split(' ')[2]
    correctCount=0
    if(word[min-1] == letter):
        correctCount+=1
    if(word[max-1] == letter):
        correctCount+=1
    if(correctCount==1):
        amtvalid2+=1
    if(word.count(letter) >= min and word.count(letter) <=max):
        amtvalid+=1
print("amount of valid passwords (part one): ", amtvalid)
print("amount of valid passwords (part two): ", amtvalid2)
