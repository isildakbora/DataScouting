import ROOT
import sys
import tdrStyle
import CMS_lumi
from ROOT import *
from rootutils import *
import math
import sys
import numpy as np

tdrStyle.setTDRStyle()
#gROOT.ProcessLine(".X ~/Dropbox/setTDRStyle.C")
gStyle.SetOptFit(1)
# gStyle.SetOptTitle(0)

# change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.extraText = ""
# used with iPeriod = 0, e.g. for simulation-only plots (default is an
# empty string)
CMS_lumi.lumi_sqrtS = "18.8 fb^{-1} (8 TeV)"
CMS_lumi.cmsTextFont = 62
CMS_lumi.cmsTextSize = 1.0
CMS_lumi.lumiTextSize = 0.8
iPos = 11
if(iPos == 0):
    CMS_lumi.relPosX = 0.08
iPeriod = 0

#input_root_file   = 'RUNBCD.root'
#input_root_file   = 'DataScouting_Bora040214_Run2012BCD_runrange_193834-208686_dijet.root'

input_root_file = 'latest_data/histo_RUNBCD.root'
input_directory = 'scoutingDiJetVariables'
fileNameSuffix = 'Run2012BCD'
input_2Dhistogram = 'h2_DetajjVsMjjWide;1'

minY_deta = 0.0
maxY_deta = 1.3
minX_mass = 386.
maxX_mass = 1856.
Lumi_Scouting_RUNB = 4412.
Lumi_Scouting_RUNC = 7055.
Lumi_Scouting_RUND = 7369.
lumi = Lumi_Scouting_RUNB + Lumi_Scouting_RUNC + Lumi_Scouting_RUND

# Fit functions
# 0: DEFAULT (4 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
# 1: VARIATION 1 (5 par.) - "( [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
#
# 2: VARIATION 2 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
#    -. 2nd order poly extension : inspired by HERA PDF 1.0 [http://arxiv.org/abs/arXiv:0911.0884 , Eq. 4.1]
#
# 3: VARIATION 3 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1])*exp([4]*x/8000)*TMath::Power(1+exp([5])*x/8000,[6]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
#    -. "exponential" extension wrt to DEFAULT - inspired by CTEQ 2008 [http://arxiv.org/pdf/hep-ph/0201195v3.pdf , Eq. 4]
#
# 4: VARIATION 4 (5 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)) )"
#    -. "log" extension wrt to DEFAULT
#
# 5: VARIATION 5 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)) )"
#    -. "log" extension wrt to DEFAULT
#
# 6: VARIATION 6 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)+[6]*TMath::Power(log(x/8000),4)) )"
#    -. "log" extension wrt to DEFAULT

FunctionType = int(sys.argv[1])

FunctionFormLatex = ["#frac{A(1-m_{jj}/#sqrt{s})^{B}}{(m_{jj}/#sqrt{s})^{C}}",  # 0
                     # 0
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})}}",
                     # 1
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}(1+Em_{jj}/#sqrt{s})}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})}}",
                     # 2
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}(1+Em_{jj}/#sqrt{s}+F(m_{jj}/#sqrt{s})^{2})}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})}}",
                     # 3
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}(1+Em_{jj}/#sqrt{s}+F(m_{jj}/#sqrt{s})^{2})+G(m_{jj}/#sqrt{s})^{3})}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})}}",
                     # 4
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}e^{E(m_{jj}/#sqrt{s})}(1+e^{F}m_{jj}/#sqrt{s})^{G}}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})}}",
                     # 5
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})+E.log^{2}(m_{jj}/#sqrt{s})}}",
                     # 6
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})+E.log^{2}(m_{jj}/#sqrt{s})+F.log^{3}(m_{jj}/#sqrt{s})}}",
                     "#frac{A(1-m_{jj}/#sqrt{s})^{B}}{(m_{jj}/#sqrt{s})^{C+D.log(m_{jj}/#sqrt{s})+E.log^{2}(m_{jj}/#sqrt{s})+F.log^{3}(m_{jj}/#sqrt{s})+G.log^{4}(m_{jj}/#sqrt{s})}}"]  # 7

