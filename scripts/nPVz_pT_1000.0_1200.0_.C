{
//=========Macro generated from canvas: nPVZ_pT_1000_/nPVz_pT_1000_
//=========  (Wed Jan  7 23:09:45 2015) by ROOT version5.34/05
   TCanvas *nPVZ_pT_1000_ = new TCanvas("nPVZ_pT_1000_", "nPVz_pT_1000_",11,73,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   nPVZ_pT_1000_->SetHighLightColor(2);
   nPVZ_pT_1000_->Range(-0.556962,0.8682927,2.924051,1.112195);
   nPVZ_pT_1000_->SetFillColor(0);
   nPVZ_pT_1000_->SetBorderMode(0);
   nPVZ_pT_1000_->SetBorderSize(2);
   nPVZ_pT_1000_->SetTickx(1);
   nPVZ_pT_1000_->SetTicky(1);
   nPVZ_pT_1000_->SetLeftMargin(0.16);
   nPVZ_pT_1000_->SetRightMargin(0.05);
   nPVZ_pT_1000_->SetTopMargin(0.05);
   nPVZ_pT_1000_->SetBottomMargin(0.13);
   nPVZ_pT_1000_->SetFrameFillStyle(0);
   nPVZ_pT_1000_->SetFrameBorderMode(0);
   nPVZ_pT_1000_->SetFrameFillStyle(0);
   nPVZ_pT_1000_->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_1000.0_1200.0");
   gre->SetFillColor(1);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0.9878667);
   gre->SetPointError(0,0.25,0.00156942);
   gre->SetPoint(1,0.75,2.686782e+154);
   gre->SetPointError(1,0.25,-3.105036e+231);
   gre->SetPoint(2,1.25,9.881313e-324);
   gre->SetPointError(2,0.25,6.930154e-310);
   gre->SetPoint(3,1.75,2.781342e-309);
   gre->SetPointError(3,0.25,6.930154e-310);
   gre->SetPoint(4,2.25,2.27174e-314);
   gre->SetPointError(4,0.25,2.686782e+154);
   
   TH1F *Graph_Graph15 = new TH1F("Graph_Graph15","eta_vs_ratio_in_pT_1000.0_1200.0",100,0,2.75);
   Graph_Graph15->SetMinimum(0.9);
   Graph_Graph15->SetMaximum(1.1);
   Graph_Graph15->SetDirectory(0);
   Graph_Graph15->SetStats(0);
   Graph_Graph15->SetLineStyle(0);
   Graph_Graph15->SetMarkerStyle(20);
   Graph_Graph15->GetXaxis()->SetTitle("eta");
   Graph_Graph15->GetXaxis()->SetLabelFont(42);
   Graph_Graph15->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph15->GetXaxis()->SetTitleFont(42);
   Graph_Graph15->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph15->GetYaxis()->SetLabelFont(42);
   Graph_Graph15->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph15->GetYaxis()->SetTitleFont(42);
   Graph_Graph15->GetZaxis()->SetLabelFont(42);
   Graph_Graph15->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph15);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.508255,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_1000.0_1200.0");
   pt->Draw();
   nPVZ_pT_1000_->Modified();
   nPVZ_pT_1000_->cd();
   nPVZ_pT_1000_->SetSelected(nPVZ_pT_1000_);
}
