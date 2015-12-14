
import ROOT, sys, tdrStyle, CMS_lumi, rootutils
from ROOT import *
from rootutils import *
import math, sys, numpy as np
from ROOT import TFile, TH1F, TMath, TCanvas, TLegend, gROOT, gPad, gStyle, TObject
import optparse
from array import array
from rootutils import *

tdrStyle.setTDRStyle()
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)

parser.add_option("--var",action="store",type="string",dest="var",default='MjjWide_finalSel_varbin')
parser.add_option("--signaltype",action="store",type="string",dest="signaltype",default='RSGravitonToGG')
parser.add_option("--highlow",action="store",type="string",dest="highlow",default='low')
parser.add_option("--xmin",action="store",type="float",dest="xmin",default=0)
parser.add_option("--xmax",action="store",type="float",dest="xmax",default=2000)
parser.add_option("--xtitle",action="store",type="string",dest="xtitle",default='M_{jj} [GeV]')
parser.add_option("--rebin",action="store",type="int",dest="rebin",default=1)

(options, args) = parser.parse_args()

var        = options.var
signaltype = options.signaltype
highlow    = options.highlow
xmin       = options.xmin
xmax       = options.xmax
xtitle     = options.xtitle
rebin      = options.rebin

gStyle.SetOptStat(0000)
partonic_decay_names = ['RSGravitonToGG', 'RSGravitonToQQbar', 'QstarToJJ']

signalnames = {'RSGravitonToGG':'gg #rightarrow RS #rightarrow gg', 'RSGravitonToQQbar':'q#bar{q} #rightarrow RS #rightarrow q#bar{q}', 'QstarToJJ':'qg #rightarrow Q* #rightarrow qg'}

mass   = array('i', range(500, 1100, 100))
massx  = array('d', range(500, 1100, 100))
#mass = array('i', range(500, 1700, 100))
color = [ROOT.kGray, ROOT.kRed, ROOT.kBlue, ROOT.kGreen+1, ROOT.kMagenta, ROOT.kAzure, ROOT.kGreen+3, ROOT.kOrange, ROOT.kAzure+6, ROOT.kRed+4, ROOT.kBlack+3, ROOT.kYellow-4]#array('i', range(1, len(mass)+2))


hist      = []
graph = [array("d",[]), array("d",[]), array("d",[])]

	#---- open the files --------------------
for signal in partonic_decay_names:
	for im in mass:
	  inf = TFile.Open("~/lxplus_workspace_fuse/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets/"+signal+"_M_"+ str(im)+"/histo.root")
	  h = inf.FindObjectAny("h1_cutFlow")

	  print h.GetXaxis().GetBinLabel(4)
	  print h.GetXaxis().GetBinLabel(5)

	  graph[partonic_decay_names.index(signal)].append(h.GetBinContent(5)/h.GetBinContent(4))


gr_1	 = TGraph(len(graph[0]), massx, graph[0])
gr_1.SetMarkerColor(ROOT.kRed)
gr_1.SetLineColor(ROOT.kRed)


gr_2	 = TGraph(len(graph[1]), massx, graph[1])
gr_2.SetMarkerColor(ROOT.kBlue)
gr_2.SetLineColor(ROOT.kBlue)

gr_3	 = TGraph(len(graph[2]), massx, graph[2])
gr_3.SetMarkerColor(ROOT.kGreen)
gr_3.SetLineColor(ROOT.kGreen)

gr_1.Draw("APZL")
gr_1.GetYaxis().SetRangeUser(0.95, 1.05)
gr_1.GetYaxis().SetTitle("Jet ID Cut Efficiency")
gr_1.GetXaxis().SetTitle("Resonance Mass [GeV]")
gr_2.Draw("PZL SAME")
gr_3.Draw("PZL SAME")

leg = TLegend(0.65, 0.70, 0.90, 0.85)

leg.AddEntry(gr_1,partonic_decay_names[0], 'lp')
leg.AddEntry(gr_2,partonic_decay_names[1], 'lp')
leg.AddEntry(gr_3,partonic_decay_names[2], 'lp')

gPad.RedrawAxis()

leg.SetFillColor(0)
leg.SetTextFont(42)
leg.SetTextSize(0.02)
leg.SetShadowColor(0)
leg.SetLineColor(ROOT.kWhite)
leg.Draw("SAME")

keepGUIalive()
