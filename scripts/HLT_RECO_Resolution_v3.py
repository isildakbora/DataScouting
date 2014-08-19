import ROOT, sys
from ROOT import *
from rootutils import *
import math, sys, numpy as np
from bisect import bisect_left
file_to_write = TFile('HLT_RECO_Smearing_Functions.root', 'RECREATE')
#if working local
myfile  = TFile( 'test_Calo.root' )
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DataScouting' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries

res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])
print res_bins

mass_points       = array('d')
mass_point_errors = np.zeros(len(res_bins)-1)
for i in range(len(res_bins)-1):
	mass_points.append(0.5*(res_bins[i]+res_bins[i+1]))

print mass_points, mass_point_errors

h_res    = []
res_func = []
#Set threshold values at which events are excluded
minPtThreshold = 30.
maxAbsEtaThreshold = 2.5
maxEtaSepThreshold = 2.0

for i in range(len(res_bins)-1):
	h_name = "h_res_" + str(int(res_bins[i])) + "_" + str(int(res_bins[i+1]))
	f_name = "f_res_" + str(int(res_bins[i])) + "_" + str(int(res_bins[i+1]))
	h = TH1F(h_name, h_name, 250, 0., 2.)
	h_res.append(h)

	total = TF1(f_name, "gaus(0)+gaus(3)+gaus(6)", 0., 2.0)
	total.SetParameter(1,1.)
	total.SetParameter(2,0.02)
	total.SetParameter(4,1.)
	total.SetParameter(5,0.02)
	total.SetParameter(8,1.)
	res_func.append(total)

print len(h_res), len(res_bins)-1

