'''
Get the concatinated file and remove remaining HTML tags.
'''

ARR = []
KEEP = []
THE_FILE = open('pre_final.txt', 'w')
COUNT = 0

with open('test/concat.txt', 'r') as ins:
    for line in ins:
        ARR.append(line)

for i in range(0, len(ARR)):
    if ARR[i][0] == '<':
        ARR[i] = ''
        COUNT += 1
    else:
        pass


for line in ARR:
    if not line.isspace():
        KEEP.append(line)


for item in KEEP:
    print>>THE_FILE, item
