{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_0_100/eta_vs_ratio_in_pT_0_100
//=========  (Sun Jan 25 16:21:18 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_0_100 = new TCanvas("eta_vs_ratio_in_pT_0_100", "eta_vs_ratio_in_pT_0_100",80,102,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_0_100->SetHighLightColor(2);
   eta_vs_ratio_in_pT_0_100->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_0_100->SetFillColor(0);
   eta_vs_ratio_in_pT_0_100->SetBorderMode(0);
   eta_vs_ratio_in_pT_0_100->SetBorderSize(2);
   eta_vs_ratio_in_pT_0_100->SetTickx(1);
   eta_vs_ratio_in_pT_0_100->SetTicky(1);
   eta_vs_ratio_in_pT_0_100->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_0_100->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_0_100->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_0_100->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_0_100->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_0_100->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_0_100->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_0_100->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_0_100");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,1.017469);
   gre->SetPointError(0,0.25,0.0007248704);
   gre->SetPoint(1,0.75,1.011361);
   gre->SetPointError(1,0.25,0.0009290233);
   gre->SetPoint(2,1.25,1.006538);
   gre->SetPointError(2,0.25,0.001027935);
   gre->SetPoint(3,1.75,1.016671);
   gre->SetPointError(3,0.25,0.001658281);
   gre->SetPoint(4,2.25,1.080075);
   gre->SetPointError(4,0.25,0.003414579);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","eta_vs_ratio_in_pT_0_100",100,0,2.75);
   Graph_Graph1->SetMinimum(0.9);
   Graph_Graph1->SetMaximum(1.1);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.3908054,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_0_100");
   pt->Draw();
   eta_vs_ratio_in_pT_0_100->Modified();
   eta_vs_ratio_in_pT_0_100->cd();
   eta_vs_ratio_in_pT_0_100->SetSelected(eta_vs_ratio_in_pT_0_100);
}
