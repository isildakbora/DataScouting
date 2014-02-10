#define DSComp_cxx
#include "DSComp.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <utility>

void DSComp::Loop()
{
  TFile *f = new TFile("Delta_pT_histograms_legends.root", "RECREATE");

  TH1F* h_recoJetPt      = new TH1F("RecoJetpT","Reco Jet pT",498,20,5000);

  TH1F* h_recoJetE       = new TH1F("RecoJetE","Reco Jet E",498,20,5000);
  TH1F* h_dsJetE         = new TH1F("HLTJetE","HLT Jet E",498,20,5000);

  TH1F* h_recoJetRawE    = new TH1F("RecoJetRawE","Reco Jet Raw E",498,20,5000);
  TH1F* h_dsJetRawE      = new TH1F("HLTJetRawE","HLT Jet Raw E",498,20,5000);

  TH1F* h_recoHLTpTdiff  = new TH1F("recoHLTpTdiff","recoHLTpTdiff",400,-1.,1.);
  TH1F* h_recoHLTEtadiff = new TH1F("recoHLTEtadiff","recoHLTEtadiff",4800,-2,2);
  TH1F* h_recoHLTPhidiff = new TH1F("recoHLTPhidiff","recoHLTPhidiff",4800,-TMath::Pi(), TMath::Pi());

  char *HLT[2]  = {"HLT Pass","HLT Fail"};
  char *RECO[2] = {"RECO Pass","RECO Fail"};

  TH2F* h_HLT_RECO_Table = new TH2F("HLT_RECO_Table", "HLT_RECO_Table",2,0,2,2,0,2);
  for (int i=1;i<=2;i++) h_HLT_RECO_Table->GetXaxis()->SetBinLabel(i,HLT[i-1]);
  for (int i=1;i<=2;i++) h_HLT_RECO_Table->GetYaxis()->SetBinLabel(i,RECO[i-1]);

   if (fChain == 0) return;

   Float_t dsjetpt, recojetpt, dsjeteta, recojeteta;
   Long64_t nentries = fChain->GetEntriesFast();
   std::cout << nentries << std::endl;
   Long64_t nbytes = 0, nb = 0;
    
    

   // Set kinematic binnings

    float pTbins[]  = {30., 103., 206., 309., 413., 515., 618., 721., 1237.};
    const Int_t   n_pTbins  = sizeof(pTbins)/sizeof(float)-1;

    float etaBins[] = {0., 0.5, 1.0, 1.5, 2.0, 2.5};
    const Int_t   n_etaBins = sizeof(etaBins)/sizeof(float)-1;
    TString histoname;
    TH1F *hDeltapT[8][5];
    TH1F *hDeltapMjj[8][5];
    TH1F *hdspileupCorr[8][5];
    TH1F *hdsJECL2L3Res[8][5];
    TH1F *hrecoJEC[8][5];
    TF1 *cbfit[8][5];
    TF1 *aux_xBal[8][5];
    TF1 *aux_gaus[8][5];

  // Set the names and bins of histograms
    for (int i = 0; i < n_pTbins; ++i)
    {
        for (int j=0; j<n_etaBins; ++j)
        {
            histoname = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            hDeltapT[i][j]= new TH1F(histoname, histoname, 1200, -1.2, 1.2);
            hDeltapT[i][j]->Sumw2();

            hDeltapMjj[i][j]= new TH1F(histoname+"Mjj", histoname+"Mjj", 1200, -1.2, 1.2);
            hDeltapMjj[i][j]->Sumw2();

            histoname = "dspileopCorr"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            hdspileupCorr[i][j]= new TH1F(histoname, histoname, 1000, 0, 10);

            histoname = "dsJECL2L3Res"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            hdsJECL2L3Res[i][j]= new TH1F(histoname, histoname, 1000, 0, 10);

            histoname = "recoJEC"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            hrecoJEC[i][j]= new TH1F(histoname, histoname, 1000, 0, 10);
        }
        
    }

   // Set threshold values at which events are excluded
    float minPtThreshold = 30.; // GeV
    float maxAbsEtaThreshold = 2.5;
    float maxEtaSepThreshold = 2.0;
    
   // Tree Loop
   for (Long64_t jentry=0; jentry<nentries/100; jentry++)
   {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;

      //----------- progress report -------------
      std::cout << "\r" << jentry << "\t" << 100.0*jentry/nentries << "% completed: ";
      //std::cout.flush();

      // Filters //
      //if two jets exist
      if (!((nDSJets > 1) && (nRECOJets > 1))) continue;    

        //Dijet HLT Selection
        int DeltaEtaHLT           = (fabs(dsJetEta[0]-dsJetEta[1]) < 1.3) ? 1 : 0;
        int MaxAbsEtaThresholdHLT = ((fabs(dsJetEta[0]) < maxAbsEtaThreshold) && (fabs(dsJetEta[1]) < maxAbsEtaThreshold));
        int MinPtThresholdHLT     = ((dsJetPt[0] > minPtThreshold) && (dsJetPt[1] > minPtThreshold));
        int allHLTDijetSelection  = (DeltaEtaHLT && MinPtThresholdHLT && MaxAbsEtaThresholdHLT);     

        //Dijet RECO Selection
        int matchindex0 = dsJetMatchIndex[0];
        int matchindex1 = dsJetMatchIndex[1];
        if(matchindex0 >=0 && matchindex1 >=0)
        {
          int DeltaEtaRECO           = (fabs(recoJetEta[matchindex0]-recoJetEta[matchindex1]) < 1.3) ? 1 : 0;
          int MinPtThresholdRECO     = ((recoJetPt[matchindex0] > minPtThreshold) && (recoJetPt[matchindex1] > minPtThreshold));
          int MaxAbsEtaThresholdRECO = ((fabs(recoJetEta[matchindex0]) < maxAbsEtaThreshold) && (fabs(recoJetEta[matchindex1]) < maxAbsEtaThreshold));
          int allRECODijetSelection  = (DeltaEtaRECO && MinPtThresholdRECO && MaxAbsEtaThresholdRECO);  
        }
        else int allRECODijetSelection = 0;
        //RECO Event Filters
        int DeltaPhiRECO  = (fabs(recoJetPhi[0]-recoJetPhi[1]) > TMath::Pi()/3) ? 1 : 0;
        int RecoFlagsGood = (DeltaPhiRECO && HBHENoiseFilterResultFlag && hcalLaserEventFilterFlag && eeBadScFilterFlag);

        //HLT Event Filters
        int DeltaPhiHLT         = (fabs(dsJetPhi[0]-dsJetPhi[1]) > TMath::Pi()/3) ? 1 : 0;
        int MET_vs_METCleanFlag = (dsMetPt != dsMetCleanPt) ? 0 : 1;
        int JetIDHLT            = (dsJetFracHad[0] < 0.95 && dsJetFracHad[1] < 0.95 && dsJetFracEm[0] < 0.95 && dsJetFracEm[1] < 0.95) ? 1 : 0;
        int HLTFlagsGood        = (JetIDHLT && MET_vs_METCleanFlag && DeltaPhiHLT);

        int keepEvent = (allHLTDijetSelection && allRECODijetSelection);

        if (!keepEvent)
        {
          continue; 
        }

        // Fill the HLT vs RECO Filter Table
        if(HLTFlagsGood && RecoFlagsGood)        h_HLT_RECO_Table->Fill(0,0);
        else if(!HLTFlagsGood && !RecoFlagsGood) h_HLT_RECO_Table->Fill(1,1);
        else if(!HLTFlagsGood && RecoFlagsGood)  h_HLT_RECO_Table->Fill(1,0);
        else                                     h_HLT_RECO_Table->Fill(0,1);

        // Filters //

      // Dijet mass difference
      int , pTbin, etabin;
      matchindex0 = dsJetMatchIndex[0];
      matchindex1 = dsJetMatchIndex[1];
      TLorentzVector dsJet1, dsJet2, recoJet1, recoJet2;
      Double_t dsMjj, recoMjj;
      if(matchindex0 >=0 && matchindex1 >=0)
      {
        dsJet1.SetPtEtaPhiE(dsJetPt[0], dsJetEta[0], dsJetPhi[0], dsJetE[0]);
        dsJet2.SetPtEtaPhiE(dsJetPt[1], dsJetEta[1], dsJetPhi[1], dsJetE[1]);
        recoJet1.SetPtEtaPhiE(recoJetPt[matchindex0], recoJetEta[matchindex0], recoJetPhi[matchindex0], recoJetE[matchindex0]);
        recoJet2.SetPtEtaPhiE(recoJetPt[matchindex1], recoJetEta[matchindex1], recoJetPhi[matchindex1], recoJetE[matchindex1]);
        
        dsMjj   = (dsJet1+dsJet2).M();
        recoMjj = (recoJet1+recoJet2).M();

        pTbin     = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsPt,dsEta).first;
        etabin    = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsPt,dsEta).second;
        hDeltapMjj[pTbin][etabin]->Fill((dsMjj-recoMjj)/recoMjj);
      }

       // Jet Loop//
       for(Int_t i=0; i< nDSJets; i++)
       {
           Double_t frac_diff, dsPt, recoPt, dsEta, recoEta, dsPhi, recoPhi;
           int matchindex;
           
           if( nDSJets<35)
           {
            matchindex = dsJetMatchIndex[i];
            if( matchindex >= 0)
            {
              dsPt      = dsJetPt[i];
              recoPt    = recoJetPt[matchindex];
              dsEta     = dsJetEta[i];
              recoEta   = recoJetEta[matchindex];
              dsPhi     = dsJetPhi[i];
              recoPhi   = recoJetPhi[matchindex];

              frac_diff = (dsPt-recoPt)/recoPt;

              h_dsJetRawE   -> Fill(dsJetRawE[i]);
              h_recoJetRawE -> Fill(recoJetRawE[i]);

              h_dsJetE      -> Fill(dsJetE[i]);
              h_recoJetE    -> Fill(recoJetE[i]);

              h_recoHLTEtadiff -> Fill((dsEta - recoEta)/recoEta);
              h_recoHLTPhidiff -> Fill((dsPhi - recoPhi)/recoPhi);
              h_recoHLTpTdiff  -> Fill(frac_diff);


              pTbin     = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsPt,dsEta).first;
              etabin    = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsPt,dsEta).second;

              hDeltapT[pTbin][etabin]->Fill(frac_diff);

              hdspileupCorr[pTbin][etabin] -> Fill(dspileupCorr[i]);
              hdsJECL2L3Res[pTbin][etabin] -> Fill(dsJECL2L3Res[i]);
              hrecoJEC[pTbin][etabin]      -> Fill(recoJEC[i]);
            }
          }
        }
        // Jet Loop//
   }
   // Tree Loop

    TString name;

    Double_t maxVal, mean, RMS;
    for (int i = 0; i < n_pTbins; ++i)
    {
        for (int j=0; j<n_etaBins; ++j)
        {
            name = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            
            hDeltapT[i][j]  ->Scale(1./hDeltapT[i][j]->GetEntries());
            hDeltapMjj[i][j]->Scale(1./hDeltapMjj[i][j]->GetEntries());
            f->cd();
            
            hDeltapT[i][j]      ->Write();
            hDeltapMjj[i][j]    ->Write();
            hdspileupCorr[i][j] ->Write();
            hdsJECL2L3Res[i][j] ->Write();
            hrecoJEC[i][j]      ->Write();
        }  
           
    }
    h_HLT_RECO_Table ->Write();

    TF1 *func = new TF1("TripleGaussian_fit",Total,-0.8,0.8,9);
    func->SetParameter(0,2e+5);
    func->SetParameter(1,-0.02);
    func->SetParameter(2,0.1);
    
    func->SetParameter(3,1000);
    func->SetParameter(4,-0.02);
    func->SetParameter(5,0.5);
    
    func->SetParameter(6,1000);
    func->SetParameter(7,-0.02);
    func->SetParameter(8,0.5);
   //h_recoHLTpTdiff -> GetXaxis()->SetTitle("#Delta p_{T}/p_{T}");
   //h_recoHLTpTdiff -> GetXaxis()->SetRangeUser(-0.4,0.4); 
   

   //TString fit_func = "CB_fit";
   //h_recoHLTpTdiff->Fit(fit_func, "RMQ+");*/
  f -> cd();
  h_dsJetRawE   -> Write();
  h_recoJetRawE -> Write();
  h_dsJetE      -> Write();
  h_recoJetE    -> Write();
  f -> Write();
  
}


