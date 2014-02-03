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
            hDeltapT[i][j]= new TH1F(histoname, histoname, 300, -1.2, 1.2);
            hDeltapT[i][j]->Sumw2();

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
   for (Long64_t jentry=0; jentry<nentries/1; jentry++)
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

        int meetsMinPtThreshold = ((dsJetPt[0] > minPtThreshold) 
                && (dsJetPt[1] > minPtThreshold) 
                && (recoJetPt[0] > minPtThreshold) 
                && (recoJetPt[1] > minPtThreshold));

        int meetsMaxAbsEtaThreshold = ((fabs(dsJetEta[0]) < maxAbsEtaThreshold) 
                && (fabs(dsJetEta[1]) < maxAbsEtaThreshold)
                && (fabs(recoJetEta[0]) < maxAbsEtaThreshold)
                && (fabs(recoJetEta[1]) < maxAbsEtaThreshold));

        int RecoFlagsGood = (HBHENoiseFilterResultFlag 
                && hcalLaserEventFilterFlag && eeBadScFilterFlag);

        int JetIDFlag           = (dsJetFracHad[i] < 0.95 && dsJetFracEm[i] < 0.95) ? 1 : 0;
        int DeltaPhiFlag        = (fabs(dsJetPhi[0]-dsJetPhi[1]) > TMath::Pi()/3) ? 1 : 0;
        int MET_vs_METCleanFlag = (dsMetPt != dsMetCleanPt) ? 0 : 1;
        
        int HLTFlagsGood        = (JetIDFlag && DeltaPhiFlag && MET_vs_METCleanFlag);

        if(HLTFlagsGood && RecoFlagsGood)        HLT_RECO_Table->Fill(0,0);
        else if(!HLTFlagsGood && !RecoFlagsGood) HLT_RECO_Table->Fill(1,1);
        else if(!HLTFlagsGood && RecoFlagsGood)  HLT_RECO_Table->Fill(1,0);
        else (HLTFlagsGood && !RecoFlagsGood)    HLT_RECO_Table->Fill(0,1);

        int keepEvent = (meetsMinPtThreshold && meetsMaxAbsEtaThreshold && RecoFlagsGood && JetIDFlag && DeltaPhiFlag && MET_vs_METCleanFlag);

        //cout << "hcalLaserEventFilterFlag:" << hcalLaserEventFilterFlag  << endl;
        if (!keepEvent)
        {
          continue; 
        }
        // Filters //

       // Jet Loop//
       for(Int_t i=0; i< nDSJets; i++)
       {
           float frac_diff, dsPt, recoPt, dsEta;
           int matchindex, pTbin, etabin;
           
           if( nDSJets<35)
           {
            matchindex = dsJetMatchIndex[i];
            if( matchindex >= 0)
            {
              
              h_dsJetRawE   -> Fill(dsJetRawE[i]);
              h_recoJetRawE -> Fill(recoJetRawE[i]);

              h_dsJetE      -> Fill(dsJetE[i]);
              h_recoJetE    -> Fill(recoJetE[i]);

              dsPt      = dsJetPt[i];
              recoPt    = recoJetPt[matchindex];
              dsEta     = dsJetEta[i];
              frac_diff = (dsPt-recoPt)/recoPt;
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


    //Set the canvases, perform the fits and draw the histograms
    TCanvas *can = new TCanvas("DSComparison","DSComparison",2240,1400);
    TCanvas *i_can[8][5];
    can->Divide(8,5);
    TString name;

    Double_t maxVal, mean, RMS;
    for (int i = 0; i < n_pTbins; ++i)
    {
        for (int j=0; j<n_etaBins; ++j)
        {
            name = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            
            i_can[i][j] =  new TCanvas(name);
            hDeltapT[i][j]->Scale(1./hDeltapT[i][j]->GetEntries());

            

            maxVal = hDeltapT[i][j]->GetBinContent(hDeltapT[i][j]->GetMaximumBin());
            mean   = hDeltapT[i][j]->GetMean();
            RMS    = hDeltapT[i][j]->GetRMS();

            cbfit[i][j] = new TF1(name, CrystalBallFunctionL, mean-1.5*RMS, mean+1.5*RMS, 5);
            //cbfit[i][j]->SetParameters(maxVal/2, -1.6, 4, mean, RMS, maxVal/2, -1.6, 4, mean, RMS);
            cbfit[i][j]->SetParNames("A_{1}","#alpha","n","#mu","#sigma");
            //cbfit[i][j]->SetParNames("A_{1}","#alpha_{1}","n_{1}","#mu_{1}","#sigma_{1}","A_{2}","#alpha_{2}","n_{2}","#mu_{2}","#sigma_{2}");
            //cbfit[i][j]->SetParNames("N","A_{L}","A_{R}","#alpha_{L}","#alpha_{R}","n_{L}","n_{R}","#mu","#sigma");
            cbfit[i][j]->SetParameters(maxVal, -4e+5, -1.e+5, mean, RMS);
            
            gStyle->SetOptStat(1101);
            can->cd(i*5+j+1);
            hDeltapT[i][j]->Fit(name, "REMQ+");
            hDeltapT[i][j]->Fit(name, "REMQ");
            hDeltapT[i][j]->GetXaxis()->SetRangeUser(mean-2*RMS,mean+2*RMS);

            /*aux_xBal[i][j] = new TF1("CrystalBallFunctionL", CrystalBallFunctionL, mean-2*RMS, mean+2*RMS, 5);
            aux_gaus[i][j] = new TF1("CrystalBallFunctionR", CrystalBallFunctionR, mean-2*RMS, mean+2*RMS, 5);

            aux_xBal[i][j]->SetParNames("A_{1}","#alpha_{1}","n_{1}","#mu_{1}","#sigma_{1}");
            aux_gaus[i][j]->SetParNames("A_{2}","#alpha_{2}","n_{2}","#mu_{2}","#sigma_{2}");

            Double_t par[10];

            cbfit[i][j]->GetParameters(par);
            aux_xBal[i][j]->SetParameters(par);
            aux_gaus[i][j]->SetParameters(&par[5]);
            

            aux_xBal[i][j]->SetLineColor(kBlue);
            aux_gaus[i][j]->SetLineColor(kRed);
            cbfit[i][j]   ->SetLineColor(kBlack);*/

            i_can[i][j]   ->cd();
            hDeltapT[i][j]->Draw();
            cbfit[i][j]   ->Draw("same");
            //aux_gaus[i][j]->Draw("same");
            //aux_xBal[i][j]->Draw("same");
            i_can[i][j]   ->Write();

            f->cd();
            
            hDeltapT[i][j]      ->Write();
            hdspileupCorr[i][j] ->Write();
            hdsJECL2L3Res[i][j] ->Write();
            hrecoJEC[i][j]      ->Write();
        }  
           
    }
    h_HLT_RECO_Table ->Write();
    can->Write();

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
    Double_t N = par[0];
    Double_t AR = par[1];
    Double_t AL = par[2];

    Double_t alphaR = par[3];
    Double_t alphaL = par[4];

    Double_t nR = par[5];
    Double_t nL = par[6];

    Double_t x0 = par[7];
    Double_t sigma = par[8];
    
    Double_t t = (x-x0)/sigma;

    Double_t absAlphaR = fabs((Double_t)alphaR);
    Double_t absAlphaL = fabs((Double_t)alphaL);

    if (t >= -absAlphaR) 
    {
      Double_t aR = AR*TMath::Power(nR/absAlphaR,nR)*exp(-0.5*absAlphaR*absAlphaR);
      Double_t bR = nR/absAlphaR - absAlphaR; 
      return N*aR/TMath::Power(bR - t, nR);
    }
    else if(t < -absAlphaR && t >= -absAlphaL)
    {
      Double_t aL = AL*TMath::Power(nL/absAlphaL,nL)*exp(-0.5*absAlphaL*absAlphaL);
      Double_t bL = nL/absAlphaL - absAlphaL; 
      return aL/TMath::Power(bL - t, nL);  
    }
    else 
    {
      N*exp(-0.5*t*t);
    }
}

Double_t CrystalBallFunctionL_plus_CrystalBallFunctionL(Double_t *x, Double_t *par)
{
   Double_t y = CrystalBallFunctionL(x,par)+CrystalBallFunctionR(x,&par[5]);
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


