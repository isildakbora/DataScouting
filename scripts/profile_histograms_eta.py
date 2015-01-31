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


file0 = TFile("HLT_RECO_Comp_nPVz_test.root")
file0.cd()
dirList = gDirectory.GetListOfKeys()
can = []

for eta in eta_bins[:-1]:
	h  = []
	x  = array('d', [])
	ex = array('d', [])
	mean_new = array('d', [])
	RMS_new = array('d', [])
	err_on_mean  = array('d', [])
	
	for i in xrange(len(res_bins) - 1):
		x.append(0.5 * (res_bins[i] + res_bins[i+1]))
		ex.append(0.5* (res_bins[i+1] - res_bins[i]))
	
	for i in xrange(len(res_bins)-1):
		h.append(dirList[0].ReadObj())
		h[i].Reset()

	for obj in dirList: 
		histo         = obj.ReadObj()
		is_raw		  = "resRawPt" in histo.GetName().split('_')
		nPVz_bin_low  = histo.GetName().split('_')[3]
		nPVz_bin_high = histo.GetName().split('_')[4]
		pT_bin_low    = histo.GetName().split('_')[5]
		pT_bin_high   = histo.GetName().split('_')[6]
		eta_bin_low   = histo.GetName().split('_')[7]
		eta_bin_high  = histo.GetName().split('_')[8]

		if (histo.GetName().split('_')[1] == 'resPt') and float(eta_bin_low) == eta:
			index = bisect_left(res_bins, float(pT_bin_low))
			print histo.GetName(), histo.GetEntries()
			h[index].Add(histo)
			h[index].SetName(histo.GetName())
			print h[index].GetName()

	for histo in h:
		if histo.GetEntries() > 100.:
			mean     = histo.GetMean()
			RMS      = histo.GetRMS()
			histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
			mean_new.append(histo.GetMean())
			RMS_new.append(histo.GetRMS())
			err_on_mean.append(histo.GetMeanError())
	  
	gr_pT_vs_eta = TGraphErrors( len(x), x, mean_new, ex, err_on_mean )

	gr_pT_vs_eta.SetTitle('pT_vs_ratio_in_eta_' + str(int(10*eta)) + '_' + str(int(10*eta_bins[bisect_left(eta_bins, eta)+1])))

	c_name = gr_pT_vs_eta.GetTitle()
	canvas = TCanvas(c_name, c_name, 600, 600)
	can.append(canvas)

	gr_pT_vs_eta.GetXaxis().SetTitle("pT [GeV]")
	gr_pT_vs_eta.GetYaxis().SetTitle("p_{T}^{HLT}/p_{T}^{RECO}")

	gr_pT_vs_eta.GetYaxis().SetRangeUser(0.90, 1.1)

	gr_pT_vs_eta.SetMarkerColor( 4 )
	gr_pT_vs_eta.SetMarkerStyle( 21 )
	gr_pT_vs_eta.Draw( 'AP' )

	can[-1].SaveAs(c_name + '.pdf')
	can[-1].SaveAs(c_name + '.C')

	del h[:], x[:], ex[:], mean_new[:], RMS_new[:]
 
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]