Double_t CrystalBallFunctionL(Double_t *xx, Double_t *par) {
    
    // variable x
    Double_t x = xx[0];
    
    // parameters alpha, n, x0, sigma
    Double_t A = par[0];
    Double_t alpha = par[1];
    Double_t n = par[2];
    Double_t x0 = par[3];
    Double_t sigma = par[4];
    
    Double_t t = (x-x0)/sigma;
    if (alpha < 0) t = -t;

    Double_t absAlpha = fabs((Double_t)alpha);

    if (t >= -absAlpha) {
        return A*exp(-0.5*t*t);
    }
    else {
        Double_t a = A*TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
        Double_t b = n/absAlpha - absAlpha; 

        return a/TMath::Power(b - t, n);
    }
}

Double_t CrystalBallFunctionR(Double_t *xx, Double_t *par) {
    
    // variable x
    Double_t x = xx[0];
    
    // parameters alpha, n, x0, sigma
    Double_t A = par[0];
    Double_t alpha = par[1];
    Double_t n = par[2];
    Double_t x0 = par[3];
    Double_t sigma = par[4];
    
    Double_t t = -(x-x0)/sigma;
    if (alpha < 0) t = -t;

    Double_t absAlpha = fabs((Double_t)alpha);

    if (t >= -absAlpha) {
        return A*exp(-0.5*t*t);
    }
    else {
        Double_t a = A*TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
        Double_t b = n/absAlpha - absAlpha; 

        return a/TMath::Power(b - t, n);
    }
}

