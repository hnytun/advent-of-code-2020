

import string
import re
passports = open("input_day4.txt","r").read().split("\n\n")

def FieldsPresent(fields):
    if(len(fields) == 8):
        return True
    elif(len(fields) < 7):
        return False;
    elif(len(fields) == 7):
        cidMissing=True
        for field in fields:
            if("cid" in field):
                cidMissing=False
        return cidMissing



def FieldsValid(fields):
    allValid=True
    for field in fields:
        split = field.split(':')
        if(split[0]=="byr"):
            if(not (int(split[1])>=1920 and int(split[1]) <=2002 and len(split[1]) == 4)):
                #print("byr cant be: ", split[1])
                return False
        if(split[0] == "iyr"):
            if (not int(split[1])>=2010 and int(split[1]) <=2020 and len(split[1]) == 4):
                #print("iyr cant be: ", split[1])
                return False
        if(split[0] == "eyr"):
            if (not(int(split[1])>=2020 and int(split[1]) <=2030 and len(split[1]) == 4)):
                #print("eyr cant be: ", split[1])
                return False
        if(split[0] == "hgt"):
            if("cm" not in split[1] and "in" not in split[1]):
                #print("height doesnt have unit")
                return False
            if("cm" in split[1]):
                if(not(int(split[1].split('c')[0]) >= 150 and int(split[1].split('c')[0]) <= 193)):
                    #print("hgt cant be: ", split[1].split('c')[0], "cm")
                    return False
            elif("in" in split[1]):
                if(not(int(split[1].split('i')[0]) >= 59 and int(split[1].split('i')[0]) <= 76)):
                    #print("hgt cant be: ", split[1].split('i')[0], "in")
                    return False
        if(split[0] == "hcl"):
             pattern = re.compile("[a-f\d]+")
             if(not(split[1][0] == '#' and len(split[1])==7 and pattern.fullmatch(split[1][1:]) is not None)):
                #print("hcl cant be: ", split[1])
                return False
        if(split[0] == "ecl"):
            if(not(split[1] == "amb" or split[1] == "blu" or split[1] == "brn" or split[1] == "gry" or split[1] == "grn" or split[1] == "hzl" or split[1] == "oth")):
                #print("ecl cant be: ", split[1])
                return False
        if(split[0] == "pid"):
            if(not(len(split[1])==9 and all(c.isnumeric() for c in split[1]))):
                #print("pid cant be: ", split[1])
                return False


    return True


valid = 0
for passport in passports:
    fields=passport.split()
    if(FieldsPresent(fields) and FieldsValid(fields)):
        valid+=1

print(valid)




