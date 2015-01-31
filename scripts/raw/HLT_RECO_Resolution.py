import ROOT, sys, getopt
from ROOT import *
import math, sys, numpy as np
from bisect import bisect_left
from array import array
import random

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)
parser.add_option("-p", "--period",      action="store",      default="BCD", dest="run_period")
parser.add_option("-w", "--useWideJets", action="store_true", default=False, dest="useWideJets")

(options, args) = parser.parse_args()

useWideJets = options.useWideJets
run_period  = options.run_period

eta_bins    = np.arange(0.0, 3.0, 0.5)
nPVzbins    = [0, 7, 15, 2500]
scale       = 1

res_bins_low  = np.arange(0., 1400., 200.)
res_bins_high = np.arange(1400., 4500., 500.)
res_bins      = np.concatenate([res_bins_low, res_bins_high])
#res_bins       = array('i', [2400, 2900])
print res_bins

def progressbar(progress):
	sys.stdout.write('\r['+int(progress)*'|'+'%'+str(2*progress)+(50-int(progress))*' '+']')
	sys.stdout.flush()

#file_to_write = TFile('HLT_RECO_pT_Comp_nPVz_pT_'+str(res_bins[0]).replace('.', '')+'_'+str(res_bins[1]).replace('.', '')+'.root', 'RECREATE')
file_to_write = TFile('HLT_RECO_Comp_nPVz.root', 'RECREATE')
#if working local
myfile  = TFile( 'test_Calo_Run' + run_period + '_latest.root' )
print myfile.GetName()
#if working in lxplus
#myfile  = TFile( '/afs/cern.ch/user/i/isildak/public/DijetDataScouting/Data/test_Calo_Run'+ run_period +'.root' )
mychain = gDirectory.Get( 'DSComp' )
entries = mychain.GetEntriesFast()
print entries

mass_points       = array('d')
mass_point_errors = np.zeros(len(res_bins)-1)
for i in range(len(res_bins)-1):
	mass_points.append(0.5*(res_bins[i]+res_bins[i+1]))

print mass_points, mass_point_errors

h_res         = []
h_resPt       = []
h_resRawPt 	  = []
res_func   	  = []
h_balance     = []
h_balance_raw = []
h_balance_HLT     = []
h_balance_HLT_raw = []

#Set threshold values at which events are excluded
minPtThreshold = 30.
maxAbsEtaThreshold = 2.5
maxEtaSepThreshold = 2.0


for k in range(len(eta_bins)-1):
	for j in range(len(nPVzbins)-1):
		for i in range(len(res_bins)-1):
			common_suffixes    = run_period + "_" + str(nPVzbins[j]) + '_' + str(nPVzbins[j+1]) + '_' + str(int(res_bins[i])) + "_" + str(int(res_bins[i+1])) + "_" + str(eta_bins[k]) + "_" + str(eta_bins[k+1])
			h_name = "h_res_" + common_suffixes
			f_name = "f_res_" + common_suffixes
			print "k =", k, " j =", j, " i =", i, " global =", i + j * (len(res_bins)-1) + k * (len(nPVzbins)-1) * (len(res_bins)-1), " h_name:", h_name 
			#h = TH1F(h_name, h_name, 250, 0., 2.)
			#h_res.append(h)

			h_name = "h_resPt_" + common_suffixes
			h = TH1F(h_name, h_name, 250, 0., 2.)
			h_resPt.append(h)

			h_name = "h_resRawPt_" + common_suffixes
			h = TH1F(h_name, h_name, 250, 0., 2.)
			h_resRawPt.append(h)

			h_name = "h_balance_" + common_suffixes
			h = TH1F(h_name, h_name, 200, -1., 1.)
			h_balance.append(h)

			h_name = "h_balanceRaw_" + common_suffixes
			h = TH1F(h_name, h_name, 200, -1., 1.)
			h_balance_raw.append(h)

			h_name = "h_balanceHLT_" + common_suffixes
			h = TH1F(h_name, h_name, 200, -1., 1.)
			h_balance_HLT.append(h)

			h_name = "h_balanceRawHLT_" + common_suffixes
			h = TH1F(h_name, h_name, 200, -1., 1.)
			h_balance_HLT_raw.append(h)

print len(h_res), len(res_bins)-1

