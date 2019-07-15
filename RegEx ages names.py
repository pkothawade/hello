import re

exampleString = ''' Jessica is 15 years old, and Daniel is 27 years old. Edward is
                         40, and his grandfather is Oscar is 84. '''

ages = re.findall (r' \d{1,3}', exampleString)

names = re.findall (r' [A-Z][a-z]*', exampleString)

print(ages)
print(names)

# to get data into a dictionary

ageDict = {}
x = 0
for eachName in names:
     ageDict[eachName] = ages[x]
     x+=1
print(ageDict)
