import sys
import random
import re

all_lines1 = list()
first_half=list()
all_lines2 = list()
second_half=list()
final=list()
f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
for line in f1:
    lines = line.split(". ")
    all_lines1.extend(lines)

for sentence in all_lines1:
    comma=sentence.find(", ")
    if(sentence[:comma+1]!=''):
        first_half.append(sentence[:comma+1])

random.shuffle(first_half)

print("now 2nd")
for line in f2:
    lines = line.split(". ")
    all_lines2.extend(lines)

for sentence in all_lines2:
    comma=sentence.find(", ")
    second_half.append(sentence[comma+1:])
# get rid of the period of the last sentence
second_half[len(second_half)-1]=second_half[len(second_half)-1][:-1]
random.shuffle(second_half)
print len(second_half)
print len(first_half)

for num in range(0,len(second_half)):
    final.append(first_half[num]+second_half[num]+'.')

for lines in final:
    print lines

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)