FunctionForm = ["([0]*pow(1-x/8000,[1]))/(pow(x/8000,[2]))",  # -1
                # 0
                "([0]*pow(1-x/8000,[1]))/(pow(x/8000,[2]+[3]*log(x/8000)))",
                # 1
                "([0]*pow(1-x/8000,[1])*(1+[4]*x/8000))/(pow(x/8000,[2]+[3]*log(x/8000)))",
                # 2
                "([0]*pow(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)))/(pow(x/8000,[2]+[3]*log(x/8000)))",
                # 3
                "([0]*pow(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)+[6]*pow(x/8000,3)))/(pow(x/8000,[2]+[3]*log(x/8000)))",
                # 4
                "([0]*pow(1-x/8000,[1])*exp([4]*x/8000)*pow(1+exp([5])*x/8000,[6]))/(pow(x/8000,[2]+[3]*log(x/8000)))",
                # 5
                "([0]*pow(1-x/8000,[1]))/(pow(x/8000,[2]+[3]*log(x/8000)+[4]*pow(log(x/8000),2)))",
                # 6
                "([0]*pow(1-x/8000,[1]))/(pow(x/8000,[2]+[3]*log(x/8000)+[4]*pow(log(x/8000),2)+[5]*pow(log(x/8000),3)))",
                "([0]*pow(1-x/8000,[1]))/(pow(x/8000,[2]+[3]*log(x/8000)+[4]*pow(log(x/8000),2)+[5]*pow(log(x/8000),3)+[6]*pow(log(x/8000),4)))"]  # 7

print "FunctionType:", FunctionType, " FunctionForm:", FunctionForm[FunctionType+1]

massBins = array('d', [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530,
                       1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250, 7500, 7750, 8000])

number_of_variableWidth_bins = len(massBins) - 1

#=========================================================================
nPar = -1

# input file and 2D histo
file0 = TFile.Open(input_root_file)

DQMData_Merged_Runs_DataScouting_Run_summary_DiJet = file0.Get(input_directory)
# DQMData_Merged_Runs_DataScouting_Run_summary_DiJet.cd()
h_DEta_Mass = DQMData_Merged_Runs_DataScouting_Run_summary_DiJet.Get(
    input_2Dhistogram)

# find bin width
bin_width_X = float(h_DEta_Mass.GetXaxis().GetXmax() - h_DEta_Mass.GetXaxis().GetXmin()) / float(h_DEta_Mass.GetNbinsX())
bin_width_Y = float(h_DEta_Mass.GetYaxis().GetXmax() - h_DEta_Mass.GetYaxis().GetXmin()) / float(h_DEta_Mass.GetNbinsY())
print "bin_width_X: ", bin_width_X
print "bin_width_Y:",  bin_width_Y

minY_deta_bin_tmp = (minY_deta / bin_width_Y) + 1
maxY_deta_bin_tmp = maxY_deta / bin_width_Y
minY_deta_bin = int(minY_deta_bin_tmp)
maxY_deta_bin = int(maxY_deta_bin_tmp)
print "minY_deta_bin: ", minY_deta_bin
print "minY_deta_bin: ", maxY_deta_bin

# project 2D histogram on X axix in the y range specified
# h_DEta_Mass.ProjectionX("hist_mass",minY_deta_bin,maxY_deta_bin,"e")
hist_mass = file0.FindObjectAny('h1_MjjWide_finalSel')
hist_mass.GetXaxis().SetTitle("M_{jj} WideJets [GeV]")

# 01: DEFAULT (3 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / (
# TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
if FunctionType == -1:
    nPar = 3
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 2.702e-02/lumi)
    M1Bkg.SetParameter(1, 7.93e+00)
    M1Bkg.SetParameter(2, 5.67e+00)
    #M1Bkg.SetParameter(3, 0.98e-01)

