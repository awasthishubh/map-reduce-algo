#!/usr/bin/env python
import sys
for line in sys.stdin:
	k,v=line.strip().split(',')
	if(v.isalpha() and v=='ABC'):
		print(k+'\t'+'000')
	if(v.isdigit()):
		print(k+'\t'+v)

