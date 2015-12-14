import numpy as np
import os, subprocess
import ROOT, sys, os
from ROOT import *
from rootutils import *
import math

def tree_analysis(event_folder):
	os.chdir("Events/mZ_" + event_folder)
	if not os.path.exists("events.lhe"):
		os.system("gunzip events.lhe.gz")
	os.system("cp ../LHE2root.py .")
	os.system("chmod a+x LHE2root.py")
	proc = subprocess.Popen("/usr/bin/python2.7 LHE2root.py events.lhe", shell=True)
	proc.wait()
	myfile  = TFile( "lhe.root" )
	entry = gDirectory.Get( "Physics" )
	acceptance_count      = 0
	entries = entry.GetEntriesFast()
	#print entries

	for jentry in range(int(entries/1)):
		entry.GetEntry( jentry )
		n_particles 	= entry.n_particles
		P_X		= entry.P_X
		P_Y		= entry.P_Y
		P_Z		= entry.P_Z
		E 		= entry.E
		M 		= entry.M
		Mother          = entry.Mother
		PID 	        = entry.PID
		PID_names       = [pdgid_to_name(id) for id in PID]

		jets = []

		for i_jet in xrange(n_particles):
			jets.append(TLorentzVector(P_X[i_jet], P_Y[i_jet], P_Z[i_jet], E[i_jet]))

		cut1 = jets[0].Pt() > 30 and jets[1].Pt() > 30
		cut2 = abs(jets[0].Eta() < 2.5) and abs(jets[1].Eta() < 2.5)
		cut3 = abs(jets[0].Eta() - jets[1].Eta()) < 1.3
		cut4 = abs(jets[0].Phi() - jets[1].Phi()) < (math.pi/3.)
		cut4 = (jets[0] + jets[1]).M() > 354.

		if cut1 and cut2 and cut3 and cut4:
			acceptance_count += 1
	acceptance = float(acceptance_count)/float(entries)
	xsec       = get_xsec("events.lhe")
	os.chdir('../../')
	return str(acceptance*xsec)

def change_param_gB_mZ(new_gB, new_mZ):
	infile  = open("Cards/param_card_template.dat")
	outfile = open("Cards/param_card.dat", "w")
	lines = infile.readlines()

	for line in lines:
		if "# gz" in line:
			outfile.write(line.replace(str(line.split()[1]), "{:.6e}".format(new_gB)))
		elif "# MZph" in line:
			outfile.write(line.replace(str(line.split()[1]), "{:.6e}".format(new_mZ)))
		else:
			outfile.write(line)

def get_xsec(lhe_file_name):
	infile  = open(lhe_file_name)
	lines = infile.readlines()
	xsec = 0
	for line in lines:
		if "#  Integrated weight (pb)" in line:
			xsec = float(line.split()[5])

	return xsec


line = []
for mZ in range(500, 4100, 100):
	for gB in np.linspace(0.2, 1.6, 8):
		change_param_gB_mZ(gB, mZ)
		cmd = "./bin/generate_events 2 4 mZ_" + str(mZ) + "_" + str(gB) + " run"
		proc = subprocess.Popen(cmd, shell=True)
		proc.wait()
		xsecxacc = tree_analysis(str(mZ) + "_" + str(gB))
		line.append(str(mZ)+" "+ str(gB) + " " + str(xsecxacc) + '\n')
		print line[-1]
		outfile = open("xsecxacc.txt", "w")

for i in line:
	outfile.write(i)
outfile.close()


