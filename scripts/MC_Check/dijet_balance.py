import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left, bisect_right
from array import array
import random

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-s", "--period",      action="store", default="RSGravitonToGG_M_300", dest="signal")
parser.add_option("-v", "--verbosity", action="store", type=int, default=0, dest="verbosity")
parser.add_option("--pTbinlow", action="store", type=float, default=0, dest="pTbinlow")
parser.add_option("--pTbinhigh", action="store", type=float, default=4000, dest="pTbinhigh")
parser.add_option("-w", "--useWideJets", action="store_true", default=False, dest="useWideJets")

(options, args) = parser.parse_args()
useWideJets = options.useWideJets
signal      = options.signal
verbosity   = options.verbosity
pTbinlow    = options.pTbinlow
pTbinhigh   = options.pTbinhigh
print "verbosity:", verbosity
print "pTbinlow:", pTbinlow
print "pTbinhigh:", pTbinhigh

gROOT.ProcessLine(".X ~/setTDRStyle.C")

massBins = array('d', [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250,7500,7750,8000])

res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])
eta_bins = np.arange(-3.5, 3.5, 0.25)
eta_binning = np.arange(0., 3.0, 0.5)

def progressbar(progress):
	sys.stdout.write('\r['+int(progress)*'|'+'%'+str(2*progress)+(50-int(progress))*' '+']')
	sys.stdout.flush()

def RECO_2_HLT_Corr(recoJetEta, recoJetPt, signal):
	recoJetEta = abs(recoJetEta)
	if recoJetEta < eta_binning[-1] and recoJetPt < res_bins[-1]:
		eta_bin    = bisect_left(eta_binning, recoJetEta)
		pt_Bin     = bisect_left(res_bins, recoJetPt)
		h_name     = 'ratio_' +str(eta_binning[eta_bin-1]) + '_' + str(eta_binning[eta_bin]) + '_' + str(int(res_bins[pt_Bin-1])) + '_' + str(int(res_bins[pt_Bin]))
		#print recoJetEta, h_name
		root_file  = TFile(signal+'_ratio.root')
		if root_file.FindObjectAny(h_name):
			h_corr = root_file.FindObjectAny(h_name)
			if h_corr.GetEntries() > 1.:
				corr    = h_corr.GetMean()
			else:
				corr = 1.0
		else:
			corr = 1.0	
	else:
		corr = 1.0
	#print "recoJetPt", recoJetPt,, "corr recoJetPt", corr*recoJetPt, "corr", corr
	return corr * recoJetPt