entries = entries/scale

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

	PVz 			  = array('d',(mychain.PVz))
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
	DeltaPhiRECO  = fabs(recoJetPhi[matchindex0]-recoJetPhi[matchindex1]) > TMath.Pi()/3.0
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

	residue = 1
	indexi0 = bisect_left(res_bins, recoJetPt[matchindex0]) - residue
	indexi1 = bisect_left(res_bins, recoJetPt[matchindex1]) - residue

	indexk0 = bisect_left(eta_bins, abs(recoJetEta[matchindex0])) - residue
	indexk1 = bisect_left(eta_bins, abs(recoJetEta[matchindex1])) - residue

	indexj  = bisect_left(nPVzbins, nPVz) - residue

	#  print len(h_resPt)
	# print res_bins
	# print eta_bins
	# print nPVzbins
	if len(recoJetPt) > 2:
		soft_third_jet_reco = 0.1*((recoJetPt[0] + recoJetPt[1])/2) > recoJetPt[2]
	else:
		soft_third_jet_reco = False

	#sufficient balance in the azimuthal plane (back-to-back: DeltaPhi_jj > 2.7)
	if abs(recoJetPhi[matchindex0] - recoJetPhi[matchindex1]) > 2.7 and soft_third_jet_reco: 

		if abs(recoJetEta[matchindex0]) < 0.25 and abs(recoJetEta[matchindex1]) > 0.25:
			ref_jet_pT    	  = recoJetPt[matchindex0]
			ref_jet_eta   	  = recoJetEta[matchindex0]

			probe_jet_pT  	  = recoJetPt[matchindex1]
			probe_jet_eta 	  = recoJetEta[matchindex1]

			probe_jet_pT_HLT  = dsJetPt[1]
			probe_jet_eta_HLT = dsJetEta[1]

			ref_jet_eta_raw 	  = recoJetEta[matchindex0]

			probe_jet_pT_raw  	  = recoJetRawPt[matchindex1]
			probe_jet_eta_raw 	  = recoJetEta[matchindex1]

			probe_jet_pT_HLT_raw  = dsJetRawPt[1]
			probe_jet_eta_HLT_raw = dsJetEta[1]

			balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
			balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
			balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
			balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
			balance_index = (bisect_left(res_bins, probe_jet_pT) - residue) + (bisect_left(nPVzbins, nPVz) - residue) * (len(res_bins) - 1) + (bisect_left(eta_bins, abs(probe_jet_eta)) - residue) * (len(res_bins) - 1) * (len(nPVzbins) - 1)
			if balance_index > -1 and balance_index < len(h_balance):
				h_balance[balance_index].Fill(balance1)
				h_balance_HLT[balance_index].Fill(balance2)
				h_balance_raw[balance_index].Fill(balance3)
				h_balance_HLT_raw[balance_index].Fill(balance4)

		elif abs(recoJetEta[matchindex0]) > 0.25 and abs(recoJetEta[matchindex1]) < 0.25:
			
			ref_jet_pT    	  = recoJetPt[matchindex1]
			ref_jet_eta   	  = recoJetEta[matchindex1]
			
			probe_jet_pT  	  = recoJetPt[matchindex0]
			probe_jet_eta 	  = recoJetEta[matchindex0]

			probe_jet_pT_HLT  = dsJetPt[0]
			probe_jet_eta_HLT = dsJetEta[0]

			ref_jet_eta_raw  	  = recoJetEta[matchindex1]

			probe_jet_pT_raw  	  = recoJetRawPt[matchindex0]
			probe_jet_eta_raw 	  = recoJetEta[matchindex0]

			probe_jet_pT_HLT_raw  = dsJetRawPt[0]
			probe_jet_eta_HLT_raw = dsJetEta[0]

			balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
			balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
			balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
			balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
			balance_index = (bisect_left(res_bins, probe_jet_pT) - residue) + (bisect_left(nPVzbins, nPVz) - residue) * (len(res_bins) - 1) + (bisect_left(eta_bins, abs(probe_jet_eta)) - residue) * (len(res_bins) - 1) * (len(nPVzbins) - 1)
			if balance_index > -1 and balance_index < len(h_balance):
				h_balance[balance_index].Fill(balance1)
				h_balance_HLT[balance_index].Fill(balance2)
				h_balance_raw[balance_index].Fill(balance3)
				h_balance_HLT_raw[balance_index].Fill(balance4)

		elif abs(recoJetEta[matchindex0]) < 0.25 and abs(recoJetEta[matchindex1]) < 0.25:

			if random.uniform(0., 1.) > 0.5: # if both jet are in the abs(eta)<0.25 region ref jet should be chosen randomly in order to eliminate the resolution bias.

				ref_jet_pT    	  = recoJetPt[matchindex1]
				ref_jet_eta   	  = recoJetEta[matchindex1]
				
				probe_jet_pT  	  = recoJetPt[matchindex0]
				probe_jet_eta 	  = recoJetEta[matchindex0]

				probe_jet_pT_HLT  = dsJetPt[0]
				probe_jet_eta_HLT = dsJetEta[0]

				ref_jet_eta_raw  	  = recoJetEta[matchindex1]

				probe_jet_pT_raw  	  = recoJetRawPt[matchindex0]
				probe_jet_eta_raw 	  = recoJetEta[matchindex0]

				probe_jet_pT_HLT_raw  = dsJetRawPt[0]
				probe_jet_eta_HLT_raw = dsJetEta[0]

				balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
				balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
				balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
				balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
				balance_index = (bisect_left(res_bins, probe_jet_pT) - residue) + (bisect_left(nPVzbins, nPVz) - residue) * (len(res_bins) - 1) +(bisect_left(eta_bins, abs(probe_jet_eta)) - residue) * (len(res_bins) - 1) * (len(nPVzbins) - 1)
				if balance_index > -1 and balance_index < len(h_balance):
					h_balance[balance_index].Fill(balance1)
					h_balance_HLT[balance_index].Fill(balance2)
					h_balance_raw[balance_index].Fill(balance3)
					h_balance_HLT_raw[balance_index].Fill(balance4)

			else:
				ref_jet_pT    	  = recoJetPt[matchindex0]
				ref_jet_eta   	  = recoJetEta[matchindex0]
				
				probe_jet_pT  	  = recoJetPt[matchindex1]
				probe_jet_eta 	  = recoJetEta[matchindex1]

				probe_jet_pT_HLT  = dsJetPt[1]
				probe_jet_eta_HLT = dsJetEta[1]

				ref_jet_eta_raw  	  = recoJetEta[matchindex0]

				probe_jet_pT_raw  	  = recoJetRawPt[matchindex1]
				probe_jet_eta_raw 	  = recoJetEta[matchindex1]

				probe_jet_pT_HLT_raw  = dsJetRawPt[1]
				probe_jet_eta_HLT_raw = dsJetEta[1]

				balance1          = (probe_jet_pT - ref_jet_pT) / (probe_jet_pT + ref_jet_pT)
				balance2          = (probe_jet_pT_HLT - ref_jet_pT) / (probe_jet_pT_HLT + ref_jet_pT)
				balance3          = (probe_jet_pT_raw - ref_jet_pT) / (probe_jet_pT_raw + ref_jet_pT)
				balance4          = (probe_jet_pT_HLT_raw - ref_jet_pT) / (probe_jet_pT_HLT_raw + ref_jet_pT)
				balance_index = (bisect_left(res_bins, probe_jet_pT) - residue) + (bisect_left(nPVzbins, nPVz) - residue) * (len(res_bins) - 1) + (bisect_left(eta_bins, abs(probe_jet_eta)) - residue) * (len(res_bins) - 1) * (len(nPVzbins) - 1)
				if balance_index > -1 and balance_index < len(h_balance):
					h_balance[balance_index].Fill(balance1)
					h_balance_HLT[balance_index].Fill(balance2)
					h_balance_raw[balance_index].Fill(balance3)
					h_balance_HLT_raw[balance_index].Fill(balance4)
	
				
		global_index0 = indexi0 + indexj * (len(res_bins) - 1) + indexk0 * (len(res_bins) - 1) * (len(nPVzbins) - 1)
		if global_index0 > -1 and global_index0 < len(h_resPt):
			#print  "nPVz =", nPVz, " recoJetPt[matchindex0] =", recoJetPt[matchindex0] , " recoJetPt[matchindex1] =", recoJetPt[matchindex1] , " recoJetEta[matchindex0] =", recoJetEta[matchindex0], "recoJetEta[matchindex1] =", recoJetEta[matchindex1], " indexi0 =", indexi0, " indexi1 =", indexi1, " indexj =", indexj, " indexk0 =", indexk0, " indexk1 =", indexk1, "global_index0 =", global_index0
			#print 'global_index0:', global_index0, 'histo name 0 =', h_resPt[global_index0].GetName()
			ratioRawPt0   = dsJetRawPt[0] / recoJetRawPt[matchindex0]
			ratioPt0      = dsJetPt[0] / recoJetPt[matchindex0]
			#print 'dsJetEta[0]', dsJetEta[0], 'recoJetEta[matchindex0]', recoJetEta[matchindex0],'dsJetPt[0]', dsJetPt[0], 'recoJetPt[matchindex0]', recoJetPt[matchindex0], 'ratioPt0', ratioPt0
			h_resPt[global_index0].Fill(ratioPt0)
			h_resRawPt[global_index0].Fill(ratioRawPt0)


		global_index1 = indexi1 + indexj * (len(res_bins) - 1) + indexk1 * (len(res_bins) - 1) * (len(nPVzbins) - 1)
		if global_index1 > -1 and global_index1 < len(h_resPt):
			#print "global_index1", global_index1
			#print " histo name 1", h_resPt[global_index1].GetName()
			ratioRawPt1   = dsJetRawPt[1] / recoJetRawPt[matchindex1]
			ratioPt1      = dsJetPt[1] / recoJetPt[matchindex1]
			h_resPt[global_index1].Fill(ratioPt1)
			h_resRawPt[global_index1].Fill(ratioRawPt1)

