#
import sys
import re
import math
from collections import defaultdict
doc = 0
index = 0
arr = []
aktual = int(input())
for line in sys.stdin:
    doc += 1
    line = re.sub('[^a-zA-z]', ' ', line)
    # print (line)
    if(ord(line[0]) == ord('R')):
        index += 1
        arr.append(index/doc)
        # print (line)
# print (arr)
doc = sum(arr)
print("%.4f" % (doc/aktual))