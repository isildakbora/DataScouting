#!usr/bin/python
import ROOT
import CMS_lumi
from ROOT import *
from setTDRStyle import setTDRStyle
from numpy import*
from array import array
import math
import tdrStyle

###############################################################
#################### Declare Functions #######################
# TGraph to python array

def TGraph2Array(graph, xy):
    data = array('d')
    for i in range(0, graph.GetN()):
        if xy == 'x':
            data.append(graph.GetX()[i])
        elif xy == 'y':
            data.append(graph.GetY()[i])
        else:
            print 'Please indicate x or y!'
    return data


def spline_inverse(y, spline, eps):
    epsilon = eps
    n = 0
    x = 0
    for j in linspace(0., 1., int(1./1000.)):
    	print j, spline.Eval(j) - y 
        if spline.Eval(j) < y + epsilon and spline.Eval(j) > y - epsilon:
            x = j
    return x
###############################################################
tdrStyle.setTDRStyle()

CMS_lumi.extraText = ""
# used with iPeriod = 0, e.g. for simulation-only plots (default is an
# empty string)
CMS_lumi.lumi_sqrtS = "18.8 fb^{-1} (8 TeV)"
iPos = 0
if(iPos == 0):
    CMS_lumi.relPosX = 0.065
iPeriod = 0

output_file = TFile.Open('gB_limits.root', 'RECREATE')
output_file.cd()

color_palette = [ROOT.kRed-4, ROOT.kMagenta-4, ROOT.kCyan-7,
                 ROOT.kAzure-4, ROOT.kOrange-3, ROOT.kGreen+3]

CMS_013_qq_xsec = [[604.23, 701.981, 803.269, 903.349, 1003.85], [
    17.3148, 16.7179, 9.85511, 4.45200, 3.35756]]
xsec_CMS_for_CDF_graph = TGraph(len(CMS_013_qq_xsec[0]), array(
    'd', CMS_013_qq_xsec[0]), array('d', CMS_013_qq_xsec[1]))

CDF_1_1_Zprime_xsec = [[620., 660., 700., 750., 800., 850., 900.], [
    0.85, 0.76, 0.64, 0.46, 0.29, 0.19, 0.14]]

c1 = TCanvas("gB Limits All", "gB Limits", 1000, 900)
c1.SetLeftMargin(0.1)
c1.SetRightMargin(0.05)

limits_CDF_1_1_data = genfromtxt(
    "gBMZB_CDF1_1_fbinv.csv", dtype=float, delimiter=',')
limits_CDF_1_1 = TGraph(len(limits_CDF_1_1_data.T[0]), array(
    'd', limits_CDF_1_1_data.T[0]), array('d', limits_CDF_1_1_data.T[1]))

limits_CDF_1_1.SetName("CDF1_1_fbinv")
limits_CDF_1_1.GetXaxis().SetLimits(0., 4500.)
limits_CDF_1_1.GetXaxis().SetTitle("M_{Z'_{B}} [GeV]")
# limits_CDF_1_1.GetXaxis().CenterTitle()

limits_CDF_1_1.GetYaxis().SetTitle('Coupling g_{B}')
limits_CDF_1_1.GetYaxis().SetLimits(0., 2.5)
limits_CDF_1_1.GetYaxis().CenterTitle()
limits_CDF_1_1.GetYaxis().SetTitleOffset(0.8)
limits_CDF_1_1.SetLineColor(ROOT.kRed)


limits_CDF_1_1.SetLineWidth(2)
limits_CDF_1_1.Write()

limits_ATLAS_1_data = genfromtxt("gBMZB_ATLAS_1_fbinv.csv", dtype=float, delimiter=',')
limits_ATLAS_1 = TGraph(len(limits_ATLAS_1_data.T[0]), array('d', limits_ATLAS_1_data.T[0]), array('d', limits_ATLAS_1_data.T[1]))
limits_ATLAS_1.SetName('ATLAS_1_fbinv')
limits_ATLAS_1.SetLineColor(ROOT.kBlack)
limits_ATLAS_1.SetLineWidth(2)
limits_ATLAS_1.Write()

limits_ATLAS_13 = TGraph("gBMZB_ATLAS_all_fbinv.csv", "%lg %lg", ",")
limits_ATLAS_13.SetName('ATLAS_13_fbinv')
limits_ATLAS_13.SetLineColor(ROOT.kMagenta-4)
limits_ATLAS_13.SetLineWidth(2)
# limits_ATLAS_13.SetLineStyle(7)
limits_ATLAS_13.Write()

