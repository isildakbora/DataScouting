import ROOT, sys, os
import subprocess
from ROOT import *
from rootutils import *
import math, sys, numpy as np

os.chdir('Events/'+ str(sys.argv[1]))
if not os.path.exists('events.lhe'):
	os.system('gunzip events.lhe.gz')
os.system('cp ../LHE2root.py .')
os.system('chmod a+x LHE2root.py')
proc = subprocess.Popen('/usr/bin/python2.7 LHE2root.py events.lhe', shell=True)
proc.wait()

myfile  = TFile( 'lhe.root' )
entry = gDirectory.Get( 'Physics' )

acceptance_count      = 0

entries = entry.GetEntriesFast()
print entries

for jentry in range(int(entries/1)):


#	print "evt_no:", jentry
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

print "acceptance=",float(acceptance_count)/float(entries)

os.chdir('../../')

keepGUIalive()


