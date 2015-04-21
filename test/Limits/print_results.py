#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import os, sys
import numpy
from array import *
from scipy.stats.mstats import mquantiles

#######################################################
def getQuantiles(limits, median, onesigma, twosigma_):
  nit=len(limits)
  if nit==0:
    return

    # sort the array wrt limits
  limits = sorted(limits)

  # median for the expected limit
  median.append(numpy.median(numpy.array(limits)))

  #quantiles for the expected limit bands
  prob    = array('d',[]) # array with quantile boundaries
  prob.append(0.021)
  prob.append(0.159)
  prob.append(0.841)
  prob.append(0.979)

  # array for the results

  #quantiles = array('d',[])
  #TMath.Quantiles(nit, 4, limits, quantiles, prob) # evaluate quantiles
  quantiles   = mquantiles(limits, prob)

  onesigma.append(quantiles[1])
  onesigma.append(quantiles[2])
  twosigma.append(quantiles[0])
  twosigma.append(quantiles[3])
  return
#######################################################

nJobs = 200
masspoints = int(sys.argv[2])	

expectedLowerBound = array('d',[])
expectedUpperBound = array('d',[])
observedLowerBound = array('d',[])
observedUpperBound = array('d',[])

for i in xrange(nJobs):
  print i
  log_file    = open('log_'+str(masspoints)+'_'+ str(sys.argv[1]) + '_' + str(i) + '.txt','r')
  outputlines = log_file.readlines()
  for line in outputlines:
    if re.search("observedLowerBound:", line):
      observedLowerBound = float(line.split()[1])
      observedUpperBound = float(line.split()[3])

      for line in outputlines:
        if re.search("expectedLowerBound:", line):
          expectedLowerBound.append(float(line.split()[1]))
          expectedUpperBound.append(float(line.split()[3]))
  log_file.close()


for i in xrange(len(expectedLowerBound)):
  print "expected bound(" + str(i+1) + ") = [ " + str(expectedLowerBound[i]) + " , " + str(expectedUpperBound[i]) + " ]\n"

print "***** observed bounds *****\n"
print "observed bound = [ " + str(observedLowerBound) + " , " + str(observedUpperBound) + " ]\n"

print "***** expected upper bounds *****\n"

median   = []
onesigma = []
twosigma = []

getQuantiles(expectedUpperBound, median, onesigma, twosigma);
print "median: " + str(median[0]) + "\n"
print "+/-1 sigma band: [ " + str(onesigma[0]) + " , " + str(onesigma[1]) + " ]\n"
print "+/-2 sigma band: [ " + str(twosigma[0]) + " , " + str(twosigma[1]) + " ]\n"
