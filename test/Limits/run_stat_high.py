#!/usr/bin/env python
import os, sys

#for i in [300, 400, 500, 600, 700, 800, 900, 1000]:
for i in [2000, 3000, 4000]:
	print './stats ' + str(sys.argv[1])+ ' ' + str(i) + ' > log_'+str(i)+'_'+ str(sys.argv[1])+ '.txt &'
	os.system('./stats ' + str(sys.argv[1])+ ' ' + str(i) + ' > log_'+str(i)+'_'+ str(sys.argv[1])+ '.txt &')