Double_t DoubleCrystalBallFunction(Double_t *xx, Double_t *par) {
    
   // variable x
   Double_t x = xx[0];
    
   // parameters alpha, n, x0, sigma
   Double_t A      = par[0];
   Double_t alpha1 = par[1];
   Double_t alpha2 = par[2];
   Double_t n1     = par[3];
   Double_t n2     = par[4];
   Double_t mean   = par[5];
   Double_t width  = par[6];

   double A1 = pow(n1/fabs(alpha1),n1)*exp(-alpha1*alpha1/2);
   double A2 = pow(n2/fabs(alpha2),n2)*exp(-alpha2*alpha2/2);
   double B1 = n1/fabs(alpha1)-fabs(alpha1);
   double B2 = n2/fabs(alpha2)-fabs(alpha2);

   if((x-mean)/width>-alpha1 && (x-mean)/width<alpha2)
   {
     return A*exp(-(x-mean)*(x-mean)/(2*width*width));
   }
   else if((x-mean)/width<-alpha1)
   {
     return A*A1*pow(B1-(x-mean)/width,-n1);
   }
   else if((x-mean)/width>alpha2)
   {
     return A*A2*pow(B2+(x-mean)/width,-n2);
   }
   else
   {
     cout << "ERROR evaluating range..." << endl;
     return 99;
   }
}

