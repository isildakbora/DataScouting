import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left
from array import array
from setTDRStyle import setTDRStyle

gROOT.ProcessLine(".X ~/setTDRStyle.C")

eta_bins      = np.arange(0., 3.0, 0.5)
nPVzbins      = [0, 7, 15, 25]
res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])


file0 = TFile("HLT_RECO_pT_Comp_nPVz_pT.root")
file0.cd()
dirList = gDirectory.GetListOfKeys()
can = []

for eta in eta_bins[:-1]:
	
	canvas = TCanvas(str(eta), str(eta), 600, 600)
	can.append(canvas)
	gr_pT_vs_eta = []

	for nPVz in nPVzbins[:-1]:
		h  = []
		x  = array('d', [])
		ex = array('d', [])
		mean_new = array('d', [])
		RMS_new = array('d', [])

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
			pT_bin_low    = histo.GetName().split('_')[6]
			eta_bin_low   = histo.GetName().split('_')[7]
			eta_bin_high  = histo.GetName().split('_')[8]

			if  (not is_raw) and (float(eta_bin_low) == eta) and (int(nPVz) == int(nPVz_bin_low)):
				index = bisect_left(res_bins, float(pT_bin_low)) - 1
				h[index].Add(histo)
				h[index].SetName(histo.GetName())

		for histo in h:
			mean     = histo.GetMean()
			RMS      = histo.GetRMS()
			histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
			mean_new.append(histo.GetMean())
			RMS_new.append(histo.GetRMS())

		gr_pT_vs_eta.append(TGraphErrors( len(x), x, mean_new, ex, RMS_new ))

		gr_pT_vs_eta[-1].GetXaxis().SetTitle("pT [GeV]")
		gr_pT_vs_eta[-1].GetYaxis().SetTitle("p_{T}^{HLT}/p_{T}^{RECO}")

		gr_pT_vs_eta[-1].GetYaxis().SetRangeUser(0.90, 1.1)

		gr_pT_vs_eta[-1].SetMarkerColor( bisect_left(nPVzbins, nPVz)+1 )
		gr_pT_vs_eta[-1].SetMarkerStyle( 21 )	

		del h[:], x[:], ex[:], mean_new[:], RMS_new[:]

	can[-1].cd()
	print len(gr_pT_vs_eta)
	gr_pT_vs_eta[0].SetTitle('pT_vs_ratio_in_eta_' + str(eta) + '_' + str(eta_bins[bisect_left(eta_bins, eta)+1]))
	gr_pT_vs_eta[0].Draw('AP')
	for gr in gr_pT_vs_eta[1:]:
		gr.Draw('PSAME')

	can[-1].SaveAs( str(eta) + '_' + str(nPVz) + '.pdf')
	
 
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]