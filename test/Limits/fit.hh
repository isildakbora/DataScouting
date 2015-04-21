#ifndef __FIT_HH__
#define __FIT_HH__

#include <map>
#include <TMinuit.h>
#include <TRandom3.h>
#include <BAT/BCModel.h>

class TGraph;
class TF1;
class TH1D;
class RandomPrior;

typedef double (*integral_ptr_t)(double*, double*, double*);

class Fitter : public BCModel
{
public:
  // constructor/destructor
  Fitter();
  Fitter(TH1D* data, integral_ptr_t functionIntegral, int maxpar=25);
  virtual ~Fitter();

  // overloaded methods from BCModel
  double LogAPrioriProbability(const std::vector<double> &parameters);
  double LogLikelihood(const std::vector<double> &parameters);

  // setters
  void setData(TH1D* hist) { data_=hist; }
  void setFunctionIntegral(integral_ptr_t fcnintegral) { functionIntegral_=fcnintegral; }
  void setRandomSeed(unsigned int seed) { rand_->SetSeed(seed); }

  // getters
  bool callLimitReached() { return callLimitReached_; }
  const std::string getFitStatus() { return std::string(minuit_.fCstatu.Data()); }
  int getNCalls() { return minuit_.fNfcn; }

  // parameter manipulation
  int defineParameter(int parno, const char* name, double value, double error, double lo, double hi, int isNuisance);
  int setParameter(int parno, double value);
  int setParLimits(int parno, double loLimit, double hiLimit);
  int fixParameter(int parno) { return minuit_.FixParameter(parno); }
  int floatParameter(int parno) { return minuit_.Release(parno); }
  double getParameter(int parno) const;
  double getParError(int parno) const;
  void getParLimits(int parno, double &loLimit, double &hiLimit) const;
  int getParameter(int parno, double &currentValue, double &currentError) const { return minuit_.GetParameter(parno, currentValue, currentError); }
  int getNumPars(void) { return minuit_.GetNumPars(); }
  double* getParameters(void);
  void setPOIIndex(int parno) { poiIndex_=parno; return; }

  // fitting, pulls, and all that
  void doFit(void);
  void doFit(double* emat, int ndim);
  TH1D* calcPull(const char* name);
  TH1D* calcDiff(const char* name);

  // other minor tweaks to Minuit
  void setStrategy(int s) { strategy_=s; }
  double getStrategy(void) const { return strategy_; }
  void setPrintLevel(int p) { printlevel_=p; }
  double getPrintLevel(void) const { return printlevel_; }

  // evaulate the NLL with the current set of parameters
  double evalNLL(void);

  // write the TMinuit object
  void write(const char* name) const { minuit_.Write(name); return; }

  // make pseudodata
  TH1D* makePseudoData(const char* name, double* parameters=0);

  // calculate the posterior distribution
  TGraph* calculatePosterior(int nSamples, bool useMCMC=false);

  // return the error on a histogram bin with N events
  static double histError(double N);

  // calculate the CLs
  double calculateUpperBoundWithCLs(int nSamples, double alpha);

private:

  static void nll(int &, double*, double&, double*, int);
  static Fitter* theFitter_;

  TRandom3* rand_;
  TMinuit minuit_;
  integral_ptr_t functionIntegral_;
  TH1D* data_;
  int printlevel_;
  int strategy_;
  std::map<int, int> parameterIsNuisance_;
  std::map<int, RandomPrior*> priors_;  // nuisance parameter priors
  double *parameters_;
  int poiIndex_;

  int nSamples_;
  int nCalls_;
  bool callLimitReached_;
  double poiBestFit_;
  double poiUserError_;
  bool parRangeSet_; // only used for nuisance parameters with uniform priors
  bool useMCMC_;

  void evaluateForPosterior(double lo, double mid, double hi, double nllNormalization, std::map<double, double>& fcnEval_);
  double computeLikelihoodWithSystematics(double poiVal, double nllNormalization);

  // calculate the CLs
  std::pair<int, int> calculateCLs_(double poiVal, std::vector<double>& CLb, std::vector<double>& CLsb);

};

#endif