limits_CMS_4 = TGraph("gBMZB_CMS_4_fbinv.csv", "%lg %lg", ",")
limits_CMS_4.SetName('CMS_4_fbinv')
limits_CMS_4.SetLineColor(ROOT.kGreen+3)
limits_CMS_4.SetLineWidth(2)
limits_CMS_4.SetLineStyle(9)
limits_CMS_4.Write()

limits_UA2 = TGraph("gBMZB_UA2.csv", "%lg %lg", ",")
limits_UA2.SetName('UA2')
limits_UA2.SetLineColor(ROOT.kBlue+2)
limits_UA2.SetLineWidth(2)
limits_UA2.Write()

limits_CMS_20 = TGraph("gBMZB_CMS_20_fbinv.csv", "%lg %lg", ",")
limits_CMS_20.SetName('CMS_20_fbinv')
limits_CMS_20.SetLineColor(ROOT.kAzure-4)
limits_CMS_20.SetLineWidth(2)
limits_CMS_20.Write()

limits_CMS_013 = TGraph("gBMZB_CMS_013_fbinv.csv", "%lg %lg", ",")
limits_CMS_013.SetName('CMS_013_fbinv')
limits_CMS_013.SetLineColor(ROOT.kCyan-2)
limits_CMS_013.SetLineWidth(2)
limits_CMS_013.SetLineStyle(9)
limits_CMS_013.Write()

limits_CMS_5 = TGraph("gBMZB_CMS_5_fbinv.csv", "%lg %lg", ",")
limits_CMS_5.SetName('CMS_5_fbinv')
limits_CMS_5.SetLineColor(ROOT.kGreen-2)
limits_CMS_5.SetLineWidth(2)
limits_CMS_5.SetLineStyle(9)
limits_CMS_5.Write()

limits_CDF_Run1 = TGraph("gBMZB_CDF_Run1.csv", "%lg %lg", ",")
limits_CDF_Run1.SetName('CDF_Run1')
limits_CDF_Run1.SetLineColor(ROOT.kRed-2)
limits_CDF_Run1.SetLineWidth(2)
limits_CDF_Run1.SetLineStyle(9)
limits_CDF_Run1.Write()


mass = array('d', range(500, 1300, 100))
xs_obs_limits = array('d', [2.95351, 1.28427, 0.660039, 1.0356, 0.504143,
                            0.43909, 0.401506, 0.250425, 0.186031, 0.104868, 0.0677886, 0.0521087])
xs_exp_limits = array(
    'd', [3.737775, 1.914845, 1.13629, 0.672481, 0.4831985, 0.3360895, 0.2663035, 0.207012])

xs_exp_limits_1sigma = array('d', [2.314797566, 1.411943314, 0.7084419502, 0.4583075586, 0.3427889568, 0.24039972, 0.1869526812, 0.159352872, 0.1168567102, 0.09070166502, 0.06638147704,
                                   0.04939500876, 0.1246133722, 0.1396474934, 0.1730244618, 0.2273564064, 0.300856536, 0.3704079632, 0.4766167574, 0.6473357134, 0.9978477006, 1.54054635, 2.633100772, 5.431141078])

xs_exp_limits_2sigma = array('d', [1.46345697, 1.116851336, 0.5770906232, 0.3316572308, 0.2316393044, 0.1905383264, 0.1479067596, 0.11764912, 0.09212326042, 0.06492590936, 0.0479290141,
                                   0.03720247206, 0.173813202, 0.198450278, 0.2412412426, 0.3438092378, 0.4010654584, 0.4768357028, 0.6622628554, 0.8958766546, 1.370757594, 2.279302618, 3.423436404, 7.553767386])

xs_obs_limits_0_07 = array('d', [1.62626, 0.719418, 0.431479, 0.675886, 0.319189,
                                 0.280534, 0.267076, 0.166265, 0.11402, 0.0727239, 0.0456865, 0.0353662])
xs_obs_limits_0_1 = array('d', [2.2091, 0.890212, 0.604036, 0.824481, 0.442209,
                                0.408836, 0.321403, 0.216742, 0.137407, 0.0833083, 0.0460332, 0.0398506])
xs_obs_limits_0_15 = array('d', [2.65642, 1.27498, 0.995386, 1.01219, 0.783474,
                                 0.609716, 0.429469, 0.276871, 0.140944, 0.0723732, 0.044647, 0.0497706])

CMS_19_fbinv = array('d', [])
CMS_19_fbinv_exp = array('d', [])
CMS_19_fbinv_1sigma_up = array('d', [])
CMS_19_fbinv_2sigma_up = array('d', [])
CMS_19_fbinv_1sigma_down = array('d', [])
CMS_19_fbinv_2sigma_down = array('d', [])
CMS_19_fbinv_0_07 = array('d', [])
CMS_19_fbinv_0_1 = array('d', [])
CMS_19_fbinv_0_15 = array('d', [])