# 0: DEFAULT (4 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / (
# TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
if FunctionType == 0:
    nPar = 4
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 2.702e-02/lumi)
    M1Bkg.SetParameter(1, 7.93e+00)
    M1Bkg.SetParameter(2, 5.67e+00)
    M1Bkg.SetParameter(3, 0.98e-01)

# 1: VARIATION 1 (5 par.) - "(
# [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000) ) / (
# TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
if FunctionType == 1:
    nPar = 5
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.005)
    M1Bkg.SetParameter(1, 9.3)
    M1Bkg.SetParameter(2, 7.2)
    M1Bkg.SetParameter(3, 0.4)
    M1Bkg.SetParameter(4, 3.1)

# 2: VARIATION 2 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
# 2nd order poly extension : inspired by HERA PDF 1.0
# [http://arxiv.org/abs/arXiv:0911.0884 , Eq. 4.1]
if FunctionType == 2:
    nPar = 6
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 5.8e-04)
    M1Bkg.SetParameter(1, 7.8e+00)
    M1Bkg.SetParameter(2, 7.3e+00)
    M1Bkg.SetParameter(3, 1.2e-01)
    M1Bkg.SetParameter(4, -1.3e+02)
    M1Bkg.SetParameter(5, -3.0e+02)

# 3: VARIATION 3 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1])*exp([4]*x/8000)*TMath::Power(1+exp([5])*x/8000,[6]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
# "exponential" extension wrt to DEFAULT - inspired by CTEQ 2008 [http://arxiv.org/pdf/hep-ph/0201195v3.pdf , Eq. 4]
if FunctionType == 3:
    nPar = 7
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.005)
    M1Bkg.SetParameter(1, 15.1)
    M1Bkg.SetParameter(2, 7.2)
    M1Bkg.SetParameter(3, 0.4)
    M1Bkg.SetParameter(4, 13.0)
    M1Bkg.SetParameter(5, -4.0)
    M1Bkg.SetParameter(6, 70.0)

if FunctionType == 4:
    nPar = 7
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.005)
    M1Bkg.SetParameter(1, 15.1)
    M1Bkg.SetParameter(2, 7.2)
    M1Bkg.SetParameter(3, 0.4)
    M1Bkg.SetParameter(4, 13.0)
    M1Bkg.SetParameter(5, -4.0)
    M1Bkg.SetParameter(6, 70.0)

# 4: VARIATION 4 (5 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)) )"
# "log" extension wrt to DEFAULT
if FunctionType == 5:
    nPar = 5
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.05)
    M1Bkg.SetParameter(1, 7.1)
    M1Bkg.SetParameter(2, 5.9)
    M1Bkg.SetParameter(3, 0.2)
    M1Bkg.SetParameter(4, 0.)

# 5: VARIATION 5 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)) )"
# "log" extension wrt to DEFAULT
if FunctionType == 6:
    nPar = 6
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 1.92457e-02)
    M1Bkg.SetParameter(1, 7.63876e+00)
    M1Bkg.SetParameter(2, 5.68472e+00)
    M1Bkg.SetParameter(3, 1.01222e-01)
    M1Bkg.SetParameter(4, 3.49455e-02)
    M1Bkg.SetParameter(5, 1.04755e-02)

# 6: VARIATION 6 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)+[6]*TMath::Power(log(x/8000),4)) )"
# "log" extension wrt to DEFAULT
if FunctionType == 7:
    nPar = 7
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.05)
    M1Bkg.SetParameter(1, 7.1)
    M1Bkg.SetParameter(2, 5.9)
    M1Bkg.SetParameter(3, 0.2)
    M1Bkg.SetParameter(4, 0.)
    M1Bkg.SetParameter(5, 0.)
    M1Bkg.SetParameter(6, 0.)

 # 7: VARIATION 7 (7 par.) - "([0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)+[6]*pow(x/8000,3)))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))"
 # "3rd order poly" extension wrt to DEFAULT
