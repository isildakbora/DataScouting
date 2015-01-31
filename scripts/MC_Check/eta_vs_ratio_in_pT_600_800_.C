{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_600_800/eta_vs_ratio_in_pT_600_800
//=========  (Sun Jan 25 13:36:03 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_600_800 = new TCanvas("eta_vs_ratio_in_pT_600_800", "eta_vs_ratio_in_pT_600_800",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_600_800->SetHighLightColor(2);
   eta_vs_ratio_in_pT_600_800->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_600_800->SetFillColor(0);
   eta_vs_ratio_in_pT_600_800->SetBorderMode(0);
   eta_vs_ratio_in_pT_600_800->SetBorderSize(2);
   eta_vs_ratio_in_pT_600_800->SetTickx(1);
   eta_vs_ratio_in_pT_600_800->SetTicky(1);
   eta_vs_ratio_in_pT_600_800->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_600_800->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_600_800->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_600_800->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_600_800->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_600_800->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_600_800->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_600_800->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_600_800");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,1.004799);
   gre->SetPointError(0,0.25,0.0003864252);
   gre->SetPoint(1,0.75,1.00594);
   gre->SetPointError(1,0.25,0.0008267306);
   gre->SetPoint(2,1.25,1.005385);
   gre->SetPointError(2,0.25,0.001423723);
   gre->SetPoint(3,1.75,2.781342e-309);
   gre->SetPointError(3,0.25,0);
   gre->SetPoint(4,2.25,0);
   gre->SetPointError(4,0.25,2.215276e-314);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","eta_vs_ratio_in_pT_600_800",100,0,2.75);
   Graph_Graph4->SetMinimum(0.9);
   Graph_Graph4->SetMaximum(1.1);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);
   Graph_Graph4->SetLineStyle(0);
   Graph_Graph4->SetMarkerStyle(20);
   Graph_Graph4->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph4);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4243624,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_600_800");
   pt->Draw();
   eta_vs_ratio_in_pT_600_800->Modified();
   eta_vs_ratio_in_pT_600_800->cd();
   eta_vs_ratio_in_pT_600_800->SetSelected(eta_vs_ratio_in_pT_600_800);
}
