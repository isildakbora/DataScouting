
#!usr/bin/python
import ROOT, tdrStyle
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
partonic_decay_names = {'RSGravitonToGG':'gg', 'RSGravitonToQQbar':'qq', 'QstarToJJ':'qg'}

signalnames = {'RSGravitonToGG':'gg #rightarrow RS #rightarrow gg', 'RSGravitonToQQbar':'q#bar{q} #rightarrow RS #rightarrow q#bar{q}', 'QstarToJJ':'qg #rightarrow Q* #rightarrow qg'}

PATH  = "~/lxplus_workspace_fuse/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets/Resonance_Shapes_"+signaltype+".root" 
mass  = array('i', range(500, 1000, 200))
#mass = array('i', range(500, 1700, 100))
color = [ROOT.kGray, ROOT.kRed, ROOT.kBlue, ROOT.kGreen+1, ROOT.kMagenta, ROOT.kAzure, ROOT.kGreen+3, ROOT.kOrange, ROOT.kAzure+6, ROOT.kRed+4, ROOT.kBlack+3, ROOT.kYellow-4]#array('i', range(1, len(mass)+2))

if highlow == 'high':
  PATH  = "~/lxplus_workspace/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets/Resonance_Shapes_"+signaltype+".root" 
  mass  = [1000,2000,3000,4000, 5500]
  color = [ROOT.kBlack,ROOT.kRed,ROOT.kBlue,ROOT.kGreen+1,ROOT.kMagenta]
  xmax  = 5000

hist      = []
hist_standard = []

#---- open the files --------------------
i = 0
for im in mass:
  inf = TFile.Open(PATH)
  print "h_"+partonic_decay_names[signaltype]+"_"+str(im)
  h = inf.FindObjectAny("h_"+partonic_decay_names[signaltype]+"_"+str(im))
  print h.GetName()
  h.Scale(1.0/(h.Integral()))
  h.Rebin(rebin)
  h.SetDirectory(0)
  h.SetLineColor(color[i+1])
  #h.SetFillColor(color[i])
  #h.SetFillColorAlpha(color[i], 0.5)
  h.SetLineWidth(2)
  hist.append(h)
   
  i += 1

#----- Drawing -----------------------
can = TCanvas('can_Signal_'+var,'can_Signal_'+var,600,600)
#can.SetRightMargin(0.2)
hist[0].GetYaxis().SetNdivisions(505)
hist[0].GetYaxis().SetTitle('Probability Distribution')
hist[0].GetYaxis().SetTitleOffset(1.3)
hist[0].GetYaxis().SetTitleSize(0.05)
hist[0].GetYaxis().CenterTitle()
hist[0].GetYaxis().SetLabelSize(0.04)
hist[0].GetXaxis().SetTitle(xtitle)
hist[0].GetXaxis().SetTitleSize(0.05)
hist[0].GetXaxis().SetLabelSize(0.04)
hist[0].GetXaxis().SetRangeUser(xmin,hist[len(mass)-1].GetMean()+4.*hist[len(mass)-1].GetRMS())
hist[0].SetMaximum(1.1*TMath.Max(hist[0].GetBinContent(hist[0].GetMaximumBin()),hist[len(mass)-1].GetBinContent(hist[len(mass)-1].GetMaximumBin())))
hist[0].Draw('hist')

for i in range(1,len(mass)):
  hist[i].Draw('same hist')
#gPad.RedrawAxis()

leg = TLegend(0.75, 0.50, 0.90, 0.85)
leg1 = TLegend(0.70, 0.87, 0.96, 0.92)
leg1.SetHeader(signalnames[signaltype])

for i in range(0,len(mass)):
  leg.AddEntry(hist[i],str(mass[i]/1000.)+' TeV','fl')

gPad.RedrawAxis()

leg.SetFillColor(0)
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetShadowColor(0)
leg.SetLineColor(ROOT.kWhite)
leg.Draw()

leg1.SetFillColor(0)
leg1.SetTextFont(42)
leg1.SetTextColor(4)
leg1.SetTextSize(0.04)
leg1.SetShadowColor(0)
leg1.SetLineColor(ROOT.kWhite)
leg1.Draw()


can.SaveAs(signaltype+"_"+highlow+".pdf")
can.SaveAs(signaltype+"_"+highlow+".png")





#----- keep the GUI alive ------------
if __name__ == '__main__':
  rep = ''
  while not rep in ['q','Q']:
    rep = raw_input('enter "q" to quit: ')
    if 1 < len(rep):
      rep = rep[0]

# #!usr/bin/python
# import ROOT
# from ROOT import TFile, TH1F, TMath, TCanvas, TLegend, gROOT, gPad, TObject
# from setTDRStyle import setTDRStyle
# import optparse
# from array import array
# from rootutils import *