if FunctionType == 8:
    nPar = 7
    M1Bkg = TF1("M1Bkg", FunctionForm[FunctionType+1], minX_mass, maxX_mass)
    M1Bkg.SetParameter(0, 0.05)
    M1Bkg.SetParameter(1, 7.1)
    M1Bkg.SetParameter(2, 5.9)
    M1Bkg.SetParameter(3, 0.2)
    M1Bkg.SetParameter(4, 0.)
    M1Bkg.SetParameter(5, 0.)
    M1Bkg.SetParameter(6, 0.)
    M1Bkg.SetParameter(7, 0.)

# stopProgram = 1
# for loop in xrange(0, 20):
# 	r = hist_mass.Fit(M1Bkg,"LRSNQ")
# 	fitStatus = int(r)
# 	if fitStatus == 0:
# 		stopProgram = 0

# if stopProgram == 1:
# 	print  "######################"
# 	print  "######################"
# 	print  "ERROR : Fit failed!!!!"
# 	print  "######################"
# 	print  "######################"

 # calculate chi2 by hand for 1 GeV bin fit
# alpha 						 = 1 - 0.6827
# NumberOfObservations_FixBin = 0
# chi2_FixBin                 = 0.
# RSS_fixed                   = 0.

# for bin in xrange(hist_mass.GetNbinsX() + 1):
# 	if (hist_mass.GetXaxis().GetBinLowEdge(bin) >= minX_mass) and (hist_mass.GetXaxis().GetBinUpEdge(bin) <= maxX_mass):
# 		NumberOfObservations_FixBin += 1
# 		data     				    = hist_mass.GetBinContent(bin)
# 		err_data 					= hist_mass.GetBinError(bin)

# 		if data == 0:
# 			#err_data = 1.8
# 			continue
# 		if data < 1:
# 			data_L     = 0 if (data==0) else (ROOT.Math.gamma_quantile(alpha/2, data, 1.))
# 			data_U 	   = ROOT.Math.gamma_quantile_c(alpha/2, data+1, 1)
# 			err_data_l = data - data_L
# 			err_data_h = data_U - data
# 			err_data   = max(err_data_h,err_data_l)
# 		else:
# 			err_data = sqrt(data)

# 		fit 		=  M1Bkg.Eval(hist_mass.GetBinCenter(bin))
# 		fit 		=  M1Bkg.Integral(hist_mass.GetXaxis().GetBinLowEdge(bin), hist_mass.GetXaxis().GetBinUpEdge(bin) )
# 		fit 		=  fit / ( hist_mass.GetBinWidth(bin) )
# 		chi2_FixBin += (data - fit)**2 / err_data**2
# 		RSS_fixed 	+= (data - fit)**2

# ndf_FixBin = NumberOfObservations_FixBin - nPar -1
# print "============================"
# print "NumberOfObservations_FixBin: ", NumberOfObservations_FixBin
# print "ndf_FixBin: ",                  ndf_FixBin
# print "chi2_FixBin: ",             	   chi2_FixBin
# print "RSS_fixed: ", 			       RSS_fixed
# print "============================"
# hist_mass_varbin.Draw()

# make histogram with variable binning
hist_mass.Rebin(number_of_variableWidth_bins, "hist_mass_varbin", massBins)

for bin in xrange(0, hist_mass_varbin.GetNbinsX()+1):
    print hist_mass_varbin.GetBinLowEdge(bin), hist_mass_varbin.GetBinLowEdge(bin) + hist_mass_varbin.GetBinWidth(bin), hist_mass_varbin.GetBinContent(bin)
    current_bin_content = hist_mass_varbin.GetBinContent(bin)
    current_bin_error = hist_mass_varbin.GetBinError(bin)
    current_bin_width = float(hist_mass_varbin.GetBinWidth(bin))

    hist_mass_varbin.SetBinContent(
        bin, float(current_bin_content / (lumi * current_bin_width)))
    hist_mass_varbin.SetBinError(
        bin, float(current_bin_error / (lumi * current_bin_width)))

hist_fit_residual_vsMass = TH1D(
    "hist_fit_residual_vsMass", "hist_fit_residual_vsMass", number_of_variableWidth_bins, massBins)
