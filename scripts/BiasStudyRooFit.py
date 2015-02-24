#!/usr/bin/env python
import sys, getopt
import ROOT
from ROOT import *
import math
from array import array
from numpy import divide, sqrt

signal_mass = sys.argv[1]
mass_low  = 354.#float(signal_mass) - 200.
mass_high = 4000.#float(signal_mass) + 200.

#Dijet Mass Binning 
#massBins = array('d',[354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509])
massBins = array('d', range(int(mass_low), int(mass_high)))

file_type     = TFile.Open("/afs/cern.ch/user/i/isildak/public/DijetDataScouting/dijetFitResults_FuncType3_nParFit7_Run2012BCD.root")
func_type     = file_type.FindObjectAny("M1Bkg").Clone("M1Bkg_func_type_2")

MC_signal_file  = TFile.Open("/afs/cern.ch/user/i/isildak/public/DijetDataScouting/SignalSamples/RSGravitonToGG_M_" + str(signal_mass) + "/histo.root")
MC_signal_histo = MC_signal_file.FindObjectAny("h1_MjjWide_finalSel")

pseudo_data = TH1F("Generated_by_Type_1_Function","Generated_by_Type_1_Function", len(massBins)-1, massBins)
pseudo_data.Sumw2()

bias      = TH1F("bias", "bias", 1000, -1, 1)
bias_pull = TH1F("bias_pull", "bias_pull", 1000, -1, 1)
bias.SetBit(TH1.kCanRebin)
bias_pull.SetBit(TH1.kCanRebin)

output_file = TFile.Open("bias" + str(signal_mass) + ".root", "RECREATE")

f = open('log_'+ str(signal_mass) +'.txt','w')
ngoodfit = 0

for i in xrange(1):#while ngoodfit < int(sys.argv[3]):
	#Generate by type 1
	for i in xrange(0, len(massBins)-1):
		r = TRandom3()
		r.SetSeed(0)
		mjj_y = func_type.Integral(massBins[i], massBins[i+1])
		bin_width = massBins[i+1] - massBins[i]
		pseudo_data.SetBinContent(i+1, r.Poisson(mjj_y/bin_width))
		pseudo_data.SetBinError(i+1, math.sqrt(pseudo_data.GetBinContent(i+1)))

	x = RooRealVar("mjj", "mjj", mass_low, mass_high)

	sigfrac   = RooRealVar("frac" ,"fraction" , 0., -1., 1.)
	#nsig      = RooRealVar("nsig" ,"N Signal" , 100, -1e-6, 1e+6)
	#nbkg      = RooRealVar("nbkg" ,"N Background" , 1e+5, -1e+6, 1e+6)
	hist1     = RooDataHist ("hist1","hist1", RooArgList(x), pseudo_data)
	MC_hist   = RooDataHist ("MC_hist","MC_hist", RooArgList(x), MC_signal_histo)

	scale = 5.
	p0 = RooRealVar('p0','p0', func_type.GetParameter(0), func_type.GetParameter(0)-scale*func_type.GetParError(0), func_type.GetParameter(0)+scale*func_type.GetParError(0))
	p1 = RooRealVar('p1','p1', func_type.GetParameter(1), func_type.GetParameter(1)-scale*func_type.GetParError(1), func_type.GetParameter(1)+scale*func_type.GetParError(1)) 
	p2 = RooRealVar('p2','p2', func_type.GetParameter(2), func_type.GetParameter(2)-scale*func_type.GetParError(2), func_type.GetParameter(2)+scale*func_type.GetParError(2))
	p3 = RooRealVar('p3','p3', func_type.GetParameter(3), func_type.GetParameter(3)-scale*func_type.GetParError(3), func_type.GetParameter(3)+scale*func_type.GetParError(3))
	p4 = RooRealVar('p4','p4', func_type.GetParameter(4), func_type.GetParameter(4)-scale*func_type.GetParError(4), func_type.GetParameter(4)+scale*func_type.GetParError(4))
	p5 = RooRealVar('p5','p5', func_type.GetParameter(5), func_type.GetParameter(5)-scale*func_type.GetParError(5), func_type.GetParameter(5)+scale*func_type.GetParError(5))
	p6 = RooRealVar('p6','p6', func_type.GetParameter(6), func_type.GetParameter(6)-scale*func_type.GetParError(6), func_type.GetParameter(6)+scale*func_type.GetParError(6))

	bkg = RooGenericPdf("background", "(@1*pow(1-@0/8000,@2)*(1+@5*@0/8000+@6*pow(@0/8000,2)+@7*pow(@0/8000,3)))/(pow(@0/8000,@3+@4*log(@0/8000)))", RooArgList(x, p0, p1, p2, p3, p4, p5, p6) )

	#hist1		 = bkg.generate(RooArgSet(x),1e+4)
	sig    = RooHistPdf("signal", "signal", RooArgSet(x), MC_hist)
	model  = RooAddPdf("model","Signal + Background", RooArgList(sig,bkg), RooArgList(sigfrac))
	result = model.fitTo(hist1, RooFit.NumCPU(8), RooFit.Save(), RooFit.PrintLevel(-1), RooFit.PrintEvalErrors(-1))

	if int(sys.argv[2])==1:
		can2 = TCanvas('can2', 'can2', 600, 600)
		can2.SetLogx(True)
		can2.SetLogy(True)
		frame  = x.frame(RooFit.Title("Signal Fraction"))
		hist1.plotOn(frame)
		model.plotOn(frame)
		model.plotOn(frame, RooFit.Components("back*"), RooFit.LineColor(RooFit.kRed))
		model.plotOn(frame, RooFit.Components("sig*"), RooFit.LineStyle(RooFit.kDashed))
		model.paramOn(frame, RooFit.Layout(0.55))
		hist1.statOn(frame,RooFit.Layout(0.55,0.99,0.8))
		frame.GetXaxis().SetRangeUser(mass_low, mass_high)
		frame.GetYaxis().SetRangeUser(1e-2, 1e+7)
		frame.GetXaxis().SetTitle('m_{jj} (GeV)')
		frame.Draw()

	for i in xrange(0,6):
		print func_type.GetParameter(i)

	print "Signal Fraction/ Signal Fraction Error/Pull: ", sigfrac.getVal(), sigfrac.getError(), sigfrac.getVal()/sigfrac.getError(), result.covQual()
	f.write('Signal Fraction/ Signal Fraction Error/Pull: ' + str(sigfrac.getVal()) + ' ' + str(sigfrac.getError()) + ' ' + str(sigfrac.getVal()/sigfrac.getError()) +'\n')
	
	if result.covQual()==3:
		ngoodfit = ngoodfit + 1
		bias.Fill(sigfrac.getVal())
		bias_pull.Fill(sigfrac.getVal()/sigfrac.getError())

	print "ngoodfit:" , ngoodfit

output_file.cd()
bias.Write()
bias_pull.Write()
f.close()

if int(sys.argv[2]) == 1:
	rep = ''
	while not rep in ['q','Q']:
		rep = raw_input('enter "q" to quit: ')
		if 1 < len(rep):
			rep = rep[0]