gROOT.ProcessLine(".X ~/setTDRStyle.C")
file_to_write = TFile('Corr_HLT_RECO_Balance' + signal + '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)) +'.root', 'RECREATE')
#if working local
myfile  = TFile( signal + '.root' )
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DijetDataScouting/Data/test_Calo_Run'+ run_period +'.root' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries
entries = entries#20000

h_reco_Mjj_corr = TH1F("h_reco_Mjj_corr", "h_reco_Mjj_corr", len(massBins)-1 , massBins)
h_ds_Mjj        = TH1F("h_ds_Mjj", "h_ds_Mjj", len(massBins)-1 , massBins)
h_reco_Mjj 	    = TH1F("h_reco_Mjj", "h_reco_Mjj", len(massBins)-1 , massBins)


for jentry in range(int(entries/2), entries):
	ientry = mychain.LoadTree( jentry )
	if verbosity == 0:
		progressbar(math.floor(50*jentry/entries))
	if ientry < 0:
		break

	nb = mychain.GetEntry( jentry )
	if nb <= 0:
		continue

	#if two jets exist
	runNo	  = mychain.runNo
	evtNo	  = mychain.evtNo
	nDSJets   = mychain.nDSJets
	nRECOJets = mychain.nRECOJets
	nPVz      = mychain.nPVz

	if nDSJets < 2 or nRECOJets < 2:
		continue
	
	PVz 			  = array('d', (mychain.PVz))
	recoJetPt  	      = array('d', (mychain.recoJetPt))
	recoJetRawPt      = array('d', (mychain.recoJetRawPt))
	recoJetE   	      = array('d', (mychain.recoJetE))
	recoJetEta 	      = array('d', (mychain.recoJetEta))
	recoJetPhi 	      = array('d', (mychain.recoJetPhi))
	dsJetPt    	      = array('d', (mychain.dsJetPt))
	dsJetRawPt 	      = array('d', (mychain.dsJetRawPt))
	dsJetE 	   	      = array('d', (mychain.dsJetE))
	dsJetEta   	  	  = array('d', (mychain.dsJetEta))
	dsJetPhi   	      = array('d', (mychain.dsJetPhi))
	dsJetMatchIndex   = array('d', (mychain.dsJetMatchIndex))
	dsJetFracHad   	  = array('d', (mychain.dsJetFracHad))
	dsJetFracEm   	  = array('d', (mychain.dsJetFracEm))
	recoJetFracHad    = array('d', (mychain.recoJetFracHad))
	recoJetFracEm     = array('d', (mychain.recoJetFracEm))

	# Filters
	#Set threshold values at which events are excluded
	minPtThreshold 	   = 30.#30.
	maxAbsEtaThreshold = 999. #2.5
	maxEtaSepThreshold = 0. #2.0
	deltaEtaCut        = 999. #1.3

	#Dijet HLT Selection
	DeltaEtaHLT           = fabs(dsJetEta[0]-dsJetEta[1]) < 1.3
	MaxAbsEtaThresholdHLT = fabs(dsJetEta[0]) < maxAbsEtaThreshold and fabs(dsJetEta[1]) < maxAbsEtaThreshold
	MinPtThresholdHLT     = dsJetPt[0] > minPtThreshold and dsJetPt[1] > minPtThreshold
	allHLTDijetSelection  = DeltaEtaHLT and MinPtThresholdHLT and MaxAbsEtaThresholdHLT

	#Dijet RECO Selection
	matchindex0 = int(dsJetMatchIndex[0])
	matchindex1 = int(dsJetMatchIndex[1])

	if matchindex0 >=0 and matchindex1 >=0:
		DeltaEtaRECO           = fabs(recoJetEta[matchindex0]-recoJetEta[matchindex1]) < deltaEtaCut
		MinPtThresholdRECO     = recoJetPt[matchindex0] > minPtThreshold and recoJetPt[matchindex1] > minPtThreshold
		MaxAbsEtaThresholdRECO = fabs(recoJetEta[matchindex0]) < maxAbsEtaThreshold and fabs(recoJetEta[matchindex1]) < maxAbsEtaThreshold
		recoJetID              = recoJetFracHad[matchindex0] < 0.95 and recoJetFracHad[matchindex1] < 0.95 and recoJetFracEm[matchindex0] < 0.95 and recoJetFracEm[matchindex1] < 0.95
		allRECODijetSelection  = DeltaEtaRECO and MinPtThresholdRECO and MaxAbsEtaThresholdRECO
	else:
		allRECODijetSelection = bool(0)

	#RECO Event Filters
	DeltaPhiRECO  = fabs(recoJetPhi[0]-recoJetPhi[1]) > TMath.Pi()/3.0
	RecoFlagsGood = DeltaPhiRECO and mychain.HBHENoiseFilterResultFlag and mychain.hcalLaserEventFilterFlag and mychain.eeBadScFilterFlag

	#Event Filter
	DeltaPhiHLT         = fabs(dsJetPhi[0]-dsJetPhi[1]) > TMath.Pi()/3.0
	if len(recoJetPt) > 2:
		soft_third_jet_reco = 0.1*((recoJetPt[0] + recoJetPt[1])/2) > recoJetPt[2]
	else:
		soft_third_jet_reco = False

	MET_vs_METCleanFlag = mychain.dsMetPt != mychain.dsMetCleanPt
	dsJetID             = dsJetFracHad[0] < 0.95 and dsJetFracHad[1] < 0.95 and dsJetFracEm[0] < 0.95 and dsJetFracEm[1] < 0.95
	HLTFlagsGood        = dsJetID and MET_vs_METCleanFlag and DeltaPhiHLT

	if (not allHLTDijetSelection) and (not allRECODijetSelection):
		continue

	#########################################################################
	#For DS jets
	DSjet1     = TLorentzVector(0.,0.,0.,0.)
	DSjet2 	   = TLorentzVector(0.,0.,0.,0.)
	auxJet     = TLorentzVector(0.,0.,0.,0.)

	DSjet1.SetPtEtaPhiE(dsJetPt[0],dsJetEta[0],dsJetPhi[0],dsJetE[0])
	DSjet2.SetPtEtaPhiE(dsJetPt[1],dsJetEta[1],dsJetPhi[1],dsJetE[1])

	if useWideJets:
		# CREATING WIDE-JET SYSTEM
		#########################################################################
		for i in xrange(2, nDSJets):
			auxJet.SetPtEtaPhiE(dsJetPt[i],dsJetEta[i],dsJetPhi[i],dsJetE[i])
			deltaR1 = auxJet.DeltaR(DSjet1)
			deltaR2 = auxJet.DeltaR(DSjet2)

			if deltaR1 < deltaR2 and deltaR1 < 1.1:
				DSjet1 += auxJet
			elif deltaR2 < 1.1:
				DSjet2 += auxJet

		# Reorder two wide-jets
		if DSjet2.Pt() > DSjet1.Pt():
			auxJet = DSjet2
			DSjet2 = DSjet1
			DSjet1 = auxJet

    #For DS jets//
    #########################################################################

	#########################################################################
    #For RECO jets
	RECOjet1      = TLorentzVector(0.,0.,0.,0.)
	RECOjet2      = TLorentzVector(0.,0.,0.,0.)
	RECOjet1_corr = TLorentzVector(0.,0.,0.,0.)
	RECOjet2_corr = TLorentzVector(0.,0.,0.,0.)
	auxJet        = TLorentzVector(0.,0.,0.,0.)

	RECOjet1.SetPtEtaPhiE(recoJetPt[0],recoJetEta[0],recoJetPhi[0],recoJetE[0])
	RECOjet2.SetPtEtaPhiE(recoJetPt[1],recoJetEta[1],recoJetPhi[1],recoJetE[1])

	if useWideJets:
		# CREATING WIDE-JET SYSTEM
		#########################################################################
		for i in xrange(2, nRECOJets):
			if i!=matchindex0 or i!=matchindex1:
				auxJet.SetPtEtaPhiE(recoJetPt[i],recoJetEta[i],recoJetPhi[i],recoJetE[i])
				deltaR1 = auxJet.DeltaR(RECOjet1)
				deltaR2 = auxJet.DeltaR(RECOjet2)

				if deltaR1 < deltaR2 and deltaR1 < 1.1:
					RECOjet1 += auxJet
				elif deltaR2 < 1.1:
					RECOjet2 += auxJet

		# Reorder two wide-jets
		if RECOjet2.Pt() > RECOjet1.Pt():
			auxJet  = RECOjet2
			RECOjet2 = RECOjet1
			RECOjet1 = auxJet


	corr0 = RECO_2_HLT_Corr(recoJetEta[0], recoJetPt[0], signal) / recoJetPt[0]
	corr1 = RECO_2_HLT_Corr(recoJetEta[1], recoJetPt[1], signal) / recoJetPt[1]

	RECOjet1_corr.SetPtEtaPhiE(corr0 * recoJetPt[0], recoJetEta[0], recoJetPhi[0], corr0 * recoJetE[0])
	RECOjet2_corr.SetPtEtaPhiE(corr1 * recoJetPt[1], recoJetEta[1], recoJetPhi[1], corr1 * recoJetE[1])
    #For RECO jets//
    #########################################################################

    #########################################################################
    #// Calculate dijet mass //
	reco_dijet_mass      = (RECOjet1      + RECOjet2).M()
	reco_dijet_mass_corr = (RECOjet1_corr + RECOjet2_corr).M()
	ds_dijet_mass        = (DSjet1        + DSjet2).M()
	h_reco_Mjj.Fill(reco_dijet_mass)
	h_reco_Mjj_corr.Fill(reco_dijet_mass_corr)
	h_ds_Mjj.Fill(ds_dijet_mass)
    #// Calculate dijet mass //
    #########################################################################

canvas = TCanvas(signal, signal, 600, 910)
pad1 =  TPad("pad1","pad1",0,0.3,1,1)
pad1.SetBottomMargin(0)
#pad1.SetLogx()
#pad1.SetLogy()
pad1.SetGridx()
pad1.SetGridy()
pad1.Draw()
pad1.cd()
gStyle.SetOptTitle(1)
h_reco_Mjj.GetXaxis().SetRangeUser(0., 2000.)
h_reco_Mjj.GetYaxis().SetTitle("# of Events")
h_reco_Mjj.SetLineColor(ROOT.kRed)
h_reco_Mjj.SetLineWidth(2)
h_reco_Mjj.Draw()
h_reco_Mjj_corr.SetLineColor(ROOT.kBlue)
h_reco_Mjj_corr.SetLineWidth(2)
h_reco_Mjj_corr.Draw("SAME")	
h_ds_Mjj.GetXaxis().SetRangeUser(0., 2000.)
h_ds_Mjj.SetLineColor(ROOT.kBlack)
h_ds_Mjj.SetLineWidth(2)
h_ds_Mjj.Draw("SAME")
h_reco_Mjj.GetYaxis().CenterTitle()

leg1 = pad1.BuildLegend(0.6, 0.67, 0.88, 0.88)
leg1.SetFillColor(0)
leg1.Draw("SAME")

title = ROOT.TPaveText(0.1, 0.95, 0.6, 0.99, 'NDC')
title.SetFillColor(ROOT.kWhite)
title.SetFillStyle(0)
title.SetBorderSize(0)
title.AddText(signal)
title.Draw()

canvas.cd()

gStyle.SetOptTitle(0)
pad2 = TPad("pad2","pad2",0,0,1,0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.35)
#pad2.SetLogx()
pad2.SetGridx()
pad2.SetGridy()
pad2.Draw()
pad2.cd()

ratio_reco_ds = h_reco_Mjj.Clone("ratio_reco_ds")
ratio_reco_ds.SetLineColor(ROOT.kRed)
ratio_ds_reco_corr = h_reco_Mjj_corr.Clone("ratio_ds_reco_corr")
ratio_ds_reco_corr.SetLineColor(ROOT.kBlue)

ratio_reco_ds.Divide(h_ds_Mjj)
ratio_ds_reco_corr.Divide(h_ds_Mjj)
ratio_reco_ds.SetTitle("ratio_reco_ds")
ratio_ds_reco_corr.SetTitle("ratio_reco_corr_ds")

ratio_reco_ds.GetYaxis().SetTitle("Ratio")
ratio_reco_ds.Draw()
ratio_ds_reco_corr.Draw("SAME")
legend = TLegend(0.6,0.4,0.9,0.6)
legend.SetFillColor(ROOT.kWhite)
legend.AddEntry(ratio_reco_ds)
legend.AddEntry(ratio_ds_reco_corr)
legend.Draw("SAME")
ratio_reco_ds.GetYaxis().CenterTitle()
ratio_reco_ds.GetYaxis().SetTitleSize(0.05)
ratio_reco_ds.GetYaxis().SetRangeUser(0., 1.5)
ratio_reco_ds.GetXaxis().SetTitle("M_{jj} [GeV]")
ratio_reco_ds.GetXaxis().SetTitleSize(0.12)
ratio_reco_ds.GetXaxis().SetLabelSize(0.09)
ratio_reco_ds.GetYaxis().SetTitleSize(0.1)
ratio_reco_ds.GetYaxis().SetTitleOffset(0.5)

l = TLine(0.,1,2000,1)
l.SetLineColor(kBlack)
l.SetLineStyle(2)
l.SetLineWidth(2)
l.Draw("SAME")

canvas.SaveAs(signal+'_MC_correction.pdf')

file_to_write.cd()
h_reco_Mjj.Write()
h_reco_Mjj_corr.Write()
h_ds_Mjj.Write()

file_to_write.Close()
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]