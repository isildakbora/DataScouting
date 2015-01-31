import ROOT, sys
from ROOT import *
from rootutils import *
import math, sys, numpy as np
from setTDRStyle import setTDRStyle


#gStyle.SetOptFit(1)
gStyle.SetOptTitle(0)

input_root_file   = "/afs/cern.ch/user/i/isildak/public/DataScouting/RUNBCD.root"
#input_root_file   = "histo.root"
input_directory   = "scoutingDiJetVariables"
fileNameSuffix    = "Run2012BCD"
input_2Dhistogram = "h2_DetajjVsMjjWide;1"

minY_deta = 0.
maxY_deta = 1.3
minX_mass = 354.
maxX_mass = 5500.

#Fit functions
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

FunctionFormLatex = ["#frac{A(1-x/#sqrt{s})^{B}}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}(1+Ex/#sqrt{s})}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}(1+Ex/#sqrt{s}+F(x/#sqrt{s})^{2})}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}(1+Ex/#sqrt{s}+F(x/#sqrt{s})^{2})+G(x/#sqrt{s})^{3})}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}e^{E(x/#sqrt{s})}(1+e^{F})^G}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})+E.log^{2}(x/#sqrt{s})+F.log^{3}(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})+E.log^{2}(x/#sqrt{s})+F.log^{3}(x/#sqrt{s})+G.log^{4}(x/#sqrt{s})}}",
					 "#frac{A(1-x/#sqrt{s})^{B}}{(x/#sqrt{s})^{C+D.log(x/#sqrt{s})+E.log^{2}(x/#sqrt{s})+F.log^{3}(x/#sqrt{s})+G.log^{4}(x/#sqrt{s})}}"]

FunctionType = int(sys.argv[1])
FunctionForm = ["([0]*TMath::Power(1-x/8000,[1]))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))",
                "([0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))",
 				"([0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))",
 				"([0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)++[6]*pow(x/8000,3)))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))",
 				"([0]*TMath::Power(1-x/8000,[1])*exp([4]*x/8000)*TMath::Power(1+exp([5])*x/8000,[6]))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))",
 				"([0]*TMath::Power(1-x/8000,[1]))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)))",
 				"([0]*TMath::Power(1-x/8000,[1]))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)))",
 				"([0]*TMath::Power(1-x/8000,[1]))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)+[6]*TMath::Power(log(x/8000),4)))",
 				"([0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)+[6]*pow(x/8000,3)))/(TMath::Power(x/8000,[2]+[3]*log(x/8000)))"]

print "FunctionType:", FunctionType, " FunctionForm:", FunctionForm[FunctionType]

massBins = array('d', [1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250,7500,7750,8000])

number_of_variableWidth_bins = len(massBins) - 1

#================================================================================================================
nPar=-1; 

### input file and 2D histo
file0 = TFile.Open( input_root_file )

DQMData_Merged_Runs_DataScouting_Run_summary_DiJet = file0.Get( input_directory )
#DQMData_Merged_Runs_DataScouting_Run_summary_DiJet.cd();
h_DEta_Mass = DQMData_Merged_Runs_DataScouting_Run_summary_DiJet.Get( input_2Dhistogram ) 

### find bin width  
bin_width_X = float( h_DEta_Mass.GetXaxis().GetXmax() - h_DEta_Mass.GetXaxis().GetXmin() ) / float ( h_DEta_Mass.GetNbinsX() )
bin_width_Y = float ( h_DEta_Mass.GetYaxis().GetXmax() - h_DEta_Mass.GetYaxis().GetXmin() ) / float ( h_DEta_Mass.GetNbinsY() )
print "bin_width_X: ", bin_width_X
print "bin_width_Y:",  bin_width_Y

minY_deta_bin_tmp = (minY_deta / bin_width_Y) + 1
maxY_deta_bin_tmp = maxY_deta / bin_width_Y
minY_deta_bin = int(minY_deta_bin_tmp)
maxY_deta_bin = int(maxY_deta_bin_tmp)
print "minY_deta_bin: ", minY_deta_bin
print "minY_deta_bin: ", maxY_deta_bin

### project 2D histogram on X axix in the y range specified
hist_mass = h_DEta_Mass.ProjectionX("hist_mass",minY_deta_bin,maxY_deta_bin,"e");
hist_mass.GetXaxis().SetTitle("M_{jj} WideJets [GeV]")

#0: DEFAULT (4 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )" 
if FunctionType == 0:
	nPar  = 4
	M1Bkg = TF1("M1Bkg", FunctionForm[0], minX_mass, maxX_mass)
	M1Bkg.SetParameter(0, 4.57e-03)
	M1Bkg.SetParameter(1, 6.79e+00)
	M1Bkg.SetParameter(2, 6.81e+00)
	M1Bkg.SetParameter(3, 3.11e-01)
	M1Bkg.SetParLimits(3, 0,0.4)

