import re
import sys

doc = dict()

n=int(input())
for inp in sys.stdin:
    for x in re.findall(r"[\w']+", inp.lower()):
        x = re.sub(r'[^\w\s]','', x)
        if x in doc:
            doc[x] = doc[x] + 1
        else:
	        doc[x] = 1

count = 0
for i in doc:
    if doc[i] > n:
	    count += 1
print(count)
