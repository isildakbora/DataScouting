#include <iostream>
#include <cmath>
#include <cassert>
#include <sstream>

#include <TGraph.h>
#include <TFile.h>
#include <TH1D.h>
#include <TCanvas.h>
#include <TF1.h>
#include <TMath.h>
#include <TROOT.h>
#include <TVectorD.h>
#include <TMatrixD.h>
#include <TMatrixDSym.h>
#include <TMatrixDSymEigen.h>

#include "binneddata.hh"
#include "fit.hh"
#include "statistics.hh"

using namespace std;

////////////////////////////////////////////////////////////////////////////////
// magic numbers
////////////////////////////////////////////////////////////////////////////////
// number of pseudoexperiments (when greater than 0, expected limit with +/- 1 and 2 sigma bands is calculated)
// number of pseudoexperiments
const int NPES=200; // 200

// number of samples of nuisance parameters for Bayesian MC integration (when greater than 0, systematic uncertanties are included in the limit calculation)
// number of samples of nuisance parameters for Bayesian MC integration
const int NSAMPLES=5000; // 5000  (larger value is better but it also slows down the code. 5000 is a reasonable compromise between the speed and precision)

// use a B-only fit for the background systematics
const bool useBonlyFit = 1;

// constrain S to be positive in the S+B fit
const bool posS = 0;

// alpha (1-alpha=confidence interval)
const double ALPHA=0.05;

// left side tail
const double LEFTSIDETAIL=0.0;

// output file name
const string OUTPUTFILE="stats.root";

// input files vector
vector<string> INPUTFILES;

// histogram binning
const int NBINS=45;
double BOUNDARIES[NBINS+1] = {  890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856,
                               1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558,
                               3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564};

// parameters
double SIGMASS=0;
const int NPARS=12;
const int NBKGPARS=4;
const int POIINDEX=0; // which parameter is "of interest"
const char* PAR_NAMES[NPARS]    = { "xs",  "lumi",  "jes", "jer",  "bkg norm",        "p1",        "p2",         "p3", "n0", "n1", "n2", "n3" };
      double PAR_GUESSES[NPARS] = { 1E-6,  19712.,    1.0,   1.0, 3.61505e-01, 7.37667e+00, 5.89228e+00,  1.25406e-01,    0,    0,    0,    0 };
      double PAR_MIN[NPARS]     = {  0.0,     0.0,    0.0,   0.0,       -9999,       -9999,       -9999,        -9999, -100, -100, -100, -100 };
const double PAR_MAX[NPARS]     = {  1E2,     3E4,    2.0,   2.0,        9999,        9999,        9999,         9999,  100,  100,  100,  100 };
      double PAR_ERR[NPARS]     = { 1E-6, 512.512,   0.01,  0.10,       1e-02,       1e-01,       1e-01,        1e-02,    1,    1,    1,    1 };//before jes is 0.03, lumi:110
const int PAR_TYPE[NPARS]       = {    1,       2,      2,     2,           0,           0,           0,            0,    3,    3,    3,    3 }; // // 1,2 = signal (2 not used in the fit); 0,3 = background (3 not used in the fit)
//const int PAR_NUIS[NPARS]       = {    0,       1,      1,     1,          0,            0,           0,            0,    4,    4,    4,    4 }; // 0 = not varied, >=1 = nuisance parameters with different priors (1 = Lognormal, 2 = Gaussian, 3 = Gamma, >=4 = Uniform)

const int PAR_NUIS[NPARS]       = {    0,      1,     1,     1,          0,            0,           0,            0,    4,    4,    4,    4 }; // for all
//const int PAR_NUIS[NPARS]       = {    0,      1,     0,     0,          0,            0,           0,            0,    0,    0,    0,    0 }; // for lumi only
//const int PAR_NUIS[NPARS]       = {    0,      0,     1,     0,          0,            0,           0,            0,    0,    0,    0,    0 }; // for jes only
//const int PAR_NUIS[NPARS]       = {    0,      0,     0,     1,          0,            0,           0,            0,    0,    0,    0,    0 }; // for jer only
//const int PAR_NUIS[NPARS]       = {    0,      0,     0,     0,          0,            0,           0,            0,    4,    4,    4,    4 }; // for background only