#1: VARIATION 1 (5 par.) - "( [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
if FunctionType == 1:
	nPar  = 5
	M1Bkg = TF1("M1Bkg", FunctionForm[1], minX_mass, maxX_mass)
	M1Bkg.SetParameter(0, 0.005)
	M1Bkg.SetParameter(1, 9.3)
	M1Bkg.SetParameter(2, 7.2)
	M1Bkg.SetParameter(3, 0.4)
	M1Bkg.SetParameter(4, 3.1)

#2: VARIATION 2 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1])*(1+[4]*x/8000+[5]*pow(x/8000,2)) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
#2nd order poly extension : inspired by HERA PDF 1.0 [http://arxiv.org/abs/arXiv:0911.0884 , Eq. 4.1]
if FunctionType == 2:
	nPar  = 6
	M1Bkg =  TF1("M1Bkg", FunctionForm[2], minX_mass, maxX_mass)
	M1Bkg.SetParameter(0, 5.8e-04)
	M1Bkg.SetParameter(1, 7.8e+00)
	M1Bkg.SetParameter(2, 7.3e+00)
	M1Bkg.SetParameter(3, 1.2e-01)
	M1Bkg.SetParameter(4, -1.3e+02)
	M1Bkg.SetParameter(5, -3.0e+02)

#3: VARIATION 3 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1])*exp([4]*x/8000)*TMath::Power(1+exp([5])*x/8000,[6]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)) )"
# "exponential" extension wrt to DEFAULT - inspired by CTEQ 2008 [http://arxiv.org/pdf/hep-ph/0201195v3.pdf , Eq. 4]
if FunctionType == 3:
	nPar  = 7
	M1Bkg = TF1("M1Bkg", FunctionForm[3], minX_mass, maxX_mass);
	M1Bkg.SetParameter(0, 0.005)
	M1Bkg.SetParameter(1, 15.1)
	M1Bkg.SetParameter(2, 7.2)
	M1Bkg.SetParameter(3, 0.4)
	M1Bkg.SetParameter(4, 13.0)
	M1Bkg.SetParameter(5, -4.0)
	M1Bkg.SetParameter(6, 70.0)

if FunctionType == 4:
	nPar  = 7
	M1Bkg = TF1("M1Bkg", FunctionForm[4], minX_mass, maxX_mass);
	M1Bkg.SetParameter(0, 0.005)
	M1Bkg.SetParameter(1, 15.1)
	M1Bkg.SetParameter(2, 7.2)
	M1Bkg.SetParameter(3, 0.4)
	M1Bkg.SetParameter(4, 13.0)
	M1Bkg.SetParameter(5, -4.0)
	M1Bkg.SetParameter(6, 70.0)

#4: VARIATION 4 (5 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)) )" 
# "log" extension wrt to DEFAULT     
if FunctionType == 5:
	nPar  = 5
  	M1Bkg = TF1("M1Bkg", FunctionForm[4], minX_mass, maxX_mass)
  	M1Bkg.SetParameter(0, 0.05)
  	M1Bkg.SetParameter(1, 7.1)
  	M1Bkg.SetParameter(2, 5.9)
  	M1Bkg.SetParameter(3, 0.2)
  	M1Bkg.SetParameter(4, 0.);
 
#5: VARIATION 5 (6 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)) )" 
# "log" extension wrt to DEFAULT     
if FunctionType == 6:
	nPar  = 6
	M1Bkg = TF1("M1Bkg", FunctionForm[5], minX_mass, maxX_mass)
	M1Bkg.SetParameter(0, 1.92457e-02)
	M1Bkg.SetParameter(1, 7.63876e+00)
	M1Bkg.SetParameter(2, 5.68472e+00)
	M1Bkg.SetParameter(3, 1.01222e-01)
	M1Bkg.SetParameter(4, 3.49455e-02)
	M1Bkg.SetParameter(5, 1.04755e-02)

# 6: VARIATION 6 (7 par.) - "( [0]*TMath::Power(1-x/8000,[1]) ) / ( TMath::Power(x/8000,[2]+[3]*log(x/8000)+[4]*TMath::Power(log(x/8000),2)+[5]*TMath::Power(log(x/8000),3)+[6]*TMath::Power(log(x/8000),4)) )" 
# "log" extension wrt to DEFAULT     
if FunctionType == 7:
	nPar  = 7
	M1Bkg = TF1("M1Bkg", FunctionForm[6], minX_mass, maxX_mass)
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
	nPar  = 7
	M1Bkg = TF1("M1Bkg", FunctionForm[7], minX_mass, maxX_mass)
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

 ### calculate chi2 by hand for 1 GeV bin fit
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

#make histogram with variable binning
hist_mass.Rebin( number_of_variableWidth_bins, "hist_mass_varbin", massBins)

