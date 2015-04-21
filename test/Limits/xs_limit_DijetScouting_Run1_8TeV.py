#!/usr/bin/env python

import sys, os, subprocess, string, re
from ROOT import *
from array import array
import CMS_lumi

CMS_lumi.extraText = "Preliminary"
CMS_lumi.lumi_sqrtS = "18.8 fb^{-1} (8 TeV)" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
iPos = 11
iPeriod = 0

import optparse
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage)

parser.add_option("--runthecode",action="store",type="int",dest="runthecode",default=0)

(options, args) = parser.parse_args()

runthecode = options.runthecode

gROOT.SetBatch(kTRUE);
gStyle.SetOptStat(0)
gStyle.SetOptTitle(0)
gStyle.SetTitleFont(42, "XYZ")
gStyle.SetTitleSize(0.06, "XYZ")
gStyle.SetLabelFont(42, "XYZ")
gStyle.SetLabelSize(0.05, "XYZ")
gStyle.SetCanvasBorderMode(0)
gStyle.SetFrameBorderMode(0)
gStyle.SetCanvasColor(kWhite)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)
gStyle.SetPadLeftMargin(0.15)
gStyle.SetPadRightMargin(0.05)
gStyle.SetPadTopMargin(0.05)
gStyle.SetPadBottomMargin(0.15)
gROOT.ForceStyle()

masses = array('d')
xs_obs_limits = array('d')
xs_exp_limits = array('d')
masses_exp = array('d')
xs_exp_limits_1sigma = array('d')
xs_exp_limits_1sigma_up = array('d')
xs_exp_limits_2sigma = array('d')
xs_exp_limits_2sigma_up = array('d')

#signal_mass = [2000, 3000, 4000, 5500]
signal_mass = [500, 600, 700, 800, 900, 1000]
#signal_mass = [300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000]

plot_exp = True

#######################################################
# Uncomment this part if running the limit code

print 'runthecode', runthecode
### for running the limit code
if runthecode == 1:
  for mass in signal_mass:
    print mass
    masses.append(mass)
    masses_exp.append(mass)

    cmd = "./stats " + str(mass)
    print "Running: " + cmd
    proc = subprocess.Popen( cmd, shell=True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT )
    output = proc.communicate()[0]
    if proc.returncode != 0:
      print output
      sys.exit(1)
    print output

    outputlines = output.split("\n")

    for line in outputlines:
      if re.search("observed bound =", line):
        xs_obs_limits.append(float(line.split()[6]))
      if plot_exp:
        if re.search("median:", line):
          xs_exp_limits.append(float(line.split()[1]))
        if re.search("1 sigma band:", line):
          xs_exp_limits_1sigma.append(float(line.split()[4]))
          xs_exp_limits_1sigma_up.append(float(line.split()[6]))
        if re.search("2 sigma band:", line):
          xs_exp_limits_2sigma.append(float(line.split()[4]))
          xs_exp_limits_2sigma_up.append(float(line.split()[6]))
else:
  for mass in signal_mass:
    print mass
    masses.append(float(mass))
    masses_exp.append(float(mass))
    log_dir = ('10_03_2015/' if plot_exp else 'logs_obs')
    log_file = open('log_'+str(int(mass))+'_'+str(sys.argv[1])+'.txt','r')
    outputlines = log_file.readlines()
    log_file.close()

    for line in outputlines:
      if re.search("observed bound =", line):
        xs_obs_limits.append(float(line.split()[6]))
      if plot_exp:
        if re.search("median:", line):
          xs_exp_limits.append(float(line.split()[1]))
        if re.search("1 sigma band:", line):
          xs_exp_limits_1sigma.append(float(line.split()[4]))
          xs_exp_limits_1sigma_up.append(float(line.split()[6]))
        if re.search("2 sigma band:", line):
          xs_exp_limits_2sigma.append(float(line.split()[4]))
          xs_exp_limits_2sigma_up.append(float(line.split()[6]))

if plot_exp:
  for i in range(0,len(masses)):
    masses_exp.append( masses[len(masses)-i-1] )
    xs_exp_limits_1sigma.append( xs_exp_limits_1sigma_up[len(masses)-i-1] )
    xs_exp_limits_2sigma.append( xs_exp_limits_2sigma_up[len(masses)-i-1] )


print "masses:"
print masses
print "xs_obs_limits:"
print xs_obs_limits
print "xs_exp_limits:"
print xs_exp_limits
print ""
print "masses_exp:"
print masses_exp
print "xs_exp_limits_1sigma:"
print xs_exp_limits_1sigma
print "xs_exp_limits_2sigma:"
print xs_exp_limits_2sigma

# ##
# ########################################################

# ########################################################
# ## Comment out this part if running the limit code

