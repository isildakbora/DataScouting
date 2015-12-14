#!usr/bin/python
import ROOT
from ROOT import TCanvas, TGraph, TLegend, gROOT, gPad, TFile, TGraphErrors, gStyle, TF1, TSpline3, TSpline5, TSpline
import numpy as np
from array import array
import rootutils
gROOT.ProcessLine(".X ~/setTDRStyle.C")
gStyle.SetOptFit(1111)

outputfile = TFile("gB_interpolation_inverse.root", "RECREATE")
data = np.genfromtxt('XSECxACC.dat', dtype=float, delimiter=',')
data_reshaped = np.reshape(data, (36, 8, 3))



err_x     = array('d',[0]*8)
graphs    = []
canvases  = []
splines   = []

for data_element in data_reshaped:
	
	x = array('d', data_element.T[1])
	y = array('d', data_element.T[2])
	
	graphs.append(TGraph(len(x), y, x))
	name = 'MZ_' + str(int(data_element.T[0][0]))
	canvases.append(TCanvas(name, name,600,600))
	canvases[-1].cd()
	graphs[-1].Draw('APE')
	graphs[-1].SetMarkerSize(1.0)
	graphs[-1].SetMarkerStyle(20)
	graphs[-1].SetTitle(name)
	splines.append(TSpline3('Spline_MZ_' + name.replace('MZ_', ''), graphs[-1]))
	splines[-1].Draw('SAME')
	splines[-1].SetLineColor(ROOT.kRed)
	outputfile.cd()
	canvases[-1].Write(name + '.C')
	splines[-1].Write('Spline_MZ_' + name.replace('MZ_', ''))

outputfile.Close()


#----- keep the GUI alive ------------
if __name__ == '__main__':
  rep = ''
  while not rep in ['q','Q']:
    rep = raw_input('enter "q" to quit: ')
    if 1 < len(rep):
      rep = rep[0]