#hist_mass_varbin.Draw()

for bin in xrange(0, hist_mass_varbin.GetNbinsX()+1):
	print hist_mass_varbin.GetBinLowEdge(bin), hist_mass_varbin.GetBinLowEdge(bin) + hist_mass_varbin.GetBinWidth(bin), hist_mass_varbin.GetBinContent(bin)
	current_bin_content = hist_mass_varbin.GetBinContent(bin)
	current_bin_error   = hist_mass_varbin.GetBinError(bin)
	current_bin_width   = hist_mass_varbin.GetBinWidth(bin)

	hist_mass_varbin.SetBinContent( bin, float(current_bin_content / current_bin_width) )
	hist_mass_varbin.SetBinError( bin, float( current_bin_error / current_bin_width ) )

hist_fit_residual_vsMass    = TH1D("hist_fit_residual_vsMass", "hist_fit_residual_vsMass", number_of_variableWidth_bins,massBins)
hist_fit_residual           = TH1D("hist_fit_residual", "hist_fit_residual", 10, -5, 5)
NumberOfObservations_VarBin = 0
chi2_VarBin  				= 0.
RSS_var 					= 0.

data = 0

for i in xrange(20):
	hist_mass_varbin.Fit(M1Bkg,"LIMRNSQ")
hist_mass_varbin.Fit(M1Bkg,"LIMRNS")

for bin in xrange(0, number_of_variableWidth_bins):
	
	if (hist_mass_varbin.GetXaxis().GetBinLowEdge(bin) >= minX_mass) and (hist_mass_varbin.GetXaxis().GetBinUpEdge(bin) <= maxX_mass):
		data     = hist_mass_varbin.GetBinContent(bin)
		err_data = hist_mass_varbin.GetBinError(bin)
	
		if data == 0:
			NumberOfObservations_VarBin += 1
			continue

		NumberOfObservations_VarBin += 1
		fit = M1Bkg.Integral(hist_mass_varbin.GetXaxis().GetBinLowEdge(bin), hist_mass_varbin.GetXaxis().GetBinUpEdge(bin) )
		fit = fit / ( hist_mass_varbin.GetBinWidth(bin) )

		err_tot                 = err_data
		fit_residual            = (data - fit) / err_tot
		err_fit_residual 		= 1
		chi2_VarBin             += (data - fit)**2 / err_data**2
		RSS_var   			    += (data - fit)**2
		hist_fit_residual_vsMass.SetBinContent(bin,fit_residual)
		hist_fit_residual_vsMass.SetBinError(bin,err_fit_residual)
		hist_fit_residual_vsMass.GetXaxis().SetRangeUser(minX_mass,maxX_mass)
		hist_fit_residual.Fill(fit_residual)
		print hist_mass_varbin.GetXaxis().GetBinLowEdge(bin), hist_mass_varbin.GetXaxis().GetBinUpEdge(bin), data , err_data 

ndf_VarBin = NumberOfObservations_VarBin - nPar
print "============================"
print "=== Function Type: ", 			   FunctionForm[FunctionType]
print "=== nPar: ", 					   nPar
print "=== NumberOfObservations_VarBin: ", NumberOfObservations_VarBin
print "=== ndf_VarBin: ",				   int(ndf_VarBin)
print "=== chi2_VarBin: ",				   chi2_VarBin
print "=== chi2_VarBin/ndf_VarBin: ", 	   chi2_VarBin/ndf_VarBin
print "=== Fit Probability: ",			   TMath.Prob(chi2_VarBin, ndf_VarBin)
print "=== RSS_var: ", 					   RSS_var
print "============================"

### Draw plots
Canvas0 = TCanvas("Canvas0","Canvas0",11,51,700,700)
Canvas0.cd()
Canvas0.SetLogy()
hist_mass.GetYaxis().SetTitle("Events")
hist_mass.Draw()
M1Bkg.SetLineColor(1)
M1Bkg.SetLineWidth(2)
M1Bkg.Draw("same")

print "NDF:", M1Bkg.GetNDF()
print "Chi^2:", M1Bkg.GetChisquare()    
print "Probability:", M1Bkg.GetProb()

Canvas1 = TCanvas("Canvas1","Canvas1",11,51,800,800)
pad1    = TPad("pad1","pad1",0,0.3,1,1)
pad1.SetBottomMargin(0)
pad1.SetLogy()
pad1.SetLogx()
pad1.Draw()
pad1.cd()
hist_mass_varbin.GetYaxis().SetTitle("Events / bin width")
hist_mass_varbin.GetXaxis().SetTitleSize(0.06)
hist_mass_varbin.GetXaxis().SetMoreLogLabels()
hist_mass_varbin.GetXaxis().SetNoExponent()
hist_mass_varbin.GetXaxis().SetRangeUser(minX_mass, maxX_mass)
hist_mass_varbin.SetMarkerStyle(20)
hist_mass_varbin.SetMarkerSize(1.2)
hist_mass_varbin.SetLineColor(kBlack)
hist_mass_varbin.SetBinErrorOption(TH1.kPoisson)
hist_mass_varbin.Draw("E1")
hist_mass_varbin_new = hist_mass_varbin.Clone("hist_mass_varbin_new")
M1Bkg.SetLineColor(ROOT.kRed)
M1Bkg.SetLineWidth(2)
M1Bkg.SetLineColor(ROOT.kRed+1)
M1Bkg.Draw("same")
  