splines_file = TFile("../scripts/gB_interpolation_inverse.root")


CMS_20_fbinv_paper = array('d', genfromtxt('CMS_20ifb.csv', delimiter=',').T[1])
limits_CMS_20_paper   = array("d", [])
limits_CMS_20_paper_2 = array("d", [])
mass_2 = [x for x in xrange(1200, 4000, 100)]

for i in mass_2:

    spline = splines_file.FindObjectAny('Spline_MZ_'+str(int(i)))
    idx = mass_2.index(i)
    
    #limit = spline.Eval(CMS_20_fbinv_paper[idx])
    #sigma_02 = spline_inverse(0.2, spline, float(1e-04))
    epsilon = float(1e-03)
    n = 0
    sigma_02 = 0
    y = 0.2
    #print i
    x_min = spline.GetXmin()
    x_max = spline.GetXmax()
    for j in linspace(x_min, x_max, int((x_max - x_min)/epsilon*10)):
    	
        if spline.Eval(j) < y + epsilon and spline.Eval(j) > y - epsilon:
            sigma_02 = j
            #print j, sigma_02, y - spline.Eval(j)
    if sigma_02 > 0.:
        limit = 0.2*(CMS_20_fbinv_paper[idx]/sigma_02)**0.5
    else:
        continue
    #print 'mass_2:', i, '\tlimit:', spline.Eval(CMS_20_fbinv_paper[idx]), "\tcalc_limit:", limit
    limits_CMS_20_paper.append(spline.Eval(CMS_20_fbinv_paper[idx]))
    print i, CMS_20_fbinv_paper[idx], limits_CMS_20_paper[-1]
    limits_CMS_20_paper_2.append(limit)


gr_limits_CMS_20_paper   = TGraph(len(limits_CMS_20_paper), array("d", mass_2), limits_CMS_20_paper)
gr_limits_CMS_20_paper_2 = TGraph(len(limits_CMS_20_paper_2), array("d", mass_2), limits_CMS_20_paper_2)

gr_limits_CMS_20_paper_2.SetName('CMS_20_fbinv_paper')
gr_limits_CMS_20_paper_2.SetLineColor(ROOT.kOrange)
gr_limits_CMS_20_paper_2.SetLineWidth(3)
#gr_limits_CMS_20_paper.Write()

print limits_CMS_20_paper
for i in xrange(len(mass)):
    print 'Spline_MZ_'+str(int(mass[i]))
    spline = splines_file.FindObjectAny('Spline_MZ_'+str(int(mass[i])))
    #gB_Limit = spline.Eval(xs_obs_limits[i])
    
    epsilon = float(1e-03)
    n = 0
    sigma_02 = 0
    y = 0.2
    #print i
    x_min = spline.GetXmin()
    x_max = spline.GetXmax()
    for j in linspace(x_min, x_max, int((x_max - x_min)/epsilon*10)):
        
        if spline.Eval(j) < y + epsilon and spline.Eval(j) > y - epsilon:
            sigma_02 = j
            #print j, sigma_02, y - spline.Eval(j)
    if sigma_02 > 0.:
        gB_Limit = 0.2*(xs_obs_limits[i]/sigma_02)**0.5
    else:
        continue
    #xsec_ref = spline.Eval(0.2)
    #gB_Limit = 0.2*math.sqrt(0.2*xs_obs_limits[i]/xsec_ref)
    CMS_19_fbinv.append(gB_Limit)

    gB_Limit = spline.Eval(xs_exp_limits[i])
    CMS_19_fbinv_exp.append(gB_Limit)

    gB_Limit = spline.Eval(xs_obs_limits_0_07[i])
    CMS_19_fbinv_0_07.append(gB_Limit)

    gB_Limit = spline.Eval(xs_obs_limits_0_1[i])
    CMS_19_fbinv_0_1.append(gB_Limit)

    gB_Limit = spline.Eval(xs_obs_limits_0_15[i])
    CMS_19_fbinv_0_15.append(gB_Limit)

    gB_Limit_1sigma_down = spline.Eval(xs_exp_limits_1sigma[i])
    gB_Limit_1sigma_up = spline.Eval(
        xs_exp_limits_1sigma[len(xs_exp_limits_1sigma)-1-i])

    CMS_19_fbinv_1sigma_up.append(gB_Limit_1sigma_up)
    CMS_19_fbinv_1sigma_down.append(gB_Limit_1sigma_down)

    gB_Limit_2sigma_down = spline.Eval(xs_exp_limits_2sigma[i])
    gB_Limit_2sigma_up = spline.Eval(
        xs_exp_limits_2sigma[len(xs_exp_limits_2sigma)-1-i])

    CMS_19_fbinv_2sigma_up.append(gB_Limit_2sigma_up)
    CMS_19_fbinv_2sigma_down.append(gB_Limit_2sigma_down)

    print mass[i], xs_exp_limits_1sigma[i], xs_obs_limits[i], xs_exp_limits_1sigma[len(xs_exp_limits_1sigma)-1-i], gB_Limit_1sigma_down, gB_Limit, gB_Limit_1sigma_up