Double_t CrystalBallFunctionL_plus_CrystalBallFunctionR(Double_t *x, Double_t *par)
{
  par[0]=par[5];
  par[3]=par[8];
  par[4]=par[9];

  Double_t y = 0.5*(CrystalBallFunctionL(x,par)+CrystalBallFunctionR(x,&par[5]));
  return y;
}

Double_t G1(Double_t *x, Double_t *par)
{
   Double_t arg = 0;
   if (par[2]) arg = (x[0] - par[1])/par[2];

   Double_t y = par[0]*TMath::Exp(-0.5*arg*arg);
   return y;
}


Double_t G2(Double_t *x, Double_t *par)
{
   Double_t arg = 0;
   if (par[2]) arg = (x[0] - par[1])/par[2];

   Double_t y = par[0]*TMath::Exp(-0.5*arg*arg);
   return y;
}

Double_t G3(Double_t *x, Double_t *par)
{
   Double_t arg = 0;
   if (par[2]) arg = (x[0] - par[1])/par[2];

   Double_t y = par[0]*TMath::Exp(-0.5*arg*arg);
   return y;
}

Double_t G4(Double_t *x, Double_t *par)
{
   Double_t arg = 0;
   if (par[2]) arg = (x[0] - par[1])/par[2];

   Double_t y = par[0]*TMath::Exp(-0.5*arg*arg);
   return y;
}


Double_t Total(Double_t *x, Double_t *par)
{
   Double_t y = G1(x,par) + G2(x,&par[3])+G3(x,&par[6]);
   return y;
}

Double_t CB_plus_Gaussian(Double_t *x, Double_t *par)
{
   Double_t y = CrystalBallFunction(x,par) + G1(x,&par[5]);
   return y;
}

std::pair <int,int> Get_ij(float array1[], int length1, float array2[], int length2, double num1, double num2)
{
    int i = 0;
    int j = 0;
    
    for(int k=0; k < length1; ++k)
    {
        if(num1 > array1[k])
        {
            i = k;
        }
        else if(num1 > array1[k] && num1 < array1[k+1])
            break;
        
    }
    
    for(int k=0; k < length2; ++k)
    {
        if(num2 > array2[k])
        {
            j = k;
        }
        else if(num2 > array2[k] && num1 < array2[k+1])
            break;
    }
    return std::make_pair(i,j);
}

Double_t CrystalBallFunction(Double_t *xx, Double_t *par) {
    
    // variable x
    Double_t x = xx[0];
    
    // parameters alpha, n, x0, sigma
    Double_t A = par[0];
    Double_t alpha = par[1];
    Double_t n = par[2];
    Double_t x0 = par[3];
    Double_t sigma = par[4];
    
    Double_t t = (x-x0)/sigma;
    if (alpha < 0) t = -t;

    Double_t absAlpha = fabs((Double_t)alpha);

    if (t >= -absAlpha) {
        return A*exp(-0.5*t*t);
    }
    else {
        Double_t a = A*TMath::Power(n/absAlpha,n)*exp(-0.5*absAlpha*absAlpha);
        Double_t b = n/absAlpha - absAlpha; 

        return a/TMath::Power(b - t, n);
    }
}

Double_t Gaussian(Double_t *x, Double_t *par)
{
   Double_t arg = 0;
   if (par[2]) arg = (x[0] - par[1])/par[2];

   Double_t y = par[0]*TMath::Exp(-0.5*arg*arg);
   return y;
}


Double_t CrystalBallFunction_plus_Gaussian(Double_t *x, Double_t *par)
{
   Double_t y = CrystalBallFunction(x,par) + Gaussian(x,&par[5]);
   return y;
}