hist_fit_residual = TH1D("hist_fit_residual", "hist_fit_residual", 50, -5, 5)
NumberOfObservations_VarBin = 0
chi2_VarBin = 0.
RSS_var = 0.

data = 0

for i in xrange(5):
    hist_mass_varbin.Fit(M1Bkg, "IMRNQ")
hist_mass_varbin.Fit(M1Bkg, "IMRN")

for bin in xrange(0, number_of_variableWidth_bins):

    if (hist_mass_varbin.GetXaxis().GetBinLowEdge(bin) >= minX_mass) and (hist_mass_varbin.GetXaxis().GetBinUpEdge(bin) <= maxX_mass):
        data = hist_mass_varbin.GetBinContent(bin)
        err_data = hist_mass_varbin.GetBinError(bin)

        if data == 0:
            NumberOfObservations_VarBin += 1
            continue

        NumberOfObservations_VarBin += 1
        fit = M1Bkg.Integral(hist_mass_varbin.GetXaxis().GetBinLowEdge(
            bin), hist_mass_varbin.GetXaxis().GetBinUpEdge(bin))
        fit = fit / (hist_mass_varbin.GetBinWidth(bin))

        err_tot = err_data
        fit_residual = (data - fit) / err_tot
        err_fit_residual = 1
        chi2_VarBin += (data - fit)**2 / err_data**2
        RSS_var += (data - fit)**2
        hist_fit_residual_vsMass.SetBinContent(bin, fit_residual)
        hist_fit_residual_vsMass.SetBinError(bin, err_fit_residual)
        hist_fit_residual_vsMass.GetXaxis().SetRangeUser(minX_mass, maxX_mass)
        hist_fit_residual.Fill(fit_residual)
        print hist_mass_varbin.GetXaxis().GetBinLowEdge(bin), hist_mass_varbin.GetXaxis().GetBinUpEdge(bin), data, err_data

ndf_VarBin = NumberOfObservations_VarBin - nPar
print "============================"
print "=== Function Type: ", 			   FunctionForm[FunctionType+1]
print "=== nPar: ", 					   nPar
print "=== NumberOfObservations_VarBin: ", NumberOfObservations_VarBin
print "=== ndf_VarBin: ",				   int(ndf_VarBin)
print "=== chi2_VarBin: ",				   chi2_VarBin
print "=== chi2_VarBin/ndf_VarBin: ", 	   chi2_VarBin/ndf_VarBin
print "=== Fit Probability: ",			   TMath.Prob(chi2_VarBin, ndf_VarBin)
print "=== RSS_var: ", 					   RSS_var
print "============================"
##########################################################################

xsec_lim_700 = float(open("../test/log_700_RSGravitonToQQbar.txt").readlines()[-6].split()[1])
xsec_lim_1200 = float(open("../test/log_1200_RSGravitonToQQbar.txt").readlines()[-6].split()[1])

signal_input_file = TFile.Open(
    "~/lxplus_workspace_fuse/CMSSW_7_0_7/test/LimitCode/Data_and_ResonanceShapes/widejets/Resonance_Shapes_RSGravitonToQQbar.root")
h_qq_700 = signal_input_file.FindObjectAny("h_qq_700")
h_qq_700.Scale(xsec_lim_700 )
h_qq_700 = th1_normalize_to_bins(h_qq_700, "h_qq_700")

h_qq_1200 = signal_input_file.FindObjectAny("h_qq_1200")
h_qq_1200.Scale(xsec_lim_1200)
h_qq_1200 = th1_normalize_to_bins(h_qq_1200, "h_qq_1200")

h_qq_700_res = h_qq_700.Clone("h_qq_700_res")
h_qq_700_res.Reset()

