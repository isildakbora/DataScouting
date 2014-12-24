import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left
from array import array

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-p", "--period", action="store", default="BCD", dest="run_period")
parser.add_option("-w", "--useWideJets", action="store_true", default=False, dest="useWideJets")
parser.add_option("-y", "--etabinlow", action="store", type="str", dest="eta_bin_low")

(options, args) = parser.parse_args()

useWideJets = options.useWideJets
run_period  = options.run_period
eta_bin_low = options.eta_bin_low

print "useWideJets:", useWideJets, " period:", run_period

def progressbar(progress):
	sys.stdout.write('\r['+int(progress)*'|'+'%'+str(2*progress)+(50-int(progress))*' '+']')
	sys.stdout.flush()

file_to_write = TFile('HLT_RECO_nPVZ_'+ run_period +'.root', 'RECREATE')
#if working local
myfile  = TFile( 'test_Calo_Run' + run_period + '.root' )
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DijetDataScouting/Data/test_Calo_Run'+ run_period +'.root' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries

res_bins  = [0, 10, 25, 1000]
print res_bins

massBins = array('d', [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250,7500,7750,8000])

h_res      = []
#Set threshold values at which events are excluded
minPtThreshold = 30.
maxAbsEtaThreshold = 2.5
maxEtaSepThreshold = 2.0

for i in range(len(res_bins)-1):
	h_name = "h_Mjj_" + run_period + "_" + str(res_bins[i]) + "_" + str(res_bins[i+1])
	h = TH1F(h_name, h_name, len(massBins)-1 , massBins)
	h_res.append(h)

print len(h_res), len(res_bins)-1

entries = entries/1
for jentry in range(entries):
	ientry = mychain.LoadTree( jentry )
	#progressbar(math.floor(50*jentry/entries))
	if ientry < 0:
		break

	nb = mychain.GetEntry( jentry )
	if nb <= 0:
		continue

	#if two jets exist
	nDSJets   = mychain.nDSJets
	nRECOJets = mychain.nRECOJets
	nPVz      = mychain.nPVz

	if nDSJets < 2 or nRECOJets < 2:
		continue

	PVz 			  = array('d', (mychain.PVz))
	recoJetPt  	      = array('d',(mychain.recoJetPt))
	recoJetRawPt      = array('d',(mychain.recoJetRawPt))
	recoJetE   	      = array('d',(mychain.recoJetE))
	recoJetEta 	      = array('d',(mychain.recoJetEta))
	recoJetPhi 	      = array('d',(mychain.recoJetPhi))
	dsJetPt    	      = array('d',(mychain.dsJetPt))
	dsJetRawPt 	      = array('d',(mychain.dsJetRawPt))
	dsJetE 	   	      = array('d',(mychain.dsJetE))
	dsJetEta   	  	  = array('d',(mychain.dsJetEta))
	dsJetPhi   	      = array('d',(mychain.dsJetPhi))
	dsJetMatchIndex   = array('d',(mychain.dsJetMatchIndex))
	dsJetFracHad   	  = array('d',(mychain.dsJetFracHad))
	dsJetFracEm   	  = array('d',(mychain.dsJetFracEm))
	recoJetFracHad    = array('d',(mychain.recoJetFracHad))
	recoJetFracEm     = array('d',(mychain.recoJetFracEm))

	# Filters
	#Dijet HLT Selection
	DeltaEtaHLT           = fabs(dsJetEta[0]-dsJetEta[1]) < 1.3
	MaxAbsEtaThresholdHLT = fabs(dsJetEta[0]) < maxAbsEtaThreshold and fabs(dsJetEta[1]) < maxAbsEtaThreshold
	MinPtThresholdHLT     = dsJetPt[0] > minPtThreshold and dsJetPt[1] > minPtThreshold
	allHLTDijetSelection  = DeltaEtaHLT and MinPtThresholdHLT and MaxAbsEtaThresholdHLT

	#Dijet RECO Selection
	matchindex0 = int(dsJetMatchIndex[0])
	matchindex1 = int(dsJetMatchIndex[1])

	if matchindex0 >=0 and matchindex1 >=0:
		DeltaEtaRECO           = fabs(recoJetEta[matchindex0]-recoJetEta[matchindex1]) < 1.3
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
	MET_vs_METCleanFlag = mychain.dsMetPt != mychain.dsMetCleanPt
	dsJetID             = dsJetFracHad[0] < 0.95 and dsJetFracHad[1] < 0.95 and dsJetFracEm[0] < 0.95 and dsJetFracEm[1] < 0.95
	HLTFlagsGood        = dsJetID and MET_vs_METCleanFlag and DeltaPhiHLT

	if (not allHLTDijetSelection) and (not allRECODijetSelection):
		continue

	#For DS jets
	DSjet1 = TLorentzVector(0.,0.,0.,0.)
	DSjet2 = TLorentzVector(0.,0.,0.,0.)
	auxJet = TLorentzVector(0.,0.,0.,0.)

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
			auxJet  = DSjet2
			DSjet2 = DSjet1
			DSjet1 = auxJet

    #For DS jets//
    #########################################################################

    #For RECO jets
	RECOjet1 = TLorentzVector(0.,0.,0.,0.)
	RECOjet2 = TLorentzVector(0.,0.,0.,0.)
	auxJet   = TLorentzVector(0.,0.,0.,0.)

	RECOjet1.SetPtEtaPhiE(recoJetPt[matchindex0],recoJetEta[matchindex0],recoJetPhi[matchindex0],recoJetE[matchindex0])
	RECOjet2.SetPtEtaPhiE(recoJetPt[matchindex1],recoJetEta[matchindex1],recoJetPhi[matchindex1],recoJetE[matchindex1])

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

    #For RECO jets//
    #########################################################################

    #// Calculate dijet mass //
	reco_dijet_mass = (RECOjet1 + RECOjet2).M()
	ds_dijet_mass   = (DSjet1   +   DSjet2).M()

	index = bisect_left(res_bins, nPVz)
	#print nPVz, index, res_bins[index-1], res_bins[index]
	h_res[index-1].Fill(ds_dijet_mass)

file_to_write.cd()
h_res[0].SetMarkerColor(ROOT.kRed)
h_res[0].SetLineColor(ROOT.kRed)
h_res[0].Scale(1./h_res[0].Integral())
h_res[0].Draw()
h_res[0].Write()

h_res[1].Scale(1./h_res[1].Integral())
h_res[1].Draw('SAME')
h_res[1].SetMarkerColor(ROOT.kBlue)
h_res[1].SetLineColor(ROOT.kBlue)
h_res[1].Write()

h_res[2].Scale(1./h_res[2].Integral())
h_res[2].Draw('SAME')
h_res[2].SetMarkerColor(ROOT.kBlack)
h_res[2].SetLineColor(ROOT.kBlack)
h_res[2].Write()
#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]
