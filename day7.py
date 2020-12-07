input = open("input_day7.txt","r").read().split("\n")
input_sample=open("input_day7_sample.txt","r").read().split("\n")



"""
produces a list of tuples on format (bag, map:what bag contains and how many it contains)
"""
def producemap(input):
    containerMaps = dict()
    for line in input:
        container = line.split("contain")[0][:-1]
        contents = line.split("contain")[1].split(",")
        map = dict()
        for content in contents:
            split = content.split(' ')
            if(split[1] == "no" and split[2] == "other"):
                continue
            number = split[1]
            type = (split[2] + " " + split[3] + " " + split[4]).replace(".","")
            if(type[-1] != 's'):
                type = type+'s'
            map[type] = number

        containerMaps[container] = map
    return containerMaps

"""
gets all containers that has a specific type of bag in them
"""




map = producemap(input_sample)

print("---------------------------------------------------------------------")
for p in map:
    print(p,map[p])
print("---------------------------------------------------------------------")


def findTarget(target,line,globalmap):

    if(globalmap[line]=={}):
        print("empty")
        return 0
    if(target in globalmap[line]):
        print("found it directly in", line)
        return 1
    else:
        for deeperline in globalmap[line]:
            print("looking deeper into ",deeperline)
            return findTarget(target,deeperline,map)



for m in map:
    findTarget("shiny gold bags",m,map)








