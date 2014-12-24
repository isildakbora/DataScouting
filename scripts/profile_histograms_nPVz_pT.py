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
can1 = []
can2 = []

for pT in res_bins[:-1]:
	canvas1 = TCanvas(str(pT), str(pT), 11, 51, 600, 600)
	can1.append(canvas1)
	canvas2 = TCanvas(str(pT)+"_", str(pT)+"_", 11, 51, 600, 300)
	can2.append(canvas2)
	gr_pT_vs_eta = []
	gr_pT_vs_eta_rms_per_mean = []
	legend = TLegend(0.6,0.7,0.9,0.9)

	for nPVz in nPVzbins[:-1]:
		h  			 = []
		x  			 = array('d', [])
		ex 			 = array('d', [])
		mean_new     = array('d', [])
		RMS_new      = array('d', [])
		err_on_mean  = array('d', [])
		rms_per_mean = array('d', [])

		for i in xrange(len(eta_bins) - 1):
			x.append(0.5 * (eta_bins[i] + eta_bins[i+1]))
			ex.append(0.5* (eta_bins[i+1] - eta_bins[i]))
		
		for i in xrange(len(eta_bins)-1):
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

			if  (not is_raw) and (float(pT_bin_low) == pT) and (int(nPVz) == int(nPVz_bin_low)):
				index = bisect_left(eta_bins, float(eta_bin_low))
				h[index].Add(histo)
				h[index].SetName(histo.GetName())

		for histo in h:
			print histo.GetName()
			mean     = histo.GetMean()
			RMS      = histo.GetRMS()
			histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
			mean_new.append(histo.GetMean())
			RMS_new.append(histo.GetRMS())
			err_on_mean.append(histo.GetMeanError())
			if mean_new[-1] != 0.:
				rms_per_mean.append(RMS_new[-1]/mean_new[-1])
			else:
				rms_per_mean.append(0.)
			print mean_new[-1]

		gr_pT_vs_eta.append(TGraphErrors( len(x), x, mean_new, ex, err_on_mean ))
		gr_pT_vs_eta_rms_per_mean.append(TGraph( len(x), x, rms_per_mean ))

		gr_pT_vs_eta[-1].GetXaxis().SetTitle("eta")
		gr_pT_vs_eta[-1].GetYaxis().SetTitle("p_{T}^{HLT}/p_{T}^{RECO}")

		gr_pT_vs_eta[-1].GetYaxis().SetRangeUser(0.90, 1.1)

		gr_pT_vs_eta[-1].SetMarkerColor( bisect_left(nPVzbins, nPVz)+1 )
		gr_pT_vs_eta[-1].SetMarkerStyle( 21 )
		legend.AddEntry(gr_pT_vs_eta[-1], "nPVzbins_"+str(nPVz)+'_'+ str(nPVzbins[bisect_left(nPVzbins, nPVz)+1]), "lp")

		gr_pT_vs_eta_rms_per_mean[-1].GetXaxis().SetTitle("eta")
		gr_pT_vs_eta_rms_per_mean[-1].GetYaxis().SetTitle("RMS/MEAN")


		gr_pT_vs_eta_rms_per_mean[-1].SetMarkerColor( bisect_left(nPVzbins, nPVz)+1 )
		gr_pT_vs_eta_rms_per_mean[-1].SetMarkerStyle( 21 )

		del h[:], x[:], ex[:], mean_new[:], RMS_new[:], rms_per_mean[:], err_on_mean[:]

	can1[-1].cd()
	print len(gr_pT_vs_eta)
	gr_pT_vs_eta[0].SetTitle('eta_vs_ratio_in_pT_' + str(pT) + '_' + str(res_bins[bisect_left(res_bins, pT)+1]))
	gr_pT_vs_eta[0].Draw('AP')
	
	for gr in gr_pT_vs_eta[1:]:
		gr.Draw('PSAME')
	legend.SetFillColor(ROOT.kWhite)
	legend.Draw("SAME")

	can2[-1].cd()
	gr_pT_vs_eta_rms_per_mean[0].Draw('AP')
	gr_pT_vs_eta_rms_per_mean[0].SetTitle('rms_per_mean_eta_vs_ratio_in_pT_' + str(pT) + '_' + str(res_bins[bisect_left(res_bins, pT)+1]))
	gr_pT_vs_eta_rms_per_mean[1].Draw('PSAME')
	gr_pT_vs_eta_rms_per_mean[2].Draw('PSAME')

	can1[-1].SaveAs( "pT_" + str(pT) + '.pdf')
	can2[-1].SaveAs( "rms_per_mean_pT_" + str(pT) + '.pdf')
	
 
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]