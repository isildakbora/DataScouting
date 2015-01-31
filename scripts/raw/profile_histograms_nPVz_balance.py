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


file0 = TFile("HLT_RECO_Comp_nPVz.root")
file0.cd()
dirList = gDirectory.GetListOfKeys()
can1 = []
can2 = []
h_balance = []

for eta in eta_bins[:-1]:
	canvas1 = TCanvas("balance_eta_" + str(int(eta)) + "_", "balance_eta_" + str(int(eta)) + "_", 11, 51, 600, 600)
	can1.append(canvas1)
	canvas2 = TCanvas("rms_balance_eta_" + str(int(eta)) + "_", "rms_balance_eta_" + str(int(eta)) + "_", 11, 51, 600, 300)
	can2.append(canvas2)
	gr_pT_vs_eta = []
	gr_pT_vs_eta_rms_per_mean = []
	legend = TLegend(0.6,0.7,0.9,0.9)
	h_balance.append(dirList[2].ReadObj())
	h_balance[-1].Reset()
	h_balance[-1].SetName("balance_" + str(eta) + str(eta + 0.5))
	h_balance[-1].SetTitle("balance_" + str(eta) + str(eta + 0.5))

	for nPVz in nPVzbins[:-1]:
		h  			 = []
		x  			 = array('d', [])
		ex 			 = array('d', [])
		mean_new 	 = array('d', [])
		RMS_new 	 = array('d', [])
		err_on_mean  = array('d', [])
		rms_per_mean = array('d', [])

		for i in xrange(len(res_bins) - 1):
			x.append(0.5 * (res_bins[i] + res_bins[i+1]))
			ex.append(0.5* (res_bins[i+1] - res_bins[i]))
		
		for i in xrange(len(res_bins)-1):
			h.append(dirList[2].ReadObj())
			h[i].Reset()

		for obj in dirList: 
			histo         = obj.ReadObj()
			print histo.GetName()
			is_raw		  = "resRawPt" in histo.GetName().split('_')
			is_balance	  = "balance"  in histo.GetName().split('_')
			nPVz_bin_low  = histo.GetName().split('_')[3]
			nPVz_bin_high = histo.GetName().split('_')[4]
			pT_bin_low    = histo.GetName().split('_')[5]
			pT_bin_high   = histo.GetName().split('_')[6]
			eta_bin_low   = histo.GetName().split('_')[7]
			eta_bin_high  = histo.GetName().split('_')[8]

			if  is_balance and (is_raw) and (float(eta_bin_low) == eta) and (int(nPVz) == int(nPVz_bin_low)):
				index = bisect_left(res_bins, float(pT_bin_low))
				h[index].Add(histo)
				h[index].SetName(histo.GetName())

			if  is_balance and (is_raw) and (float(eta_bin_low) == eta) and (int(nPVz) < 25):
				index_eta = bisect_left(eta_bins, float(eta_bin_low))
				h_balance[index_eta].Add(histo)


		for histo in h:
			#print histo.GetName()
			mean     = histo.GetMean()
			RMS      = histo.GetRMS()
			#histo.GetXaxis().SetRangeUser(mean - 3 * RMS, mean + 3 * RMS)
			mean_new.append(histo.GetMean())
			RMS_new.append(histo.GetRMS())
			err_on_mean.append(histo.GetMeanError())
			if mean_new[-1] != 0.:
				rms_per_mean.append(RMS_new[-1]/mean_new[-1])
			else:
				rms_per_mean.append(0.)
			
		gr_pT_vs_eta.append(TGraphErrors( len(x), x, mean_new, ex, err_on_mean ))
		gr_pT_vs_eta_rms_per_mean.append(TGraph( len(x), x, rms_per_mean ))

		gr_pT_vs_eta[-1].GetXaxis().SetTitle("pT [GeV]")
		gr_pT_vs_eta[-1].GetYaxis().SetTitle("dijet_balance")

		gr_pT_vs_eta[-1].GetYaxis().SetRangeUser(-0.5, 0.5)

		gr_pT_vs_eta[-1].SetMarkerColor( bisect_left(nPVzbins, nPVz)+1 )
		gr_pT_vs_eta[-1].SetMarkerStyle( 21 )
		legend.AddEntry(gr_pT_vs_eta[-1], "nPVzbins_"+str(nPVz)+'_'+ str(nPVzbins[bisect_left(nPVzbins, nPVz)+1]), "lp")

		gr_pT_vs_eta_rms_per_mean[-1].GetXaxis().SetTitle("pT")
		gr_pT_vs_eta_rms_per_mean[-1].GetYaxis().SetTitle("RMS/MEAN")

		gr_pT_vs_eta_rms_per_mean[-1].SetMarkerColor( bisect_left(nPVzbins, nPVz)+1 )
		gr_pT_vs_eta_rms_per_mean[-1].SetMarkerStyle( 21 )

		del h[:], x[:], ex[:], mean_new[:], RMS_new[:], rms_per_mean[:], err_on_mean[:]

	can1[-1].cd()
	gr_pT_vs_eta[0].SetTitle('dijet_balance_' + str(int(eta)) + '_' + str(int(eta_bins[bisect_left(eta_bins, eta)+1])))
	gr_pT_vs_eta[0].Draw('AP')
	for gr in gr_pT_vs_eta[1:]:
		gr.Draw('PSAME')
	legend.SetFillColor(ROOT.kWhite)
	legend.Draw("SAME")
	gr_pT_vs_eta[0].GetXaxis().SetRangeUser(0, 1500.)
	can1[-1].SaveAs( "dijet_balance_" + str(eta) + '.pdf')
	can1[-1].SaveAs( "dijet_balance_" + str(eta) + '.C')

	can2[-1].cd()
	gr_pT_vs_eta_rms_per_mean[0].SetTitle('dijet_balance_rms_per_mean' + str(int(eta)) + '_' + str(int(eta_bins[bisect_left(eta_bins, eta)+1])))
	gr_pT_vs_eta_rms_per_mean[0].Draw('AP')
	for gr in gr_pT_vs_eta_rms_per_mean[1:]:
		gr.Draw('PSAME')
	legend.SetFillColor(ROOT.kWhite)
	legend.Draw("SAME")
	gr_pT_vs_eta_rms_per_mean[0].GetXaxis().SetRangeUser(0, 1500.)
	can2[-1].SaveAs( "dijet_balance_rms_per_mean" + str(eta) + '_.pdf')
	can2[-1].SaveAs( "dijet_balance_rms_per_mean" + str(eta) + '_.C')
can = []
for h in h_balance:
	can.append(TCanvas(h.GetName(), h.GetName(), 600, 600))
	can[-1].cd()
	h.Draw()


#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]