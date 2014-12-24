import ROOT, sys
from ROOT import *
from rootutils import *
import math, sys, numpy as np
from setTDRStyle import setTDRStyle

gROOT.Reset()
setTDRStyle()
gROOT.ForceStyle()
gROOT.SetStyle('tdrStyle')
resonance = str(sys.argv[1])
mass      = str(sys.argv[2])
f1=TFile.Open(resonance + '_M_' + mass + '.root')
h1=f1.FindObjectAny('h1_MjjWide_finalSel_varbin')
h1.SetLineColor(ROOT.kRed)

f3=TFile.Open('RECO_' + resonance + '_M_' + mass + '.root')
h4=f3.FindObjectAny('h1_MjjWide_finalSel_varbin')
h4.SetLineColor(ROOT.kOrange)


f2=TFile.Open(resonance + '_signals.root')
h2=f2.FindObjectAny('hist_smeared_'+mass)
h2.SetLineColor(ROOT.kBlack)
h3=f2.FindObjectAny('hist_true'+mass)

h1.Scale(1./h1.Integral())
h2.Scale(1./h2.Integral())
h3.Scale(1./h3.Integral())
h4.Scale(1./h4.Integral())

h1.Draw()
h2.Draw('SAME')
h3.Draw('SAME')
h4.Draw('SAME')
keepGUIalive()