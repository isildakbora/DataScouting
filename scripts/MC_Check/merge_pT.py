import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left
from array import array
from setTDRStyle import setTDRStyle

gROOT.ProcessLine(".X ~/setTDRStyle.C")

eta_bins      = np.arange(0., 3.0, 0.5)
nPVzbins      = array("d", [0, 7, 15, 25])
res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])

file_to_write = TFile("pt_dist.root", "RECREATE")
file0 = TFile("HLT_RECO_Comp_nPVz.root")
file0.cd()
dirList = gDirectory.GetListOfKeys()
can = []
can1d = []

for pT in res_bins[:-1]:

	h 			 = []

	for i in xrange(len(eta_bins)-1):
		h.append(file0.FindObjectAny('h_reco_pTBCD_0_7_0_200_0.0_0.5'))

	for obj in dirList: 
		histo         = obj.ReadObj()
		nPVz_bin_low  = histo.GetName().split('_')[3]
		nPVz_bin_high = histo.GetName().split('_')[4]
		pT_bin_low    = histo.GetName().split('_')[5]
		pT_bin_high   = histo.GetName().split('_')[6]
		eta_bin_low   = histo.GetName().split('_')[7]
		eta_bin_high  = histo.GetName().split('_')[8]
		
		if (histo.GetName().split('_')[1] == 'hlt') and float(pT_bin_low) == pT:
			index = bisect_left(eta_bins, float(eta_bin_low))

			#print histo.GetName(), histo.GetEntries()
			h[index].Add(histo)
			h[index].SetName(histo.GetName())
			#print h[index].GetName()

	file_to_write.cd()
		
	for histo in h:
		print histo.GetName()
		name = str(histo.GetName().split('_')[1]) + "_" + str(histo.GetName().split('_')[7])+"_"+str(histo.GetName().split('_')[8])+"_"+str(int(pT)) + '_' + str(int(res_bins[bisect_left(res_bins, pT)+1]))
		mean     = histo.GetMean()
		RMS      = histo.GetRMS()
		histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
		histo.SetName('pt_dist_' + name)
		histo.Write()
 
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]