# usage = "usage: %prog [options]"
# parser = optparse.OptionParser(usage)

# parser.add_option("--var",action="store",type="string",dest="var",default='MjjWide_finalSel_varbin')
# parser.add_option("--signaltype",action="store",type="string",dest="signaltype",default='RSGravitonToGG')
# parser.add_option("--highlow",action="store",type="string",dest="highlow",default='low')
# parser.add_option("--xmin",action="store",type="float",dest="xmin",default=0)
# parser.add_option("--xmax",action="store",type="float",dest="xmax",default=2000)
# parser.add_option("--xtitle",action="store",type="string",dest="xtitle",default='M_{jj} [GeV]')
# parser.add_option("--rebin",action="store",type="int",dest="rebin",default=1)

# (options, args) = parser.parse_args()

# var        = options.var
# signaltype = options.signaltype
# highlow    = options.highlow
# xmin       = options.xmin
# xmax       = options.xmax
# xtitle     = options.xtitle
# rebin      = options.rebin

# #gROOT.Reset()
# #setTDRStyle()
# #gROOT.ForceStyle()
# #gROOT.SetStyle('tdrStyle')

# partonic_decay_names = {'RSGravitonToGG':'gg', 'RSGravitonToQQbar':'qq', 'QstarToJJ':'qg'}

# signalnames = {'RSGravitonToGG':'gg #rightarrow RS #rightarrow gg', 'RSGravitonToQQbar':'q#bar{q} #rightarrow RS #rightarrow q#bar{q}', 'QstarToJJ':'qg #rightarrow Q* #rightarrow qg'}

# PATH  = "~/lxplus_workspace/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets" + signaltype 
# mass  = array('d', range(500, 1700, 100))
# color = range(0, len(mass)+1, 1)

# if highlow == 'high':

#   PATH  = "/Users/bora/Dropbox/DataScouting/SignalSamples/" + signaltype 
#   mass  = [1000,2000,3000,4000]
#   color = [ROOT.kBlack,ROOT.kRed,ROOT.kBlue,ROOT.kGreen+1,ROOT.kMagenta]
#   xmax  = 5000

# hist      = []
# hist_standard = []
# can = TCanvas('can_Signal_'+var,'can_Signal_'+var,600,600)
# leg = TLegend(0.75,0.60,0.8,0.85)
# leg1 = TLegend(0.65,0.87,0.76,0.92)
# leg1.SetHeader(signalnames[signaltype])
# #---- open the files --------------------
# i = 0
# for im in mass:
#   inf  = TFile.Open("/Users/boraisildak/lxplus_workspace/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets/Resonance_Shapes_"+signaltype+".root")
#   print inf.GetName()
#   h = inf.FindObjectAny('h_'+partonic_decay_names[signaltype]+'_'+str(int(im)))
#   h.SetLineColor(color[i])
#   #h.SetFillColorAlpha(color[i], 0.5)
#   h.SetLineWidth(2)
#   hist.append(h)
#   i += 1
#   #can.SetRightMargin(0.2)
#   if i == 0:
#     h.Draw('hist')
#     h.GetYaxis().SetNdivisions(505)
#     h.GetYaxis().SetTitle('Number of Events / bin size')
#     h.GetYaxis().SetLabelSize(0.04)
#     h.GetXaxis().SetTitle(xtitle)
#     h.GetXaxis().SetLabelSize(0.04)
#     h.GetXaxis().SetRangeUser(xmin,hist[len(mass)-1].GetMean()+3*hist[len(mass)-1].GetRMS())
#     h.SetMaximum(1.1*TMath.Max(hist[0].GetBinContent(hist[0].GetMaximumBin()),hist[len(mass)-1].GetBinContent(hist[len(mass)-1].GetMaximumBin())))

#   h.Draw('same hist')
#   leg.AddEntry(h, str(im/1000)+' TeV','L')

# leg.SetFillColor(0)
# leg.SetTextFont(42)
# leg.SetTextSize(0.03)
# leg.Draw()
# leg1.SetFillColor(0)
# leg1.SetTextFont(42)
# leg1.SetTextColor(4)
# leg1.SetTextSize(0.04)
# leg1.Draw()

# #can.SaveAs(signaltype+"_"+highlow+".pdf")
# #can.SaveAs(signaltype+"_"+highlow+".png")


# #----- keep the GUI alive ------------
# if __name__ == '__main__':
#   rep = ''
#   while not rep in ['q','Q']:
#     rep = raw_input('enter "q" to quit: ')
#     if 1 < len(rep):
#       rep = rep[0]