entries = entries/int(sys.argv[1])
for jentry in range(entries):
	ientry = mychain.LoadTree( jentry )
	progress = math.floor(50*jentry/entries)
	progressbar(progress)
	if ientry < 0:
		break

	nb = mychain.GetEntry( jentry )
	if nb <= 0:
		continue

	#if two jets exist
	nDSJets   = mychain.nDSJets
	nRECOJets = mychain.nRECOJets

	if nDSJets < 2 or nRECOJets < 2:
		continue
	recoJetpT  = array('d',(mychain.recoJetPt))
	recoJetE   = array('d',(mychain.recoJetE))
	recoJetEta = array('d',(mychain.recoJetEta))
	recoJetPhi = array('d',(mychain.recoJetPhi))

	dsJetPt    = array('d',(mychain.dsJetPt))
	dsJetE 	   = array('d',(mychain.dsJetE))
	dsJetEta   = array('d',(mychain.dsJetEta))
	dsJetPhi   = array('d',(mychain.dsJetPhi))

	dsJetMatchIndex   = array('d',(mychain.dsJetMatchIndex))
	dsJetFracHad   	  = array('d',(mychain.dsJetFracHad))
	dsJetFracEm   	  = array('d',(mychain.dsJetFracEm))
	recoJetFracHad    = array('d',(mychain.recoJetFracHad))
	recoJetFracEm     = array('d',(mychain.recoJetFracEm))

	# Filters
	#Dijet HLT Selection
	DeltaEtaHLT = fabs(dsJetEta[0]-dsJetEta[1]) < 1.3
	MaxAbsEtaThresholdHLT = fabs(dsJetEta[0]) < maxAbsEtaThreshold and fabs(dsJetEta[1]) < maxAbsEtaThreshold
	MinPtThresholdHLT     = dsJetPt[0] > minPtThreshold and dsJetPt[1] > minPtThreshold
	allHLTDijetSelection  =  DeltaEtaHLT and MinPtThresholdHLT and MaxAbsEtaThresholdHLT

	#Dijet RECO Selection
	matchindex0 = int(dsJetMatchIndex[0])
	matchindex1 = int(dsJetMatchIndex[1])

	if matchindex0 >=0 and matchindex1 >=0:
		DeltaEtaRECO           = fabs(recoJetEta[matchindex0]-recoJetEta[matchindex1]) < 1.3
		MinPtThresholdRECO     = recoJetpT[matchindex0] > minPtThreshold and recoJetpT[matchindex1] > minPtThreshold
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

	if allHLTDijetSelection and allRECODijetSelection:
		continue

	# CREATING WIDE-JET SYSTEM
	#########################################################################
	#For DS jets
	wDSjet1 = TLorentzVector(0.,0.,0.,0.)
	wDSjet2 = TLorentzVector(0.,0.,0.,0.)
	auxJet  = TLorentzVector(0.,0.,0.,0.)

	wDSjet1.SetPtEtaPhiE(dsJetPt[0],dsJetEta[0],dsJetPhi[0],dsJetE[0])
	wDSjet2.SetPtEtaPhiE(dsJetPt[1],dsJetEta[1],dsJetPhi[1],dsJetE[1])

	for i in xrange(2,nDSJets):
		auxJet.SetPtEtaPhiE(dsJetPt[i],dsJetEta[i],dsJetPhi[i],dsJetE[i])
		deltaR1 = auxJet.DeltaR(wDSjet1)
		deltaR2 = auxJet.DeltaR(wDSjet2)

		if deltaR1 < deltaR2 and deltaR1 < 1.1:
			wDSjet1 += auxJet
		elif deltaR2 < 1.1:
			wDSjet2 += auxJet

	# Reorder two wide-jets
	if wDSjet2.Pt() > wDSjet1.Pt():
		auxJet  = wDSjet2
		wDSjet2 = wDSjet1
		wDSjet1 = auxJet

    #For DS jets//
    #########################################################################
    #For RECO jets
	wRECOjet1 = TLorentzVector(0.,0.,0.,0.)
	wRECOjet2 = TLorentzVector(0.,0.,0.,0.)
	auxJet    = TLorentzVector(0.,0.,0.,0.)

	wRECOjet1.SetPtEtaPhiE(recoJetpT[0],recoJetEta[0],recoJetPhi[0],recoJetE[0])
	wRECOjet2.SetPtEtaPhiE(recoJetpT[1],recoJetEta[1],recoJetPhi[1],recoJetE[1])

	for i in xrange(2,nRECOJets):
		auxJet.SetPtEtaPhiE(recoJetpT[i],recoJetEta[i],recoJetPhi[i],recoJetE[i])
		deltaR1 = auxJet.DeltaR(wRECOjet1)
		deltaR2 = auxJet.DeltaR(wRECOjet2)

		if deltaR1 < deltaR2 and deltaR1 < 1.1:
			wRECOjet1 += auxJet
		elif deltaR2 < 1.1:
			wRECOjet2 += auxJet

	# Reorder two wide-jets
	if wRECOjet2.Pt() > wRECOjet1.Pt():
		auxJet  = wRECOjet2
		wRECOjet2 = wRECOjet1
		wRECOjet1 = auxJet

    #For RECO jets//
    #########################################################################

    #// Calculate dijet mass //
	reco_dijet_mass = (wRECOjet1 + wRECOjet2).M()
	ds_dijet_mass   = (wDSjet1   +   wDSjet2).M()
	
	index = bisect_left(res_bins, reco_dijet_mass)
	if index > 0 and index < len(res_bins):
		h_res[index-1].Fill(ds_dijet_mass / reco_dijet_mass)


mean      = array('d')
sigma     = array('d')
mean_err  = array('d')
sigma_err = array('d')

can      = []

for i in range(len(res_bins)-1):
	c_name = "c_res_" + str(int(res_bins[i])) + "_" + str(int(res_bins[i+1]))
	can.append(TCanvas(c_name, 600, 600))
	can[i].cd()

	for j in xrange(20):
		r  = h_res[i].Fit(res_func[i].GetName(), 'RQN+')
	r  = h_res[i].Fit(res_func[i].GetName(), 'SRQ+')

	if int(r) >= 0:
		mean.append(array('d', r.Parameters())[1])
		sigma.append(array('d', r.Parameters())[2])
		mean_err.append(r.ParError(1))
		sigma_err.append(r.ParError(2))

	h_res[i].SetMarkerStyle(20)
	h_res[i].SetDrawOption('E1][')
	gPad.SetLogy()
	can[i].Update()
print mean, mean_err, sigma

mean_graph = TGraphErrors(len(mean), mass_points, mean, mass_point_errors, mean_err)
sigma_graph = TGraphErrors(len(sigma), mass_points, sigma, mass_point_errors, sigma_err)

canMeangraph = TCanvas("mean graph","mean graph", 600, 600)
mean_graph.Draw('APZ')

canSigmagraph = TCanvas("sigma graph","sigma graph", 600, 600)
sigma_graph.Draw('APZ')

file_to_write.cd()
for i in xrange(len(h_res)):
	res_func[i].Write()
	h_res[i].Write()
	can[i].Write()

keepGUIalive()

print mass_points, mass_point_errors