CMS_19_fbinv_1sigma = CMS_19_fbinv_1sigma_down+CMS_19_fbinv_1sigma_up[::-1]
CMS_19_fbinv_2sigma = CMS_19_fbinv_2sigma_down+CMS_19_fbinv_2sigma_up[::-1]

print CMS_19_fbinv_1sigma

print mass, CMS_19_fbinv
splines_file.Close()

output_file.cd()
limits_CMS_19_fbinv = TGraph(len(CMS_19_fbinv), mass, CMS_19_fbinv)
limits_CMS_19_fbinv.SetName('CMS_19_fbinv')
limits_CMS_19_fbinv.SetLineColor(ROOT.kBlack)
limits_CMS_19_fbinv.SetLineWidth(3)
s = TSpline3("CMS_gB_Limit_spline", limits_CMS_19_fbinv)
s.Write()
limits_CMS_19_fbinv.Write()

limits_CMS_19_fbinv_exp = TGraph(len(CMS_19_fbinv_exp), mass, CMS_19_fbinv_exp)
limits_CMS_19_fbinv_exp.SetName('CMS_19_fbinv_exp')
limits_CMS_19_fbinv_exp.SetLineColor(ROOT.kBlack)
limits_CMS_19_fbinv_exp.SetLineWidth(2)
limits_CMS_19_fbinv_exp.SetLineStyle(7)
limits_CMS_19_fbinv_exp.Write()

limits_CMS_19_fbinv_0_07 = TGraph(
    len(CMS_19_fbinv_0_07), mass, CMS_19_fbinv_0_07)
limits_CMS_19_fbinv_0_07.SetName('CMS_19_fbinv_0_15')
limits_CMS_19_fbinv_0_07.SetLineColor(ROOT.kGreen)
limits_CMS_19_fbinv_0_07.SetLineWidth(3)
limits_CMS_19_fbinv_0_07.Write()

limits_CMS_19_fbinv_0_1 = TGraph(len(CMS_19_fbinv_0_1), mass, CMS_19_fbinv_0_1)
limits_CMS_19_fbinv_0_1.SetName('CMS_19_fbinv_0_1')
limits_CMS_19_fbinv_0_1.SetLineColor(ROOT.kBlue)
limits_CMS_19_fbinv_0_1.SetLineWidth(3)
limits_CMS_19_fbinv_0_1.Write()

limits_CMS_19_fbinv_0_15 = TGraph(
    len(CMS_19_fbinv_0_15), mass, CMS_19_fbinv_0_15)
limits_CMS_19_fbinv_0_15.SetName('CMS_19_fbinv_0_15')
limits_CMS_19_fbinv_0_15.SetLineColor(ROOT.kGreen)
limits_CMS_19_fbinv_0_15.SetLineWidth(3)
limits_CMS_19_fbinv_0_15.Write()

limits_CMS_19_fbinv_1sigma = TGraph(
    len(CMS_19_fbinv_1sigma), mass+mass[::-1], CMS_19_fbinv_1sigma)
limits_CMS_19_fbinv_1sigma.SetName('CMS_19_fbinv_0_15')
limits_CMS_19_fbinv_1sigma.SetLineColor(ROOT.kGreen)
limits_CMS_19_fbinv_1sigma.SetFillColor(ROOT.kGreen)
limits_CMS_19_fbinv_1sigma.SetFillColorAlpha(ROOT.kGreen, 0.5)
limits_CMS_19_fbinv_1sigma.SetLineWidth(2)
limits_CMS_19_fbinv_1sigma.Write()

limits_CMS_19_fbinv_2sigma = TGraph(
    len(CMS_19_fbinv_2sigma), mass+mass[::-1], CMS_19_fbinv_2sigma)