for bin_idx in xrange(h_qq_700.GetNbinsX()+1):
    x_bin_low   = h_qq_700.GetXaxis().GetBinLowEdge(bin_idx)
    x_bin_high  = h_qq_700.GetXaxis().GetBinUpEdge(bin_idx)
    x_bin_width = h_qq_700.GetBinWidth(bin_idx)
    bin_content = (lumi * x_bin_width) * h_qq_700.GetBinContent(bin_idx)
    bin_error   = (lumi * x_bin_width) * h_qq_700.GetBinError(bin_idx)
    fit_val     = lumi * M1Bkg.Integral(x_bin_low, x_bin_high)

    if not math.isnan(bin_content/(fit_val + bin_content)**0.5):
        h_qq_700_res.SetBinContent(
            bin_idx, bin_content/(fit_val + bin_content)**0.5)
        h_qq_700_res.SetBinError(
            bin_idx, bin_error/(fit_val + bin_content)**0.5)

h_qq_1200_res = h_qq_1200.Clone("h_qq_1200_res")
h_qq_1200_res.Reset()

for bin_idx in xrange(h_qq_1200.GetNbinsX()+1):
    x_bin_low = h_qq_1200.GetXaxis().GetBinLowEdge(bin_idx)
    x_bin_high = h_qq_1200.GetXaxis().GetBinUpEdge(bin_idx)
    x_bin_width = h_qq_1200.GetBinWidth(bin_idx)
    bin_content = (lumi * x_bin_width) * h_qq_1200.GetBinContent(bin_idx)
    bin_error = (lumi * x_bin_width) * h_qq_1200.GetBinError(bin_idx)
    fit_val = lumi * M1Bkg.Integral(x_bin_low, x_bin_high)

    if not math.isnan(bin_content/(fit_val + bin_content)**0.5):
        h_qq_1200_res.SetBinContent(
            bin_idx, bin_content/(fit_val + bin_content)**0.5)
        h_qq_1200_res.SetBinError(
            bin_idx, bin_error/(fit_val + bin_content)**0.5)

h_qq_700.GetXaxis().SetRangeUser(500., 900)
h_qq_1200.GetXaxis().SetRangeUser(1000., 1400)

# Draw plots
Canvas0 = TCanvas("Canvas0", "Canvas0", 11, 51, 700, 700)
Canvas0.cd()
Canvas0.SetLogy()
hist_mass.GetYaxis().SetTitle("Events")
hist_mass.Draw()
M1Bkg.SetLineColor(ROOT.kBlack)
M1Bkg.SetLineWidth(2)
M1Bkg.Draw("same")

print "NDF:", M1Bkg.GetNDF()
print "Chi^2:", M1Bkg.GetChisquare()
print "Probability:", M1Bkg.GetProb()

Canvas1 = TCanvas("Canvas1", "Canvas1", 11, 51, 750, 900)
pad1 = TPad("pad1", "pad1", 0, 0.3, 1, 1)
pad1.SetBottomMargin(0.03)
pad1.SetLogy()
# pad1.SetLogx()
pad1.Draw()
pad1.cd()
hist_mass_varbin.GetYaxis().SetTitle("d#sigma / dm_{jj} [pb/GeV]")
hist_mass_varbin.GetYaxis().SetTitleSize(0.06)
hist_mass_varbin.GetYaxis().SetLabelSize(0.05)
hist_mass_varbin.GetXaxis().SetMoreLogLabels()
hist_mass_varbin.GetXaxis().SetNoExponent()
hist_mass_varbin.GetXaxis().SetTitle("")
hist_mass_varbin.GetXaxis().SetLabelColor(ROOT.kWhite)
hist_mass_varbin.GetXaxis().SetRangeUser(minX_mass, maxX_mass)
hist_mass_varbin.GetYaxis().SetRangeUser(6e-06, 5e+02)
hist_mass_varbin.SetMarkerStyle(20)
hist_mass_varbin.SetMarkerSize(1.2)
hist_mass_varbin.SetLineColor(ROOT.kBlack)
hist_mass_varbin.SetBinErrorOption(TH1.kPoisson)
hist_mass_varbin.Draw("E1")
hist_mass_varbin_new = hist_mass_varbin.Clone("hist_mass_varbin_new")
M1Bkg.SetLineColor(ROOT.kRed)
M1Bkg.SetLineWidth(2)
M1Bkg.SetLineColor(ROOT.kRed+1)
M1Bkg.Draw("same")


