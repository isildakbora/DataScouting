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

file_to_write = TFile(str(sys.argv[1])+"_ratio.root", "RECREATE")
file0 = TFile(str(sys.argv[1])+"_HLT_RECO_Comp_nPVz_test.root")
file0.cd()
dirList = gDirectory.GetListOfKeys()
can = []
can1d = []
for pT in res_bins[:-1]:
	h 			 = []
	x  			 = array('d', [])
	ex 			 = array('d', [])
	mean_new 	 = array('d', [])
	RMS_new 	 = array('d', [])
	err_on_mean  = array('d', [])
	
	for i in xrange(len(eta_bins) - 1):
		x.append(0.5 * (eta_bins[i] + eta_bins[i+1]))
		ex.append(0.5* (eta_bins[i+1] - eta_bins[i]))
	
	for i in xrange(len(eta_bins)-1):
		h.append(dirList[0].ReadObj())
		h[i].Reset()

	for obj in dirList: 
		histo         = obj.ReadObj()
		is_raw		  = "resRawPt" in histo.GetName().split('_')
		is_balance	  = "Balance"  in histo.GetName().split('_')
		nPVz_bin_low  = histo.GetName().split('_')[5]
		nPVz_bin_high = histo.GetName().split('_')[6]
		pT_bin_low    = histo.GetName().split('_')[7]
		pT_bin_high   = histo.GetName().split('_')[8]
		eta_bin_low   = histo.GetName().split('_')[9]
		eta_bin_high  = histo.GetName().split('_')[10]

		if (histo.GetName().split('_')[1] == 'resPt')  and float(pT_bin_low) == pT:
			index = bisect_left(eta_bins, float(eta_bin_low))
			print histo.GetName(), histo.GetEntries()
			h[index].Add(histo)
			h[index].SetName(histo.GetName())

			print h[index].GetName()

	file_to_write.cd()
	
	for histo in h:
		if histo.GetEntries() > 100.:
			can1d.append(TCanvas(str(histo.GetName().split('_')[9])+"_"+str(histo.GetName().split('_')[10])+"_"+str(int(pT)) + '_' + str(int(res_bins[bisect_left(res_bins, pT)+1])), str(histo.GetName().split('_')[9])+"_"+str(histo.GetName().split('_')[10])+"_"+str(int(pT)) + '_' + str(int(res_bins[bisect_left(res_bins, pT)+1])), 600, 600))
			mean     = histo.GetMean()
			RMS      = histo.GetRMS()	
			histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
			mean_new.append(histo.GetMean())
			RMS_new.append(histo.GetRMS())
			err_on_mean.append(histo.GetMeanError())
			can1d[-1].cd()
			histo.Draw()
			histo.SetName('ratio_' + can1d[-1].GetName())
			histo.Write()

	if len(mean_new) > 0:
		gr_pT_vs_eta = TGraphErrors( len(x), x, mean_new, ex, err_on_mean )
		gr_pT_vs_eta.SetTitle('eta_vs_ratio_in_pT_' + str(int(pT)) + '_' + str(int(res_bins[bisect_left(res_bins, pT)+1])))

		c_name = gr_pT_vs_eta.GetTitle()
		canvas = TCanvas(c_name, c_name, 600, 600)
		can.append(canvas)

		gr_pT_vs_eta.GetXaxis().SetTitle("eta [GeV]")
		gr_pT_vs_eta.GetYaxis().SetTitle("p_{T}^{HLT}/p_{T}^{RECO}")

		gr_pT_vs_eta.GetYaxis().SetRangeUser(0.90, 1.1)

		gr_pT_vs_eta.SetMarkerColor( 4 )
		gr_pT_vs_eta.SetMarkerStyle( 21 )
		gr_pT_vs_eta.Draw( 'AP' )

		can[-1].SaveAs(c_name + '_.pdf')
		can[-1].SaveAs(c_name + '_.C')
 
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]