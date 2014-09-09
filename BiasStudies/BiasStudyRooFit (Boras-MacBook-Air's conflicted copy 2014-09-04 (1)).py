#!usr/bin/python
import sys, getopt
import ROOT
from ROOT import *
from rootutils import *
import math

#Dijet Mass Binning 
massBins = array('d',[1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250,7500,7750,8000])

mass_low  = 354.
mass_high = 8000.
N = mass_high-mass_low

file_type1 = TFile.Open("../FisherStudies/5%Data/dijetFitResults_FuncType2_nParFit6_Run2012BCD.root")
func_type1 = file_type1.FindObjectAny("M1Bkg").Clone("M1Bkg_func_type_1")

gen_type1 = TH1F("Generated_by_Type_1_Function","Generated_by_Type_1_Function", int(N), mass_low, mass_high)
gen_type1.Sumw2()


#Generate by type 1
for i in xrange(0,int(N)):
	r = TRandom1()
	mjj_y = func_type1.Integral(mass_low+i, mass_low+i+1)
	gen_type1.SetBinContent(i+1, r.Poisson(mjj_y))
	gen_type1.SetBinError(i+1, TMath.Sqrt(gen_type1.GetBinContent(i+1)))
	print mjj_y, gen_type1.GetBinLowEdge(i+1), gen_type1.GetBinContent(i+1)



can = TCanvas('can', 'can', 600, 600)

func_type1.Draw()

x = RooRealVar("mjj", "mjj", 354., 8000.) 
x.setBins(10000, "cache")
hist1 = RooDataHist ("hist1","hist1", RooArgList(x), gen_type1)

p1 = RooRealVar('p1','p1', func_type1.GetParameter(1)) 
p2 = RooRealVar('p2','p2', func_type1.GetParameter(2))
p3 = RooRealVar('p3','p3', func_type1.GetParameter(3))
p4 = RooRealVar('p4','p4', func_type1.GetParameter(4), -100., 100.)
p5 = RooRealVar('p5','p5', func_type1.GetParameter(5))
p0 = RooRealVar('p0','p0', func_type1.GetParameter(0))

bkg = RooGenericPdf('background', '@1*(pow(1-@0/8000,@2)*(1+@5*(@0/8000)+@6*pow(@0/8000,2))/pow(@0/8000,@3+@4*log(@0/8000)))', RooArgList(x, p0, p1, p2, p3, p4, p5))

pdf1 = RooHistPdf ("pdf1", "pdf1", RooArgSet(x), hist1)

pseduodata = bkg.generate( RooArgSet(x), 1e+6)

can2 = TCanvas('can2', 'can2', 600, 600)
can2.SetLogy(True)
bkg.fitTo(pseduodata)
frame = x.frame()
pseduodata.plotOn(frame)
bkg.plotOn(frame)
frame.GetXaxis().SetRangeUser(0., 8000.)
frame.GetYaxis().SetRangeUser(1e-4, 4*1e+4)
frame.GetXaxis().SetTitle('m_{jj} (GeV)')
frame.Draw()
frame.GetXaxis().UnZoom()

keepGUIalive()