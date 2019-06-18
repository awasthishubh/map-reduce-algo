#!/usr/bin/env python
import sys
lastK=''
lastV=0
true=False
for line in sys.stdin:
	k,v=line.strip().split('\t')
	if(k==lastK and not true):
		continue
	if(k==lastK and true):
		lastV+=int(v)
	else:
		if(true):
			print(lastK+','+str(lastV))
		lastK=k
		lastV=0
		if(v=='000'): true=True
		else: true=False
if(true):
	print(lastK+','+str(lastV))
