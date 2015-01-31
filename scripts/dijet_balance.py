import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left, bisect_right
from array import array
import random

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-p", "--period", action="store", default="BCD", dest="run_period")
parser.add_option("-v", "--verbosity", action="store", type=int, default=0, dest="verbosity")
parser.add_option("--pTbinlow", action="store", type=float, default=0, dest="pTbinlow")
parser.add_option("--pTbinhigh", action="store", type=float, default=0, dest="pTbinhigh")
(options, args) = parser.parse_args()
run_period  = options.run_period
verbosity   = options.verbosity
pTbinlow    = options.pTbinlow
pTbinhigh   = options.pTbinhigh
print "verbosity:", verbosity
print "pTbinlow:", pTbinlow
print "pTbinhigh:", pTbinhigh

res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])
eta_bins = np.arange(-3.5, 3.5, 0.25)
eta_binning = np.arange(0., 3.0, 0.5)
h = [[], [], [], []]

for eta in eta_bins:
	h[0].append(TH1F(str(eta), str(eta), 200, -2., 2.))
	h[1].append(TH1F(str(eta) + "HLT", str(eta) + "HLT", 200, -2., 2.))
	h[2].append(TH1F(str(eta) + "raw", str(eta) + "raw", 200, -2., 2.))
	h[3].append(TH1F(str(eta) + "rawHLT", str(eta) + "rawHLT", 200, -2., 2.))

def progressbar(progress):
	sys.stdout.write('\r['+int(progress)*'|'+'%'+str(2*progress)+(50-int(progress))*' '+']')
	sys.stdout.flush()

def RECO_2_HLT_Corr(recoJetEta, recoJetPt):
	recoJetEta = abs(recoJetEta)
	if recoJetEta < eta_binning[-1] and recoJetPt < res_bins[-1]:
		eta_bin    = bisect_left(eta_binning, recoJetEta)
		pt_Bin     = bisect_left(res_bins, recoJetPt)
		h_name     = 'ratio_' +str(eta_binning[eta_bin-1]) + '_' + str(eta_binning[eta_bin]) + '_' + str(int(res_bins[pt_Bin-1])) + '_' + str(int(res_bins[pt_Bin]))
		#print recoJetEta, h_name
		root_file  = TFile('ratio.root')
		if root_file.FindObjectAny(h_name):
			h_corr = root_file.FindObjectAny(h_name)
			if h_corr.GetEntries() > 10.:
				corr    = h_corr.GetMean()
			else:
				corr = 1.0
		else:
			corr = 1.0	
	else:
		corr = 1.0
	#print 'corr', corr
	return corr * recoJetPt