mean      = array('d')
sigma     = array('d')
mean_err  = array('d')
sigma_err = array('d')

can         = []
can_pT      = []
can_Raw_pT  = []

# for k in range(len(eta_bins)-1):
# 	for j in range(len(nPVzbins)-1):
# 		for i in range(len(res_bins)-1):
# 			common_suffixes    = run_period + "_" + str(nPVzbins[j]) + '_' + str(nPVzbins[j+1]) + '_' + str(int(res_bins[i])) + "_" + str(int(res_bins[i+1])) + "_" + str(eta_bins[k]) + "_" + str(eta_bins[k+1])
# 			global_index = i + j * (len(res_bins)-1) + k * (len(nPVzbins)-1) * (len(res_bins)-1)
# 			c_name = "c_res_" + common_suffixes
# 			can.append(TCanvas(c_name, c_name, 600, 600))
# 			can[global_index].cd()

# 			h_res[global_index].SetMarkerStyle(20)
# 			h_res[global_index].SetDrawOption('E1][')
# 			gPad.SetLogy()
# 			can[global_index].Update()
# 			can[global_index].SaveAs(c_name + '.pdf')
# 			can[global_index].SaveAs(c_name + '.png')

# 			c_name = "c_res_Pt" + common_suffixes
# 			can_pT.append(TCanvas(c_name, c_name, 600, 600))
# 			can_pT[global_index].cd()

