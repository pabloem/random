#import fileinput
import csv
import re
import ipdb
import os

exp = re.compile('([^_]*)_([0-9]*)-(log-test.*)')

files = dict()
#for line in fileinput.input():
for line in os.listdir('.'):
    line = line.strip()
    mch = exp.match(line)
    if not mch:
        print 'ERR: '+line
        continue
    label = mch.group(1)+' '+mch.group(2)
    if label not in files:
        files[label] = list()
    files[label].append(line)

#fileinput.close()

print 'Added files'

f = open('/home/pablo/codes/Kokiri_views/interfaces_new_qrys/csv/test_fail_history_inv.csv','r')
rdr = csv.reader(f)

TSTMP = 0
RUN_ID = 1
BBNUM = 2
PLATF = 9

interval = 0
for i,elm in enumerate(rdr):
    label = elm[PLATF]+' '+elm[BBNUM]
    if label not in files:
        interval += 1
        continue
    if label in files:
        if len(files[label]) == 0:
            print 'INFORMATION OF '+label+' is not reliable'
            continue
        print elm[RUN_ID]+': - '+files[label].pop(0)
    if interval > 0:
        print 'Skip '+str(interval)
        interval = 0