limits_CMS_19_fbinv_2sigma.SetName('CMS_19_fbinv_0_15')
limits_CMS_19_fbinv_2sigma.SetLineColor(ROOT.kYellow)
limits_CMS_19_fbinv_2sigma.SetFillColor(ROOT.kYellow)
limits_CMS_19_fbinv_2sigma.SetFillColorAlpha(ROOT.kYellow, 0.5)
limits_CMS_19_fbinv_2sigma.SetLineWidth(2)
limits_CMS_19_fbinv_2sigma.Write()


limits_CDF_1_1.Draw('AL')
limits_CMS_19_fbinv_2sigma.Draw('F SAME')
limits_CMS_19_fbinv_1sigma.Draw('F SAME')
limits_CMS_19_fbinv_exp.Draw('C SAME')
#limits_ATLAS_1.Draw('C SAME')
#limits_CMS_4.Draw('C SAME')
limits_UA2.Draw('C SAME')
limits_CMS_20.Draw('C SAME')
limits_ATLAS_13.Draw('C SAME')
#limits_CMS_013.Draw('C SAME')
#limits_CMS_5.Draw('C SAME')
limits_CDF_Run1.Draw('C SAME')

limits_CMS_19_fbinv.Draw('C SAME')
#gr_limits_CMS_20_paper.Draw('C SAME')
gr_limits_CMS_20_paper_2.Draw('C SAME')
#limits_CMS_19_fbinv_0_07.Draw('C SAME')
#limits_CMS_19_fbinv_0_1.Draw('C SAME')
#limits_CMS_19_fbinv_0_15.Draw('C SAME')

leg = TLegend(0.55, 0.20, 0.8, 0.65)
leg.AddEntry(limits_CDF_1_1, ' CDF 1.1 fb^{-1} (2009)', 'L')
#leg.AddEntry(limits_ATLAS_1, ' ATLAS 1 fb^{-1}', 'L')
#leg.AddEntry(limits_CMS_4,' CMS 4 fb^{-1}','L')
leg.AddEntry(limits_UA2, ' UA2 (1991-1993)', 'L')
leg.AddEntry(gr_limits_CMS_20_paper_2, ' CMS 20 fb^{-1}', 'L')
leg.AddEntry(limits_ATLAS_13, "#splitline{ATLAS 13 #oplus 20.3  fb^{-1}}{(with Gaussian resonance shapes)}", 'L')
#leg.AddEntry(limits_CMS_013,' CMS 0.13 fb^{-1}','L' )
#leg.AddEntry(limits_CMS_5,' CMS 5 fb^{-1}','L' )
leg.AddEntry(limits_CDF_Run1, ' CDF Run I (1990)', 'L')
leg.AddEntry(limits_CMS_19_fbinv, ' CMS 18.8 fb^{-1} (Data Scouting)', 'L')
leg.AddEntry(limits_CMS_19_fbinv_1sigma, '#pm 1 #sigma CMS Data Scouting', 'F')
leg.AddEntry(limits_CMS_19_fbinv_2sigma, '#pm 2 #sigma CMS Data Scouting', 'F')
#leg.AddEntry(limits_CMS_19_fbinv_0_07, ' CMS 18.8 fb^{-1} (Data Scouting-Gaussian 0.07)', 'L')
#leg.AddEntry(limits_CMS_19_fbinv_0_1, ' CMS 18.8 fb^{-1} (Data Scouting-Gaussian 0.10)', 'L')
#leg.AddEntry(limits_CMS_19_fbinv_0_15, ' CMS 18.8 fb^{-1} (Data Scouting-Gaussian 0.15)', 'L')

leg.SetFillColor(0)
leg.SetTextFont(42)
leg.SetTextSize(0.025)
leg.SetShadowColor(0)
leg.SetShadowColor(0)
leg.Draw()

lnote = TLatex()
lnote.SetTextAlign(12)
lnote.SetTextFont(42)
lnote.SetNDC()
lnote.SetTextSize(0.025)
lnote.SetTextAngle(90)
lnote.SetText(0.97, 0.15, "All except CMS 18.8 fb^{-1} and ATLAS 13#oplus20 fb^{-1} are taken from [21].")
#lnote.Draw()

limits_CDF_1_1.GetYaxis().SetRangeUser(0., 2.5)
limits_CDF_1_1.GetXaxis().SetLimits(200, 4000)
gPad.Update()

gPad.cd()
CMS_lumi.CMS_lumi(gPad, iPeriod, iPos)

gPad.RedrawAxis()

c1.Write()
output_file.Close()
#c1.SaveAs("gB_Limits_all.pdf")

#----- keep the GUI alive ------------
if __name__ == '__main__':
    rep = ''
    while not rep in ['q', 'Q']:
        rep = raw_input('enter "q" to quit: ')
        if 1 < len(rep):
            rep = rep[0]
