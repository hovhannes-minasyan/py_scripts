"""
Spilt the data three parts (80% - train.txt, 10% - val.txt, 10% - test.txt)
and store them in the languages/LANG_CODE/data/ folder.
"""

FILE_DIR = 'pre_final.txt'
TRAIN_DIR = open('translit-rnn/languages/hy-AM/data/train.txt', 'w')
VAL_DIR = open('translit-rnn/languages/hy-AM/data/val.txt', 'w')
TEST_DIR = open('translit-rnn/languages/hy-AM/data/test.txt', 'w')

ARR = []

with open(FILE_DIR, 'r') as ins:
    for line in ins:
        ARR.append(line)

for i in range(0, int(len(ARR)*0.8)):
    print>>TRAIN_DIR, ARR[i]


for i in range(int(len(ARR) * 0.8), int(len(ARR) * 0.9)):
    print>>VAL_DIR, ARR[i]

for i in range(int(len(ARR) * 0.9), len(ARR)):
    print>>TEST_DIR, ARR[i]
 