h_qq_700.SetLineColor(ROOT.kGreen)
h_qq_700.SetLineWidth(2)
h_qq_700.SetLineStyle(5)
h_qq_700.Draw("same histc")

h_qq_1200.SetLineColor(ROOT.kPink + 9)
h_qq_1200.SetLineWidth(2)
h_qq_1200.SetLineStyle(5)
h_qq_1200.Draw("same histc")

leg = TLegend(0.50, 0.65, 0.90, 0.90)
leg.AddEntry(hist_mass_varbin, "Data", 'lpe1')
leg.AddEntry(M1Bkg, "Background fit", 'l')
leg.AddEntry(h_qq_700, "Z'_{B} (M = 700 GeV, g_{B} = 0.37)", 'lp')
leg.AddEntry(h_qq_1200, "Z'_{B} (M = 1200 GeV, g_{B} = 0.84)", 'lp')

#gPad.RedrawAxis()

leg.SetFillColorAlpha(0, 0)
leg.SetTextFont(42)
leg.SetTextColor(ROOT.kBlack)
leg.SetTextSize(0.035)
leg.SetShadowColor(0)
leg.SetLineColor(ROOT.kWhite)
leg.Draw()

lstat = TLatex()
lstat.SetTextAlign(12)
lstat.SetTextFont(42)
lstat.SetNDC()
lstat.SetTextSize(0.03)

x_latex_pos_left = 0.60
y_latex_pos_up = 0.90

# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-0*0.05, "A   = " + "%.5e" % M1Bkg.GetParameter(0) + " #pm %.5e" % M1Bkg.GetParError(0))
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-1*0.05, "B   = " + "%.5e" % M1Bkg.GetParameter(1) + " #pm %.5e" % M1Bkg.GetParError(1))
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-2*0.05, "C   = " + "%.5e" % M1Bkg.GetParameter(2) + " #pm %.5e" % M1Bkg.GetParError(2))
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-3*0.05, "D   = " + "%.5e" % M1Bkg.GetParameter(3) + " #pm %.5e" % M1Bkg.GetParError(3))
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-4*0.05, " ")
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-5*0.05, "#chi^{2}       = "+"%.4f" % M1Bkg.GetChisquare() )
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-6*0.05, "ndf      = " + "%i" % M1Bkg.GetNDF() )
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-7*0.05, "#chi^{2}/ndf = " + "%.4f" % (M1Bkg.GetChisquare()/M1Bkg.GetNDF()) )
# lstat.DrawLatex(x_latex_pos_left, y_latex_pos_up-8*0.05, "Prob   = " + "%.4f" % M1Bkg.GetProb() )

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
# l1.SetTextColor(ROOT.kAzure-7)
l1.SetNDC()
l1.SetTextSize(0.05)
l1.DrawLatex(0.20, 0.17, "Wide jets")

l2 = TLatex()
l2.SetTextAlign(12)
l2.SetTextFont(42)
# l2.SetTextColor(ROOT.kAzure-7)
l2.SetNDC()
l2.SetTextSize(0.05)
l2.DrawLatex(0.20, 0.10, "|#eta| < 2.5, |#Delta#eta_{jj}| < 1.3")
# if FunctionType == 1 or FunctionType == 2 or FunctionType == 3:
# 	l1.DrawLatex(0.27, 0.38, "Type I Fit Function")
# elif FunctionType == 4 or FunctionType == 5 or FunctionType == 6:
# 	l1.DrawLatex(0.27, 0.38, "Type II Fit Function")
# else:
# 	l1.DrawLatex(0.27, 0.38, "Default Fit Function")

# l2 = TLatex()
# l2.SetTextAlign(12)
# l2.SetTextFont(42)
# l2.SetNDC()
# l2.SetTextSize(0.05)
# l2.DrawLatex(0.27, 0.27, FunctionFormLatex[FunctionType+1])

