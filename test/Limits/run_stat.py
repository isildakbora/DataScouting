#!/usr/bin/env python
import os, sys

nJobs = 200
masspoints = [1000, 2000, 3000, 400]
for i in masspoints:
	for j in xrange(nJobs):
		print './stats_parallel ' + str(sys.argv[1])+ ' ' + str(i)+ ' '+ str(j)  + ' > log_'+str(i)+'_'+ str(sys.argv[1]) + '_' + str(j) + '.txt &'
		os.system('./stats_parallel ' + str(sys.argv[1])+ ' ' + str(i)+ ' '+ str(j) + ' > log_'+str(i)+'_'+ str(sys.argv[1]) + '_' + str(j) + '.txt &')