# 			h_resPt[global_index].SetMarkerStyle(20)
# 			h_resPt[global_index].SetDrawOption('E1][')
# 			gPad.SetLogy()
# 			can_pT[global_index].Update()
# 			can_pT[global_index].SaveAs(c_name + '.pdf')
# 			can_pT[global_index].SaveAs(c_name + '.png')

# 			c_name = "c_res_Raw_pT" + common_suffixes
# 			can_Raw_pT.append(TCanvas(c_name, c_name, 600, 600))
# 			can_Raw_pT[global_index].cd()

# 			h_resRawPt[global_index].SetMarkerStyle(20)
# 			h_resRawPt[global_index].SetDrawOption('E1][')
# 			gPad.SetLogy()
# 			can_Raw_pT[global_index].Update()
# 			can_Raw_pT[global_index].SaveAs(c_name + '.pdf')
# 			can_Raw_pT[global_index].SaveAs(c_name + '.png')


file_to_write.cd()

for i in xrange(len(h_resPt)-1):
    h_resPt[i].Write()
    h_resRawPt[i].Write()
    h_balance[i].Write()
    h_balance_raw[i].Write()
    h_balance_HLT[i].Write()
    h_balance_HLT_raw[i].Write()

	#can[i].Write()
	#can_pT[i].Write()
	#can_Raw_pT[i].Write()

#keepGUIalive
rep = ''
while not rep in ['q','Q']:
	rep = raw_input('enter "q" to quit: ')
	if 1 < len(rep):
		rep = rep[0]