// covariance matrix
double COV_MATRIX[NPARS][NPARS];
TMatrixDSym covMatrix = TMatrixDSym(NBKGPARS);
TVectorD eigenValues = TVectorD(NBKGPARS);
TMatrixD eigenVectors = TMatrixD(NBKGPARS,NBKGPARS);

// shift in the counter used to extract the covariance matrix
int shift = 1;

// branching ratio for bbbar final state (calculated wrt to the branching ratio for jet-jet final state)
double BR = 1;

// light flavor resonance shape
string LFRS = "gg";


TH1D* HISTCDF=0; // signal CDF


////////////////////////////////////////////////////////////////////////////////
// function integral
////////////////////////////////////////////////////////////////////////////////
double INTEGRAL(double *x0, double *xf, double *par)
{
  double xs=par[0];
  double lumi=par[1];
  double jes=par[2];
  double jer=par[3];
  double norm=par[4];
  double p1=par[5];
  double p2=par[6];
  double p3=par[7];
  double n[NBKGPARS] = {0.};
  n[0]=par[8];
  n[1]=par[9];
  n[2]=par[10];
  n[3]=par[11];

  if( COV_MATRIX[0+shift][0+shift]>0. && (n[0]!=0. || n[1]!=0. || n[2]!=0. || n[3]!=0.) )
  {
    double g[NBKGPARS] = {0.};
    for(int v=0; v<NBKGPARS; ++v)
    {
      for(int k=0; k<NBKGPARS; ++k) g[k]=n[v]*eigenValues(v)*eigenVectors[k][v];
      norm += g[0];
      p1   += g[1];
      p2   += g[2];
      p3   += g[3];
    }
  }

  // uses Simpson's 3/8th rule to compute the background integral over a short interval
  // also use a power series expansion to determine the intermediate intervals since the pow() call is expensive

  double dx=(xf[0]-x0[0])/3./8000.;
  double x=x0[0]/8000.0;
  double logx=log(x);

  double a=pow(1-x,p1)/pow(x,p2+p3*logx);
  double b=dx*a/x/(x-1)*(p2+p1*x-p2*x-2*p3*(x-1)*logx);
  double c=0.5*dx*dx*a*( (p1-1)*p1/(x-1)/(x-1) - 2*p1*(p2+2*p3*logx)/(x-1)/x + (p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/x/x );
  double d=0.166666667*dx*dx*dx*a*( (p1-2)*(p1-1)*p1/(x-1)/(x-1)/(x-1) - 3*(p1-1)*p1*(p2+2*p3*logx)/(x-1)/(x-1)/x - (1+p2+2*p3*logx)*(p2*(2+p2) - 6*p3 + 4*p3*logx*(1+p2*p3*logx))/x/x/x + 3*p1*(p2+p2*p2-2*p3+2*p3*logx*(1+2*p2+2*p3*logx))/(x-1)/x/x );

  double bkg=(xf[0]-x0[0])*norm*(a+0.375*(b+c+d)+0.375*(2*b+4*c+8*d)+0.125*(3*b+9*c+27*d));
  if(bkg<0.) bkg=0.0000001;

  if(xs==0.0) return bkg;

  double xprimef=jes*(jer*(xf[0]-SIGMASS)+SIGMASS);
  double xprime0=jes*(jer*(x0[0]-SIGMASS)+SIGMASS);
  int bin1=HISTCDF->GetXaxis()->FindBin(xprimef);
  int bin2=HISTCDF->GetXaxis()->FindBin(xprime0);
  if(bin1<1) bin1=1;
  if(bin1>HISTCDF->GetNbinsX()) bin1=HISTCDF->GetNbinsX();
  if(bin2<1) bin1=1;
  if(bin2>HISTCDF->GetNbinsX()) bin2=HISTCDF->GetNbinsX();
  double sig=xs*lumi*(HISTCDF->GetBinContent(bin1)-HISTCDF->GetBinContent(bin2));

  return bkg+sig;
}

////////////////////////////////////////////////////////////////////////////////
// main function
////////////////////////////////////////////////////////////////////////////////

int main(int argc, char* argv[])
{
  if(argc<=1) {
    cout << "Usage: stats signalmass [BR LFRS]" << endl;
    return 0;
  }

  SIGMASS = atof(argv[1]);
  int masspoint = int(SIGMASS);

  if(argc>2) BR = atof(argv[2]);
  if(argc>3) LFRS = argv[3];

  if(useBonlyFit) shift = 0;

  if(!posS) PAR_MIN[0] = -PAR_MAX[0];

  // initialize the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  
  INPUTFILES.push_back("/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_7/src/limit/LimitCode/Data_and_ResonanceShapes/hist_data_Run2012all_21nov.root");

  //  53X resonances files 
  string shapefile ="Histos_RSGtoQQ_0p5_truncated.root";
 //string shapefile = "Resonance_Shapes_qq_Pythia8.root";
  //string shapefile = "Resonance_Shapes_BH0p2_Pythia8.root";   
  //if(LFRS=="qq") shapefile = "Resonance_Shapes_qq_Pythia8.root";
  //string shapefile = "Resonance_Shapes_gg_Z2Star.root";   
  //if(LFRS=="qq")       shapefile = "Resonance_Shapes_qq_Z2Star.root";
 //else if (LFRS=="qg") shapefile = "Resonance_Shapes_qg_Pythia8.root";

 // 52X resonances files
 /*
 string shapefile = "Resonance_Shapes_RSGraviton_2012_D6T_ak5_GGtoGG_fat30.root";  
 if(LFRS=="qq")       shapefile = "Resonance_Shapes_RSGraviton_2012_D6T_ak5_QQtoQQ_fat30.root";
 else if (LFRS=="qg") shapefile = "Resonance_Shapes_Qstar_2012_D6T_ak5_fat30.root";
 */

string filename1 = "/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_11/src/KKousour/QCDAnalysis/RSfilesqq/" + shapefile;
string filename2 = "/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_11/src/KKousour/QCDAnalysis/RSfilesqq/" + shapefile;

//string filename1 = "/uscms_data/d3/gurpinar/work/DijetMass/LimitCalc/LimitCode/Data_and_ResonanceShapes/" + shapefile;
//string filename2 = "/uscms_data/d3/gurpinar/work/DijetMass/LimitCalc/LimitCode/Data_and_ResonanceShapes/" + shapefile;


 //string filename1 = "/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_7/src/limit/LimitCode/Data_and_ResonanceShapes/Resonance_Shapes_qq_Pythia8.root";
 //string filename2 = "/uscms_data/d3/gurpinar/work/Dijet/CMSSW_5_3_7/src/limit/LimitCode/Data_and_ResonanceShapes/Resonance_Shapes_gg_Pythia8.root";

  ostringstream histname1, histname2;
 histname1 << "h_" <<LFRS << "_" << masspoint;   // 53X
 histname2 << "h_" << LFRS << "_" << masspoint;  // 53X


 //histname1 << "h_qq_" << masspoint;
 //histname2 << "h_gg_" << masspoint;

  //  For 52X file
  /*
  histname1 << "h_qstar_"<< masspoint;   
  histname2 << "h_qstar_"<< masspoint;  
  */

  HISTCDF=getSignalCDF(filename1.c_str(), histname1.str().c_str(), filename2.c_str(), histname2.str().c_str(), BR, 1., 1.);
  
  assert(HISTCDF && SIGMASS>0);
  
  // get the data
  TH1D* data=getData(INPUTFILES, "h_DijetMass_data_fine", NBINS, BOUNDARIES);

  // create the output file
  ostringstream outputfile;
  outputfile << OUTPUTFILE.substr(0,OUTPUTFILE.find(".root")) << "_" << masspoint << "_" << BR << "_" << LFRS << ".root";
  TFile* rootfile=new TFile(outputfile.str().c_str(), "RECREATE");  rootfile->cd();

  // xs value
  double XSval;

  // setup an initial fitter to perform a signal+background fit
  Fitter initfit(data, INTEGRAL);
  for(int i=0; i<NPARS; i++) initfit.defineParameter(i, PAR_NAMES[i], PAR_GUESSES[i], PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // do an initial signal+background fit first
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) initfit.fixParameter(i);
  initfit.doFit();
  XSval = initfit.getParameter(0); // get the xs value for later use
  initfit.fixParameter(0); // a parameter needs to be fixed before its value can be changed
  initfit.setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  initfit.setPrintLevel(0);
  initfit.calcPull("pull_bkg_init")->Write();
  initfit.calcDiff("diff_bkg_init")->Write();
  initfit.write("fit_bkg_init");
  initfit.setParameter(0, XSval);

  // setup the limit values
  double observedLowerBound, observedUpperBound;
  vector<double> expectedLowerBounds;
  vector<double> expectedUpperBounds;

  cout << "********************** pe=0 (data) **********************" << endl;

  // setup the fitter with the input from the signal+background fit
  Fitter fit_data(data, INTEGRAL);
  fit_data.setPOIIndex(POIINDEX);
  //fit_data.setPrintLevel(0);
  for(int i=0; i<NPARS; i++) fit_data.defineParameter(i, PAR_NAMES[i], initfit.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

  // perform a signal+background fit or a background-only fit with a fixed non-zero signal
  for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit_data.fixParameter(i);
  if(useBonlyFit) { fit_data.doFit(); fit_data.fixParameter(0); }
  fit_data.doFit(&COV_MATRIX[0][0], NPARS);
  cout << "Data fit status: " << fit_data.getFitStatus() << endl;
  fit_data.fixParameter(0); // a parameter needs to be fixed before its value can be changed
  fit_data.setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
  fit_data.setPrintLevel(0);
  fit_data.calcPull("pull_bkg_0")->Write();
  fit_data.calcDiff("diff_bkg_0")->Write();
  fit_data.write("fit_bkg_0");

  // calculate eigenvalues and eigenvectors
  for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix(i,j)=COV_MATRIX[i+shift][j+shift]; } }
  //covMatrix.Print();
  const TMatrixDSymEigen eigen_data(covMatrix);
  eigenValues = eigen_data.GetEigenValues();
  eigenValues.Sqrt();
  //eigenValues.Print();
  eigenVectors = eigen_data.GetEigenVectors();

  fit_data.setParLimits(0, 0.0, PAR_MAX[0]); // for posterior calculation, signal has to be positive
  TGraph* post_data=fit_data.calculatePosterior(NSAMPLES);
  post_data->Write("post_0");
  cout << "Call limit reached: " << (fit_data.callLimitReached() ? "True" : "False") << endl;

  // evaluate the limit
  pair<double, double> bounds_data=evaluateInterval(post_data, ALPHA, LEFTSIDETAIL);
  observedLowerBound=bounds_data.first;
  observedUpperBound=bounds_data.second;

  // reset the covariance matrix
  for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }

  // perform the PEs
  for(int pe=1; pe<=NPES; ++pe) {

    cout << "********************** pe=" << pe << " **********************" << endl;
    ostringstream pestr;
    pestr << "_" << pe;

    // setup the fitter with the input from the signal+background fit
    fit_data.setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    TH1D* hist = fit_data.makePseudoData((string("data")+pestr.str()).c_str());
    fit_data.setParameter(0, PAR_GUESSES[0]);

    Fitter fit(hist, INTEGRAL);
    fit.setPOIIndex(POIINDEX);
    fit.setPrintLevel(0);
    for(int i=0; i<NPARS; i++) fit.defineParameter(i, PAR_NAMES[i], fit_data.getParameter(i), PAR_ERR[i], PAR_MIN[i], PAR_MAX[i], PAR_NUIS[i]);

    // perform a signal+background fit or a background-only fit with a fixed non-zero signal
    for(int i=0; i<NPARS; i++) if(PAR_TYPE[i]>=2 || PAR_MIN[i]==PAR_MAX[i]) fit.fixParameter(i);
    if(useBonlyFit) { fit.doFit(); fit.fixParameter(0); }
    fit.doFit(&COV_MATRIX[0][0], NPARS);
    if(fit.getFitStatus().find("CONVERGED")==string::npos) continue; // skip this PE if the fit failed
    fit.fixParameter(0); // a parameter needs to be fixed before its value can be changed
    fit.setParameter(0, 0.0); // set the xs value to 0 to get the B component of the S+B fit (for calculating pulls and generating pseudo-data)
    fit.calcPull((string("pull_bkg")+pestr.str()).c_str())->Write();
    fit.calcDiff((string("diff_bkg")+pestr.str()).c_str())->Write();
    fit.write((string("fit_bkg")+pestr.str()).c_str());

    // calculate eigenvalues and eigenvectors
    for(int i = 0; i<NBKGPARS; ++i) { for(int j = 0; j<NBKGPARS; ++j) { covMatrix(i,j)=COV_MATRIX[i+shift][j+shift]; } }
    const TMatrixDSymEigen eigen(covMatrix);
    eigenValues = eigen.GetEigenValues();
    bool hasNegativeElement = false;
    for(int i = 0; i<NBKGPARS; ++i) { if(eigenValues(i)<0.) hasNegativeElement = true; }
    if(hasNegativeElement) continue;
    eigenValues.Sqrt();
    eigenVectors = eigen.GetEigenVectors();

    fit.setParLimits(0, 0.0, PAR_MAX[0]); // for posterior calculation, signal has to be positive
    TGraph* post=fit.calculatePosterior(NSAMPLES);
    post->Write((string("post")+pestr.str()).c_str());
    cout << "Call limit reached in pe=" << pe << ": " << (fit.callLimitReached() ? "True" : "False") << endl;

    // evaluate the limit
    pair<double, double> bounds=evaluateInterval(post, ALPHA, LEFTSIDETAIL);
    if(bounds.first==0. && bounds.second>0.)
    {
      expectedLowerBounds.push_back(bounds.first);
      expectedUpperBounds.push_back(bounds.second);
    }

    // reset the covariance matrix
    for(int i = 0; i<NPARS; ++i) { for(int j = 0; j<NPARS; ++j) COV_MATRIX[i][j]=0.; }
  }

  ////////////////////////////////////////////////////////////////////////////////
  // print the results
  ////////////////////////////////////////////////////////////////////////////////

  cout << "**********************************************************************" << endl;
  for(unsigned int i=0; i<expectedLowerBounds.size(); i++)
    cout << "expected bound(" << (i+1) << ") = [ " << expectedLowerBounds[i] << " , " << expectedUpperBounds[i] << " ]" << endl;

  cout << "\nobserved bound = [ " << observedLowerBound << " , " << observedUpperBound << " ]" << endl;

  if(LEFTSIDETAIL>0.0 && NPES>0) {
    cout << "\n***** expected lower bounds *****" << endl;
    double median;
    pair<double, double> onesigma;
    pair<double, double> twosigma;
    getQuantiles(expectedLowerBounds, median, onesigma, twosigma);
    cout << "median: " << median << endl;
    cout << "+/-1 sigma band: [ " << onesigma.first << " , " << onesigma.second << " ] " << endl;
    cout << "+/-2 sigma band: [ " << twosigma.first << " , " << twosigma.second << " ] " << endl;
  }

  if(LEFTSIDETAIL<1.0 && NPES>0) {
    cout << "\n***** expected upper bounds *****" << endl;
    double median;
    pair<double, double> onesigma;
    pair<double, double> twosigma;
    getQuantiles(expectedUpperBounds, median, onesigma, twosigma);
    cout << "median: " << median << endl;
    cout << "+/-1 sigma band: [ " << onesigma.first << " , " << onesigma.second << " ] " << endl;
    cout << "+/-2 sigma band: [ " << twosigma.first << " , " << twosigma.second << " ] " << endl;
  }

  // write out all histograms... 
  // rootfile->Write();

  // close the output file
  rootfile->Close();


  return 0;
}
