import ROOT, itertools, re, tdrStyle, CMS_lumi
from ROOT import TGraph, TLatex, TLegend, TColor
from rootutils import*
from array import array

tdrStyle.setTDRStyle()
# CMS_lumi.extraText  = "Data"
# CMS_lumi.lumi_sqrtS = "18.8 fb^{-1} (8 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText      = ""
CMS_lumi.lumiTextSize   = 0.75
CMS_lumi.lumi_sqrtS     = "18.8 fb^{-1} (8 TeV)"
iPos = 0
if( iPos==0 ): CMS_lumi.relPosX = 0.1
iPeriod = 0

masses          = array('d', range(500, 1700, 100))
resonances      = ["RSGravitonToGG", "RSGravitonToQQbar", "QStarToJJ"]
Observed_Bounds = {"RSGravitonToGG":array('d',[]), "RSGravitonToQQbar":array('d',[]), "QStarToJJ":array('d',[])}
#Expected_Bounds = {"RSGravitonToGG":array('d',[]), "RSGravitonToQQbar":array('d',[]), "QStarToJJ":array('d',[])}
#One_Sigma_Band  = {"RSGravitonToGG":array('d',[]), "RSGravitonToQQbar":array('d',[]), "QStarToJJ":array('d',[])}
#Two_Sigma_Band  = {"RSGravitonToGG":array('d',[]), "RSGravitonToQQbar":array('d',[]), "QStarToJJ":array('d',[])}

qstar_theory      = array('d',[])
axigluon_theory   = array('d',[])
E6Diquark_theory  = array('d',[])
Zprime_theory     = array('d',[])
Wprime_theory     = array('d',[])
RSGraviton_theory = array('d',[])

theory_xsections  = [qstar_theory, axigluon_theory, E6Diquark_theory, Zprime_theory, Wprime_theory, RSGraviton_theory]

lines = [line.rstrip('\n') for line in open('all_lhc8TeV.txt')]

line_style_for_signals = 8

for i in range(len(lines)):
	for j in xrange(len(lines[i].split())-1):
		theory_xsections[j].append(float(lines[i].split()[j+1]))
		print str(float(theory_xsections[j][-1]))
	print "\n"

for resonance, mass in itertools.product(resonances, xrange(500, 1700, 100)):
	log_filename = 'log_' + str(mass) + '_' + resonance + '.txt'
	#print log_filename
	lines = [line.rstrip('\n') for line in open(log_filename)]
	for line in lines:
		#print line
		if re.search("observed bound =", line):
			Observed_Bounds[resonance].append(float(line.split()[6]))
			#print Observed_Bounds[resonance][-1], float(line.split()[6])
		
		if resonance == "RSGravitonToQQbar":
			
			if re.search("median", line):
				print float(line.split()[1])
			
			#if re.search("sigma band:", line):
			#	print line #float(line.split()[5]), float(line.split()[7])
print qstar_theory

qstar_theory_limits 	 = TGraph(len(masses), masses, qstar_theory)
qstar_theory_limits.SetLineColor(ROOT.kBlack)
qstar_theory_limits.SetLineStyle(2)
qstar_theory_limits.SetLineWidth(2)

axigluon_theory_limits	 = TGraph(len(masses), masses, axigluon_theory)
axigluon_theory_limits.SetLineColor(ROOT.kAzure + 10)
axigluon_theory_limits.SetLineStyle(3)
axigluon_theory_limits.SetLineWidth(2)

ScalarDiquark_theory_limits  = TGraph(len(masses), masses, E6Diquark_theory)
ScalarDiquark_theory_limits.SetLineColor(ROOT.kOrange - 8)
ScalarDiquark_theory_limits.SetLineStyle(9)
ScalarDiquark_theory_limits.SetLineWidth(2)

Wprime_theory_limits     = TGraph(len(masses), masses, Wprime_theory)
Wprime_theory_limits.SetLineColor(ROOT.kRed - 7)
Wprime_theory_limits.SetLineStyle(7)
Wprime_theory_limits.SetLineWidth(2)

Zprime_theory_limits     = TGraph(len(masses), masses, Zprime_theory)
Zprime_theory_limits.SetLineColor(ROOT.kBlue - 8)
Zprime_theory_limits.SetLineStyle(5)
Zprime_theory_limits.SetLineWidth(2)

RSGraviton_theory_limits = TGraph(len(masses), masses, RSGraviton_theory)
RSGraviton_theory_limits.SetLineColor(ROOT.kCyan - 6)
RSGraviton_theory_limits.SetLineStyle(4)
RSGraviton_theory_limits.SetLineWidth(2)