Canvas1.cd()
pad2 = TPad("pad2", "pad2", 0, 0, 1, 0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.35)
# pad2.SetLogx()
pad2.SetGridx()
pad2.SetGridy()
pad2.Draw()
pad2.cd()
hist_fit_residual_vsMass.GetXaxis().SetTitleSize(0.15)
hist_fit_residual_vsMass.GetXaxis().SetLabelSize(0.10)
hist_fit_residual_vsMass.GetYaxis().SetLabelSize(0.08)
hist_fit_residual_vsMass.GetYaxis().SetTitleSize(0.06)
hist_fit_residual_vsMass.GetYaxis().SetTitleOffset(0.60)
hist_fit_residual_vsMass.GetYaxis().SetRangeUser(-3.1, 3.5)
hist_fit_residual_vsMass.GetYaxis().SetTitle(
    "#frac{(Data-Fit)}{#sigma_{stat}}")
hist_fit_residual_vsMass.GetYaxis().SetTitleSize(0.10)
hist_fit_residual_vsMass.GetYaxis().CenterTitle()
hist_fit_residual_vsMass.GetYaxis().SetTickLength(hist_mass_varbin.GetXaxis().GetTickLength())
hist_fit_residual_vsMass.GetXaxis().SetRangeUser(minX_mass, maxX_mass)
hist_fit_residual_vsMass.GetXaxis().SetTitle("Dijet mass [GeV]")
hist_fit_residual_vsMass.SetFillColor(ROOT.kRed)
hist_fit_residual_vsMass.SetLineColor(ROOT.kBlack)
hist_fit_residual_vsMass.Draw("HIST")

h_qq_700_res.SetLineStyle(8)
h_qq_700_res.SetLineWidth(2)
h_qq_700_res.SetLineColor(ROOT.kGreen)
h_qq_700_res.GetXaxis().SetRangeUser(500., 900.)
h_qq_700_res.Draw("SAME HISTC")

h_qq_1200_res.SetLineStyle(8)
h_qq_1200_res.SetLineWidth(2)
h_qq_1200_res.SetLineColor(ROOT.kPink + 9)
h_qq_1200_res.GetXaxis().SetRangeUser(1000., 1400.)
h_qq_1200_res.Draw("SAME HISTC")

# draw the lumi text on the canvas
pad1.cd()
CMS_lumi.CMS_lumi(pad1, iPeriod, iPos)
gPad.RedrawAxis()

Canvas3 = TCanvas("Canvas3", "Canvas3", 11, 51, 600, 600)
Canvas3.cd()
hist_fit_residual.GetXaxis().SetTitle("(data - fit) / #sqrt{data}")
hist_fit_residual.GetYaxis().SetTitle("Number of bins")
hist_fit_residual.GetYaxis().SetRangeUser(0, number_of_variableWidth_bins/3)
hist_fit_residual.Draw()
hist_fit_residual.Fit("gaus", "L", "", -3, 3)

# Output files
output_root_file = "dijetFitResults_FuncType" + \
    str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+".root"
f_output = TFile.Open(output_root_file, "RECREATE")
M1Bkg.Write()
hist_mass_varbin_new.Write()
Canvas0.Write()
Canvas1.Write()
Canvas3.Write()
h_qq_700_res.Write()
f_output.Close()

# Save figures from canvas
c0_fileName = "dijetmass_FuncType" + \
    str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c1_fileName = "dijetmass_varbin_FuncType" + \
    str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c2_fileName = "fitresiduals_vs_mass_FuncType" + \
    str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c3_fileName = "fitresiduals_FuncType" + \
    str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"

Canvas0.SaveAs(c0_fileName)
Canvas1.SaveAs(c1_fileName)
Canvas3.SaveAs(c3_fileName)

Canvas0.SaveAs(c0_fileName.replace("png", "pdf"))
Canvas1.SaveAs(c1_fileName.replace("png", "pdf"))
Canvas3.SaveAs(c3_fileName.replace("png", "pdf"))

keepGUIalive()
