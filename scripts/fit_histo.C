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
    //gROOT->ProcessLine(".L DSComp.C");
    TString histoname;
    TH1F *hDeltapT[8][5];
	TFile *f = new TFile("Delta_pT_histograms.root");
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
            hDeltapT[i][j] = (TH1F*)f->FindObjectAny(histoname);
            i_can[i][j] =  new TCanvas(histoname);
            if(hDeltapT[i][j]->GetEntries()>3000)hDeltapT[i][j]->Rebin(6);
            else hDeltapT[i][j]->Rebin(3);
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

            maxVal = hDeltapT[i][j]->GetBinContent(hDeltapT[i][j]->GetMaximumBin());
            mean   = hDeltapT[i][j]->GetMean();
            RMS    = hDeltapT[i][j]->GetRMS();

            cbfit[i][j] = new TF1(name, DoubleCrystalBallFunction, mean-4*RMS, mean+4*RMS, 7);
            cbfit[i][j]->SetParNames("A_{1}","#alpha_{1}","#alpha_{2}","n_{1}","n_{2}","#mu","#sigma");
            cbfit[i][j]->SetParameters(maxVal, 2., 2., 2., 2., mean, RMS);
            //cbfit[i][j]->SetParLimits(3, 0, 10);
            cbfit[i][j]   ->SetLineColor(kRed+1);

            gStyle->SetOptStat(1101);

            if(i*5+j+1<10)can->cd(i*5+j+1);
            //gPad->SetLogy();
            hDeltapT[i][j]->Fit(name, "REMQN+");
            hDeltapT[i][j]->Fit(name, "REMQ");
            hDeltapT[i][j]->GetXaxis()->SetRangeUser(mean-6*RMS, mean+6*RMS);
            hDeltapT[i][j]->GetXaxis()->SetTitle("#Deltap_{T}/p_{T}");
            hDeltapT[i][j]->GetXaxis()->SetLabelSize(0.04);
            hDeltapT[i][j]->GetYaxis()->SetLabelSize(0.04);

            i_can[i][j]   ->cd();
            hDeltapT[i][j]->Draw("E1");
            cbfit[i][j]   ->Draw("same");
            i_can[i][j]   ->SaveAs(name.ReplaceAll(".", "_")+".pdf");
        }
    }
    can->SaveAs("DSCompAllInOne.pdf");
}

Double_t DoubleCrystalBallFunction(Double_t *xx, Double_t *par) {
    // variable x
    Double_t x = xx[0];
    // parameters alpha, n, x0, sigma
    Double_t A = par[0];
    Double_t alpha1 = par[1];
    Double_t alpha2 = par[2];
    Double_t n1 = par[3];
    Double_t n2 = par[4];
    Double_t x0 = par[5];
    Double_t sigma = par[6];

    Double_t absAlpha1 = fabs((Double_t)alpha1);
    Double_t absAlpha2 = fabs((Double_t)alpha2);
    
    Double_t t = (x-x0)/sigma;
    Double_t a1 = pow(n1/absAlpha1,n1)*exp(-0.5*absAlpha1*absAlpha1);
    Double_t b1 = n1/absAlpha1 - absAlpha1; 
    Double_t a2 = pow(n2/absAlpha2,n2)*exp(-0.5*absAlpha2*absAlpha2);
    Double_t b2 = n2/absAlpha2 - absAlpha2;

    if (t < -alpha1)        return A*a1*TMath::Power(b1 - t, -n1);
    else if (t > alpha2)    return A*a2*TMath::Power(b2 - t, -n2);
    else                    return A*exp(-0.5*t*t);
}