RSGravitonToGG_limits 	 = TGraph(len(Observed_Bounds["RSGravitonToGG"]), masses, Observed_Bounds["RSGravitonToGG"])
RSGravitonToQQbar_limits = TGraph(len(Observed_Bounds["RSGravitonToQQbar"]), masses, Observed_Bounds["RSGravitonToQQbar"])
QStarToJJ_limits 		 = TGraph(len(Observed_Bounds["QStarToJJ"]), masses, Observed_Bounds["QStarToJJ"])

RSGravitonToGG_limits.SetLineColor(ROOT.kGreen+3)
RSGravitonToGG_limits.SetMarkerColor(ROOT.kGreen+3)
RSGravitonToGG_limits.SetMarkerStyle(4)
RSGravitonToGG_limits.SetLineWidth(3)

RSGravitonToQQbar_limits.SetLineColor(ROOT.kBlue)
RSGravitonToQQbar_limits.SetMarkerColor(ROOT.kBlue)
RSGravitonToQQbar_limits.SetMarkerStyle(26)
RSGravitonToQQbar_limits.SetLineWidth(3)

QStarToJJ_limits.SetLineColor(ROOT.kRed)
QStarToJJ_limits.SetMarkerColor(ROOT.kRed)
QStarToJJ_limits.SetMarkerStyle(20)
QStarToJJ_limits.SetLineWidth(3)

RSGravitonToGG_limits.GetXaxis().SetTitle("Resonance Mass [GeV]")
RSGravitonToGG_limits.GetYaxis().SetTitle("#sigma B A [pb]")
RSGravitonToGG_limits.GetYaxis().SetTitleFont(42)
RSGravitonToGG_limits.GetYaxis().SetRangeUser(2e-02, 1e+04)
RSGravitonToGG_limits.GetXaxis().SetNdivisions(1005)
#RSGravitonToGG_limits.GetYaxis().CenterTitle()

Canvas0 = TCanvas("Canvas0","Canvas0",600,600)

RSGravitonToGG_limits.Draw('APL')
gPad.SetLogy()

RSGravitonToQQbar_limits.Draw('PL SAME')
QStarToJJ_limits.Draw('PL SAME')

qstar_theory_limits.Draw('L SAME')
axigluon_theory_limits.Draw('L SAME')
ScalarDiquark_theory_limits.Draw('L SAME')
Zprime_theory_limits.Draw('L SAME')
Wprime_theory_limits.Draw('L SAME')
RSGraviton_theory_limits.Draw('L SAME')

leg = TLegend(0.43, 0.72, 0.63, 0.92)
leg.SetHeader("95 % CL Upper Limit")

leg.AddEntry(RSGravitonToGG_limits, "gluon-gluon",'pl')
leg.AddEntry(QStarToJJ_limits, "quark-qluon",'pl')
leg.AddEntry(RSGravitonToQQbar_limits, "quark-quark",'pl')
leg.SetFillColorAlpha(0, 0)
leg.SetTextFont(42)
leg.SetTextSize(0.03)
leg.SetShadowColor(0)
leg.SetLineColor(ROOT.kWhite)
leg.Draw()

leg1 = TLegend(0.70, 0.72,0.95, 0.92)

leg1.AddEntry(ScalarDiquark_theory_limits, "Scalar diquark",'l')
leg1.AddEntry(axigluon_theory_limits, "Axigluon",'l')
leg1.AddEntry(qstar_theory_limits, "Excited quark",'l')
leg1.AddEntry(Wprime_theory_limits, "W\'",'l')
leg1.AddEntry(Zprime_theory_limits, "Z\'",'l')
leg1.AddEntry(RSGraviton_theory_limits, "RS graviton",'l')
leg1.SetFillColorAlpha(0, 0)
leg1.SetTextFont(42)
leg1.SetTextSize(0.03)
leg1.SetShadowColor(0)
leg1.SetLineColor(ROOT.kWhite)
leg1.Draw()

lstat = TLatex()
lstat.SetTextAlign(12)
lstat.SetTextFont(42)
lstat.SetNDC()
lstat.SetTextSize(0.05)

x_latex_pos_left = 0.50
y_latex_pos_up   = 0.90

#lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-0*0.05, "|#eta| < 2.5 & |#Delta #eta| < 1.3")

gPad.cd()
CMS_lumi.CMS_lumi(gPad, iPeriod, iPos)
Canvas0.cd()
Canvas0.Update()
Canvas0.RedrawAxis()
Canvas0.SaveAs("xsec_limits.pdf")
Canvas0.SaveAs("xsec_limits.png")

print CMS_lumi.lumi_sqrtS
keepGUIalive()
