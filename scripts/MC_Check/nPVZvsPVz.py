import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left
from array import array

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-p", "--period", action="store", default="BCD", dest="run_period")
parser.add_option("-y", "--etabinlow", action="store", type="str", dest="eta_bin_low",)

(options, args) = parser.parse_args()

run_period  = options.run_period
eta_bin_low = options.eta_bin_low

def progressbar(progress):
	sys.stdout.write('\r['+int(progress)*'|'+'%'+str(2*progress)+(50-int(progress))*' '+']')
	sys.stdout.flush()

file_to_write = TFile('HLT_RECO_PVz' + run_period +'.root', 'RECREATE')
#if working local
myfile  = TFile( 'test_Calo_Run' + run_period + '.root' )
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DijetDataScouting/Data/test_Calo_Run'+ run_period +'.root' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries

h_nPVZ_0_10      = TH1F('nPVZ_0_10',     'nPVZ_0_10'    , 600, -30., 30.)
h_nPVZ_10_25     = TH1F('nPVZ_10_25',    'nPVZ_10_25'   , 600, -30., 30.)
h_nPVZ_25_inf    = TH1F('h_nPVZ_25_inf', 'h_nPVZ_25_inf', 600, -30., 30.)

entries = entries

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
	#Set threshold values at which events are excluded
	minPtThreshold = 30.
	maxAbsEtaThreshold = 2.5
	maxEtaSepThreshold = 2.0

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

	if nPVz < 11:
		for i in xrange(nPVz):
			h_nPVZ_0_10.Fill(PVz[i])

	elif nPVz > 10 and nPVz < 26:
		for i in xrange(nPVz):
			h_nPVZ_10_25.Fill(PVz[i])

	else:
		for i in xrange(nPVz):
			h_nPVZ_25_inf.Fill(PVz[i])

can1 = TCanvas('nPVZ_0_10', 'nPVZ_0_10', 600, 600)
h_nPVZ_0_10.Draw()

can2 = TCanvas('nPVZ_10_25', 'nPVZ_10_25', 600, 600)
h_nPVZ_10_25.Draw()

can3 = TCanvas('nPVZ_25_inf', 'nPVZ_25_inf', 600, 600)
h_nPVZ_25_inf.Draw()

rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]