# if plot_exp:
#   masses = array('d', [300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0])
#   xs_obs_limits = array('d', [39.3249, 1.3241799999999999, 0.70614600000000005, 4.4668999999999999, 1.87497, 1.04667, 0.37109500000000001, 0.092092099999999996])
#   xs_exp_limits = array('d', [7.3874500000000003, 4.16594, 2.5205000000000002, 1.7962, 1.17222, 0.84475299999999998, 0.65692600000000001, 0.42596200000000001])
# else:
#   masses = array('d', [300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0])
#   xs_obs_limits = array('d', [39.380800000000001, 1.2964599999999999, 0.68032400000000004, 4.4672000000000001, 1.86924, 1.05078, 0.35594799999999999, 0.088954400000000003])

# masses_exp = array('d', [300.0, 400.0, 500.0, 600.0, 700.0, 800.0, 900.0, 1000.0, 1000.0, 900.0, 800.0, 700.0, 600.0, 500.0, 400.0, 300.0])
# xs_exp_limits_1sigma = array('d', [3.17753, 1.50461, 1.032, 0.81818000000000002, 0.547682, 0.43849399999999999, 0.33072000000000001, 0.24565100000000001, 0.84676700000000005, 1.3159799999999999, 1.6796899999999999, 2.65605, 3.7145700000000001, 6.5505100000000001, 13.477499999999999, 18.206700000000001])
# xs_exp_limits_2sigma = array('d', [2.00014, 0.81118199999999996, 0.58127700000000004, 0.49383100000000002, 0.28355999999999998, 0.25376500000000002, 0.19730700000000001, 0.133491, 1.5154399999999999, 1.93604, 2.3307500000000001, 4.5853200000000003, 6.2245100000000004, 9.7461699999999993, 20.569600000000001, 35.542400000000001])

# ##
# ########################################################

if plot_exp:
  graph_exp_2sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_2sigma)
  graph_exp_2sigma.SetFillColor(kYellow)
  graph_exp_2sigma.GetXaxis().SetTitle("Resonance Mass [GeV]")
  graph_exp_2sigma.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
  graph_exp_2sigma.GetYaxis().SetRangeUser(1e-04, 1e+03)
  graph_exp_2sigma.GetXaxis().SetNdivisions(1005)

  graph_exp_1sigma = TGraph(len(masses_exp),masses_exp,xs_exp_limits_1sigma)
  graph_exp_1sigma.SetFillColor(kGreen+1)

  graph_exp = TGraph(len(masses),masses,xs_exp_limits)
  #graph_exp.SetMarkerStyle(24)
  graph_exp.SetLineWidth(2)
  graph_exp.SetLineStyle(2)
  graph_exp.SetLineColor(4)

graph_obs = TGraph(len(masses),masses,xs_obs_limits)
graph_obs.SetMarkerStyle(20)
graph_obs.SetLineWidth(2)
#graph_obs.SetLineStyle(1)
graph_obs.SetLineColor(1)
graph_obs.GetXaxis().SetTitle("Resonance Mass [GeV]")
graph_obs.GetYaxis().SetTitle("#sigma#timesBR(X#rightarrowjj)#timesA [pb]")
graph_obs.GetYaxis().SetRangeUser(1e-04, 1e+03)
graph_obs.GetXaxis().SetNdivisions(1005)


c = TCanvas("c", "",800,800)
c.cd()

if plot_exp:
  graph_exp_2sigma.Draw("AF")
  graph_exp_1sigma.Draw("F")
  graph_exp.Draw("L")
  graph_obs.Draw("LP")
else:
  graph_obs.Draw("ALP")

legend = TLegend(.40,.73,.80,.86)
null = TObject()
legend.AddEntry(null, '95% CL Upper Limits (stat. only)', "");
legend.SetBorderSize(0)
legend.SetFillColor(0)
legend.SetFillStyle(0)
legend.SetTextFont(42)
legend.SetTextSize(0.03)
legend.SetHeader(sys.argv[1]+"\n" )
legend.AddEntry(graph_obs,"Observed","lp")
if plot_exp:
  legend.AddEntry(graph_exp,"Expected","lp")

legend.Draw()

#draw the lumi text on the canvas
CMS_lumi.CMS_lumi(c, iPeriod, iPos)


gPad.RedrawAxis();

c.SetLogy()
if plot_exp:
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_exp_DijetScouting_Run1_8TeV.eps')
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_exp_DijetScouting_Run1_8TeV.pdf')
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_exp_DijetScouting_Run1_8TeV.root')
else:
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_DijetScouting_Run1_8TeV.eps')
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_DijetScouting_Run1_8TeV.pdf')
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_DijetScouting_Run1_8TeV.png')
  c.SaveAs(sys.argv[1]+'_xs_limit_obs_DijetScouting_Run1_8TeV.root')

