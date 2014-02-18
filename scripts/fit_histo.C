#ifndef __CINT__
#include "RooGlobalFunc.h"
#endif
#include "RooRealVar.h"
#include "RooDataSet.h"
#include "RooGaussian.h"
#include "TCanvas.h"
#include "RooPlot.h"
#include "TAxis.h"
#include <TH1.h>
#include <TCanvas.h>
#include <utility>
#include "DSComp.C"

using namespace RooFit ;

void fit_histo()
{
    ROOT::Math::MinimizerOptions::SetDefaultMinimizer("Minuit2");
    //gROOT->ProcessLine(".L DSComp.C");
    TString histoname;
    TH1F *hDeltapT[8][5];
    TFile *f = new TFile("Delta_pT_histograms_legends.root");
    TFile *fresolution = new TFile("Delta_pT_Resolution.root", "RECREATE");
    TCanvas *i_can[8][5];
    TString name;
    float pTbins[]  = {30., 103., 206., 309., 413., 515., 618., 721., 1237.};
    const Int_t   n_pTbins  = sizeof(pTbins)/sizeof(float)-1;

    float etaBins[] = {0., 0.5, 1.0, 1.5, 2.0, 2.5};
    const Int_t   n_etaBins = sizeof(etaBins)/sizeof(float)-1;

    for (int i = 0; i < n_pTbins; ++i)
    {
        for (int j=0; j< n_etaBins; ++j)
        {
            histoname      = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
            hDeltapT[i][j] = (TH1F*)f->FindObjectAny(histoname+"pT12");
            i_can[i][j] =  new TCanvas(histoname+"pT12");
            if(hDeltapT[i][j]->GetEntries()>1000)hDeltapT[i][j]->Rebin(4);
            else hDeltapT[i][j]->Rebin(2);
        }   
    }

    TCanvas *can = new TCanvas("DSComparison","DSComparison",1200,1200);

    TF1 *cbfit[8][5];
    can->Divide(3,3);

    Double_t maxVal, mean, RMS;
    for (int i = 0; i < n_pTbins; ++i)
    {
        for (int j=0; j<n_etaBins; ++j)
        {
            std::cout << i << "\t" << j << std::endl;
            name = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
           
            gStyle->SetOptStat("nemr");
            gStyle->SetOptFit(0011);

            maxVal = hDeltapT[i][j]->GetBinContent(hDeltapT[i][j]->GetMaximumBin());
            mean   = hDeltapT[i][j]->GetMean();
            RMS    = hDeltapT[i][j]->GetRMS();

            cbfit[i][j] = new TF1(name, DoubleCrystalBallFunction, mean-2*RMS, mean+2*RMS, 7);
            cbfit[i][j]->SetParNames("A_{1}","#alpha_{1}","#alpha_{2}","n_{1}","n_{2}","#mu","#sigma");
            cbfit[i][j]->SetParameters(maxVal, 0.9, 3.3, 50., 50., mean, RMS);
            /*cbfit[i][j]->SetParLimits(0, 0.9*maxVal, 1.1*maxVal);
            cbfit[i][j]->SetParLimits(1, 0., 5.);
            cbfit[i][j]->SetParLimits(2, 0., 5.);
            cbfit[i][j]->SetParLimits(3, 0., 100);
            cbfit[i][j]->SetParLimits(4, 0., 100);
            //cbfit[i][j]->SetParLimits(5, 0.5*mean, 1.5*mean);
            cbfit[i][j]->SetParLimits(6, 0.8*RMS, 1.2*RMS);*/
            cbfit[i][j]->SetLineColor(kRed+1);

            if(i*5+j+1<10)can->cd(i*5+j+1);
            //gPad->SetLogy();
            hDeltapT[i][j]->Fit(name, "REQ0+");
            hDeltapT[i][j]->Fit(name, "REQ");
            hDeltapT[i][j]->GetXaxis()->SetRangeUser(mean-2*RMS, mean+2*RMS);
            hDeltapT[i][j]->GetXaxis()->SetTitle("#Deltap_{T}/p_{T}");
            hDeltapT[i][j]->GetXaxis()->SetLabelSize(0.04);
            hDeltapT[i][j]->GetYaxis()->SetLabelSize(0.04);

            i_can[i][j]   ->cd();
            hDeltapT[i][j]->Draw("E1");
            cbfit[i][j]   ->Draw("same");
            i_can[i][j]   ->SaveAs(name.ReplaceAll(".", "_")+".pdf");
            fresolution->cd();
            cbfit[i][j]->Write();
        }
    }
    can->SaveAs("DSCompAllInOne.pdf");   
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