lstat = TLatex()
lstat.SetTextAlign(12)
lstat.SetTextFont(42)
lstat.SetNDC()
lstat.SetTextSize(0.03)

lstat.DrawLatex(0.7, 0.80, "#chi^{2}       = "+"%.4f" % M1Bkg.GetChisquare() )
lstat.DrawLatex(0.7, 0.75, "ndf      = " + "%i" % M1Bkg.GetNDF() )
lstat.DrawLatex(0.7, 0.70, "#chi^{2}/ndf = " + "%.4f" % (M1Bkg.GetChisquare()/M1Bkg.GetNDF()) )
lstat.DrawLatex(0.7, 0.65, "Prob   = " + "%.4f" % M1Bkg.GetProb() )

l1 = TLatex()
l1.SetTextAlign(12)
l1.SetTextFont(42)
l1.SetTextColor(ROOT.kAzure-7)
l1.SetNDC()
l1.SetTextSize(0.05)
if FunctionType == 1 or FunctionType == 2 or FunctionType == 3:
	l1.DrawLatex(0.17, 0.38, "Type I Fit Function")
elif FunctionType == 4 or FunctionType == 5 or FunctionType == 6:
	l1.DrawLatex(0.17, 0.38, "Type II Fit Function")
else:
	l1.DrawLatex(0.17, 0.38, "Default Fit Function")

l2 = TLatex()
l2.SetTextAlign(12)
l2.SetTextFont(42)
l2.SetTextColor(ROOT.kAzure-7)
l2.SetNDC()
l2.SetTextSize(0.03)
l2.DrawLatex(0.17, 0.27, FunctionFormLatex[FunctionType])

Canvas1.cd()
pad2 = TPad("pad2","pad2",0 ,0 ,1 , 0.3)
pad2.SetTopMargin(0)
pad2.SetBottomMargin(0.35)
pad2.SetLogx()
pad2.Draw()
pad2.cd()
hist_fit_residual_vsMass.GetYaxis().SetLimits(-5, 5)
hist_fit_residual_vsMass.GetYaxis().SetRangeUser(-5, 5)
hist_fit_residual_vsMass.GetYaxis().SetTitle("(data - fit) / #sqrt{data}")
hist_fit_residual_vsMass.GetXaxis().SetRangeUser(minX_mass, maxX_mass)
hist_fit_residual_vsMass.GetXaxis().SetTitle("M_{jj} WideJets [GeV]")
hist_fit_residual_vsMass.SetFillColor(ROOT.kRed)
hist_fit_residual_vsMass.Draw("HIST")

Canvas3 = TCanvas("Canvas3","Canvas3",11, 51, 600, 600)
Canvas3.cd()
hist_fit_residual.GetXaxis().SetTitle("(data - fit) / #sqrt{data}")
hist_fit_residual.GetYaxis().SetTitle("Number of bins")
hist_fit_residual.GetYaxis().SetRangeUser(0,number_of_variableWidth_bins/3)
hist_fit_residual.Draw()
hist_fit_residual.Fit("gaus","L","",-3, 3)

### Output files
output_root_file = "dijetFitResults_FuncType"+str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+".root" 
f_output 		 = TFile.Open(output_root_file,"RECREATE")
M1Bkg.Write()
hist_mass_varbin_new.Write()
Canvas0.Write()
Canvas1.Write()
Canvas3.Write()
f_output.Close()

### Save figures from canvas
c0_fileName = "dijetmass_FuncType"+str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c1_fileName = "dijetmass_varbin_FuncType"+str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c2_fileName = "fitresiduals_vs_mass_FuncType"+str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"
c3_fileName = "fitresiduals_FuncType"+str(FunctionType)+"_nParFit"+str(nPar)+"_"+fileNameSuffix+"_extended.png"

Canvas0.SaveAs(c0_fileName)
Canvas1.SaveAs(c1_fileName)
Canvas3.SaveAs(c3_fileName)

Canvas0.SaveAs(c0_fileName.replace("png", "pdf"))
Canvas1.SaveAs(c1_fileName.replace("png", "pdf"))
Canvas3.SaveAs(c3_fileName.replace("png", "pdf"))

keepGUIalive()