gROOT.ProcessLine(".X ~/setTDRStyle.C")
file_to_write = TFile('Corr_HLT_RECO_Balance' + run_period + '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)) +'.root', 'RECREATE')
#if working local
myfile  = TFile( 'test_Calo_Run' + run_period + '_latest.root' )
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DijetDataScouting/Data/test_Calo_Run'+ run_period +'.root' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries
entries = entries#20000

prof_balance1 = TProfile("Jet pT Balance with RECO", "Jet pT Balance RECO PROBE", 28, -3.5, 3.5, -1., 1.)
prof_balance2 = TProfile("Jet pT Balance with RECO vs HLT", "Jet pT Balance  HLT PROBE", 28, -3.5, 3.5, -1., 1.)
prof_balance3 = TProfile("Jet pT Balance with RECO (raw)", "Jet pT Balance RECO PROBE (raw)", 28, -3.5, 3.5, -1., 1.)
prof_balance4 = TProfile("Jet pT Balance with RECO vs HLT (raw)", "Jet pT Balance HLT PROBE (raw)", 28, -3.5, 3.5, -1., 1.)

prof_balance1.Sumw2()
prof_balance2.Sumw2()
prof_balance3.Sumw2()
prof_balance4.Sumw2()

for jentry in range(entries):
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
	minPtThreshold 	   = 200.#30.
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
	DeltaPhiRECO  = fabs(recoJetPhi[matchindex0]-recoJetPhi[matchindex1]) > TMath.Pi()/3.0
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
	
	#sufficient balance in the azimuthal plane (back-to-back: DeltaPhi_jj > 2.7)
	if abs(recoJetPhi[matchindex0] - recoJetPhi[matchindex1]) > 2.7 and soft_third_jet_reco: 

		if verbosity == 1:
			print "runNo:", runNo, "evtNo", evtNo,  "recoeta1:", recoJetEta[matchindex0], "recoeta2:", recoJetEta[matchindex1], "recopT1:", recoJetPt[matchindex0], "recopT2:", recoJetPt[matchindex1], "HLTpT1:", dsJetPt[0], "HLTpT2:", dsJetPt[1], "\n", "ratio1:", dsJetPt[0]/recoJetPt[matchindex0], "ratio2:", dsJetPt[1]/recoJetPt[matchindex1]

		if abs(recoJetEta[matchindex0]) < 0.25 and abs(recoJetEta[matchindex1]) > 0.25:
			ref_jet_pT    	  = recoJetPt[matchindex0]
			ref_jet_eta   	  = recoJetEta[matchindex0]
				
			probe_jet_pT  	  = recoJetPt[matchindex1]
			if verbosity == 1:
				print 'probe_jet_pT_before', probe_jet_pT
			probe_jet_eta 	  = recoJetEta[matchindex1]
			probe_jet_pT      = RECO_2_HLT_Corr(probe_jet_eta, probe_jet_pT)

			probe_jet_pT_HLT  = dsJetPt[1]
			probe_jet_eta_HLT = dsJetEta[1]

			if verbosity == 1:
				print 'probe_jet_pT', probe_jet_pT, 'probe_jet_pT_HLT', probe_jet_pT_HLT

			ref_jet_eta_raw 	  = recoJetEta[matchindex0]

			probe_jet_pT_raw  	  = recoJetRawPt[matchindex1]
			probe_jet_eta_raw 	  = recoJetEta[matchindex1]

			probe_jet_pT_HLT_raw  = dsJetRawPt[1]
			probe_jet_eta_HLT_raw = dsJetEta[1]

			if ref_jet_pT < pTbinhigh and ref_jet_pT > pTbinlow:
				balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
				prof_balance1.Fill(probe_jet_eta, balance1)
				h[0][bisect_right(eta_bins, probe_jet_eta) - 1].Fill(balance1)

				balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
				prof_balance2.Fill(probe_jet_eta, balance2)
				h[1][bisect_right(eta_bins, probe_jet_eta_HLT) - 1].Fill(balance2)

				balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
				prof_balance3.Fill(probe_jet_eta_raw, balance3)
				h[2][bisect_right(eta_bins, probe_jet_eta_raw) - 1].Fill(balance3)

				balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
				prof_balance4.Fill(probe_jet_eta_raw, balance4)
				h[3][bisect_right(eta_bins, probe_jet_eta_HLT_raw) - 1].Fill(balance4)
				if verbosity == 1:
					print "ref_jet_pT:", ref_jet_pT, "probe_jet_pT:", probe_jet_pT, "probe_jet_eta:", probe_jet_eta, "balance1:", balance1, "balance2:", balance2

		elif abs(recoJetEta[matchindex0]) > 0.25 and abs(recoJetEta[matchindex1]) < 0.25:
			
			ref_jet_pT    	  = recoJetPt[matchindex1]
			ref_jet_eta   	  = recoJetEta[matchindex1]
			
			probe_jet_pT  	  = recoJetPt[matchindex0]
			if verbosity == 1:
				print 'probe_jet_pT_before', probe_jet_pT
			probe_jet_eta 	  = recoJetEta[matchindex0]
			probe_jet_pT      = RECO_2_HLT_Corr(probe_jet_eta, probe_jet_pT)

			probe_jet_pT_HLT  = dsJetPt[0]
			probe_jet_eta_HLT = dsJetEta[0]

			if verbosity == 1:
				print 'probe_jet_pT', probe_jet_pT, 'probe_jet_pT_HLT', probe_jet_pT_HLT

			ref_jet_eta_raw  	  = recoJetEta[matchindex1]

			probe_jet_pT_raw  	  = recoJetRawPt[matchindex0]
			probe_jet_eta_raw 	  = recoJetEta[matchindex0]

			probe_jet_pT_HLT_raw  = dsJetRawPt[0]
			probe_jet_eta_HLT_raw = dsJetEta[0]

			if ref_jet_pT < pTbinhigh and ref_jet_pT > pTbinlow:

				balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
				prof_balance1.Fill(probe_jet_eta, balance1)
				h[0][bisect_right(eta_bins, probe_jet_eta) - 1].Fill(balance1)

				balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
				prof_balance2.Fill(probe_jet_eta, balance2)
				h[1][bisect_right(eta_bins, probe_jet_eta_HLT) - 1].Fill(balance2)

				balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
				prof_balance3.Fill(probe_jet_eta_raw, balance3)
				h[2][bisect_right(eta_bins, probe_jet_eta_raw) - 1].Fill(balance3)

				balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
				prof_balance4.Fill(probe_jet_eta_raw, balance4)
				h[3][bisect_right(eta_bins, probe_jet_eta_HLT_raw) - 1].Fill(balance4)
				if verbosity == 1:
					print "ref_jet_pT:", ref_jet_pT, "probe_jet_pT:", probe_jet_pT, "probe_jet_eta:", probe_jet_eta, "balance1:", balance1, "balance2:", balance2

		elif abs(recoJetEta[matchindex0]) < 0.25 and abs(recoJetEta[matchindex1]) < 0.25:

			if random.uniform(0., 1.) > 0.5: # if both jet are in the abs(eta)<0.25 region ref jet should be chosen randomly in order to eliminate the resolution bias.

				ref_jet_pT    	  = recoJetPt[matchindex1]
				ref_jet_eta   	  = recoJetEta[matchindex1]
				
				probe_jet_pT  	  = recoJetPt[matchindex0]
				if verbosity == 1:
					print 'probe_jet_pT_before', probe_jet_pT
				probe_jet_eta 	  = recoJetEta[matchindex0]
				probe_jet_pT      = RECO_2_HLT_Corr(probe_jet_eta, probe_jet_pT)

				probe_jet_pT_HLT  = dsJetPt[0]
				probe_jet_eta_HLT = dsJetEta[0]

				if verbosity == 1:
					print 'probe_jet_pT', probe_jet_pT, 'probe_jet_pT_HLT', probe_jet_pT_HLT

				ref_jet_eta_raw  	  = recoJetEta[matchindex1]

				probe_jet_pT_raw  	  = recoJetRawPt[matchindex0]
				probe_jet_eta_raw 	  = recoJetEta[matchindex0]

				probe_jet_pT_HLT_raw  = dsJetRawPt[0]
				probe_jet_eta_HLT_raw = dsJetEta[0]

				if ref_jet_pT < pTbinhigh and ref_jet_pT > pTbinlow:

					balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
					prof_balance1.Fill(probe_jet_eta, balance1)
					h[0][bisect_right(eta_bins, probe_jet_eta) - 1].Fill(balance1)

					balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
					prof_balance2.Fill(probe_jet_eta, balance2)
					h[1][bisect_right(eta_bins, probe_jet_eta_HLT) - 1].Fill(balance2)

					balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
					prof_balance3.Fill(probe_jet_eta_raw, balance3)
					h[2][bisect_right(eta_bins, probe_jet_eta_raw) - 1].Fill(balance3)

					balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
					prof_balance4.Fill(probe_jet_eta_raw, balance4)
					h[3][bisect_right(eta_bins, probe_jet_eta_HLT_raw) - 1].Fill(balance4)
					if verbosity == 1:
						print "ref_jet_pT:", ref_jet_pT, "probe_jet_pT:", probe_jet_pT, "probe_jet_eta:", probe_jet_eta, "balance1:", balance1, "balance2:", balance2

			else:
				ref_jet_pT    	  = recoJetPt[matchindex0]
				ref_jet_eta   	  = recoJetEta[matchindex0]
				
				probe_jet_pT  	  = recoJetPt[matchindex1]
				if verbosity == 1:
					print 'probe_jet_pT_before', probe_jet_pT
				probe_jet_eta 	  = recoJetEta[matchindex1]
				probe_jet_pT      = RECO_2_HLT_Corr(probe_jet_eta, probe_jet_pT)

				probe_jet_pT_HLT  = dsJetPt[1]
				probe_jet_eta_HLT = dsJetEta[1]

				if verbosity == 1:
					print 'probe_jet_pT', probe_jet_pT, 'probe_jet_pT_HLT', probe_jet_pT_HLT

				ref_jet_eta_raw  	  = recoJetEta[matchindex0]

				probe_jet_pT_raw  	  = recoJetRawPt[matchindex1]
				probe_jet_eta_raw 	  = recoJetEta[matchindex1]

				probe_jet_pT_HLT_raw  = dsJetRawPt[1]
				probe_jet_eta_HLT_raw = dsJetEta[1]

				if ref_jet_pT < pTbinhigh and ref_jet_pT > pTbinlow:

					balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
					prof_balance1.Fill(probe_jet_eta, balance1)
					h[0][bisect_right(eta_bins, probe_jet_eta) - 1].Fill(balance1)
					#print h[0][bisect_right(eta_bins, probe_jet_eta) - 1].GetName(), probe_jet_eta

					balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
					prof_balance2.Fill(probe_jet_eta, balance2)
					h[1][bisect_right(eta_bins, probe_jet_eta_HLT) - 1].Fill(balance2)

					balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
					prof_balance3.Fill(probe_jet_eta_raw, balance3)
					h[2][bisect_right(eta_bins, probe_jet_eta_raw) - 1].Fill(balance3)

					balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
					prof_balance4.Fill(probe_jet_eta_raw, balance4)
					h[3][bisect_right(eta_bins, probe_jet_eta_HLT_raw) - 1].Fill(balance4)
					if verbosity == 1:
						print "ref_jet_pT:", ref_jet_pT, "probe_jet_pT:", probe_jet_pT, "probe_jet_eta:", probe_jet_eta, "balance1:", balance1, "balance2:", balance2

if verbosity == 0:
	can1 = TCanvas("Corr_Canvas1"+ '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)), "Canvas1"+ '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)), 600, 800)
	pad1 =  TPad("pad1","pad1",0,0.3,1,1);
	pad1.SetBottomMargin(0)
	pad1.Draw()
	pad1.cd()
	gStyle.SetOptTitle(0)
	prof_balance1.SetLineColor(ROOT.kBlue + 2)
	prof_balance2.SetLineColor(ROOT.kRed  + 2)
	prof_balance1.SetMarkerColor(ROOT.kBlue + 2)
	prof_balance2.SetMarkerColor(ROOT.kRed  + 2)
	prof_balance1.GetXaxis().SetTitle("eta")
	prof_balance1.GetYaxis().SetTitle("#frac{probe_jet_pT - ref_jet_pT}{probe_jet_pT + ref_jet_pT}")
	prof_balance1.GetYaxis().CenterTitle()
	prof_balance1.GetXaxis().SetRangeUser(-3.5, 3.5)
	prof_balance2.GetXaxis().SetRangeUser(-3.5, 3.5)
	prof_balance1.GetYaxis().SetRangeUser(-0.1, 0.1)
	prof_balance2.GetYaxis().SetRangeUser(-0.1, 0.1)
	prof_balance1.Draw("hist e1")
	prof_balance2.Draw("hist e1 same")
	leg1 = pad1.BuildLegend(0.4, 0.67, 0.88, 0.88)
	leg1.SetFillColor(0)

	can1.cd()
	pad2 = TPad("pad2","pad2",0,0,1,0.3);
	pad2.SetTopMargin(0)
	pad2.SetBottomMargin(0.15)
	pad2.Draw()
	pad2.cd()
	h1 = prof_balance1.ProjectionX()
	h2 = prof_balance2.ProjectionX()
	h1.Sumw2()
	h2.Sumw2()
	h1.Divide(h2)
	h1.GetYaxis().SetRangeUser(-5, 5)
	h1.GetYaxis().SetTitle("ratio")
	h1.Draw("hist e1")

	can2 = TCanvas("Corr_Canvas2"+ '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)),"Canvas2"+ '_' + str(int(pTbinlow))+'_' + str(int(pTbinhigh)), 600, 800)
	pad3 =  TPad("pad3","pad3",0,0.3,1,1);
	pad3.SetBottomMargin(0)
	pad3.Draw()
	pad3.cd()
	gStyle.SetOptTitle(0)
	gStyle.SetOptTitle(0)
	prof_balance3.SetLineColor(ROOT.kBlue + 2)
	prof_balance4.SetLineColor(ROOT.kRed  + 2)
	prof_balance3.SetMarkerColor(ROOT.kBlue + 2)
	prof_balance4.SetMarkerColor(ROOT.kRed  + 2)
	prof_balance3.GetXaxis().SetTitle("eta")
	prof_balance3.GetYaxis().SetTitle("#frac{probe_jet_pT - ref_jet_pT}{probe_jet_pT + ref_jet_pT}")
	prof_balance3.GetYaxis().CenterTitle()
	prof_balance3.GetXaxis().SetRangeUser(-3.5, 3.5)
	prof_balance4.GetXaxis().SetRangeUser(-3.5, 3.5)
	prof_balance3.GetYaxis().SetRangeUser(-0.5, 0.5)
	prof_balance4.GetYaxis().SetRangeUser(-0.5, 0.5)
	prof_balance3.Draw("hist e1")
	prof_balance4.Draw("hist e1 same")
	leg2 = pad3.BuildLegend(0.4, 0.67, 0.88, 0.88)
	leg2.SetFillColor(0)

	can2.cd()
	pad4 = TPad("pad4","pad4",0,0,1,0.3);
	pad4.SetTopMargin(0)
	pad4.SetBottomMargin(0.15)
	pad4.Draw()
	pad4.cd()
	h3 = prof_balance3.ProjectionX()
	h4 = prof_balance4.ProjectionX()
	h3.Sumw2()
	h4.Sumw2()
	h3.Divide(h4)
	h3.GetYaxis().SetRangeUser(0, 2)
	h3.Draw("hist e1")

	file_to_write.cd()
	for h1 in h:
		for h2 in h1:
			h2.Write()

	prof_balance1.Write()
	prof_balance2.Write()
	prof_balance3.Write()
	prof_balance4.Write()

can1.SaveAs(can1.GetName()+".pdf")
can2.SaveAs(can2.GetName()+".pdf")

rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]