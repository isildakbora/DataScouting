{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_400_600/eta_vs_ratio_in_pT_400_600
//=========  (Wed Jan  7 23:30:01 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_400_600 = new TCanvas("eta_vs_ratio_in_pT_400_600", "eta_vs_ratio_in_pT_400_600",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_400_600->SetHighLightColor(2);
   eta_vs_ratio_in_pT_400_600->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_400_600->SetFillColor(0);
   eta_vs_ratio_in_pT_400_600->SetBorderMode(0);
   eta_vs_ratio_in_pT_400_600->SetBorderSize(2);
   eta_vs_ratio_in_pT_400_600->SetTickx(1);
   eta_vs_ratio_in_pT_400_600->SetTicky(1);
   eta_vs_ratio_in_pT_400_600->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_400_600->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_400_600->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_400_600->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_400_600->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_400_600->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_400_600->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_400_600->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_400_600");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0.9882118);
   gre->SetPointError(0,0.25,8.414168e-05);
   gre->SetPoint(1,0.75,0.9844585);
   gre->SetPointError(1,0.25,0.0001129508);
   gre->SetPoint(2,1.25,0.9767045);
   gre->SetPointError(2,0.25,0.0001550661);
   gre->SetPoint(3,1.75,0.98033);
   gre->SetPointError(3,0.25,0.000252562);
   gre->SetPoint(4,2.25,0.9597487);
   gre->SetPointError(4,0.25,0.00130041);
   
   TH1F *Graph_Graph3 = new TH1F("Graph_Graph3","eta_vs_ratio_in_pT_400_600",100,0,2.75);
   Graph_Graph3->SetMinimum(0.9);
   Graph_Graph3->SetMaximum(1.1);
   Graph_Graph3->SetDirectory(0);
   Graph_Graph3->SetStats(0);
   Graph_Graph3->SetLineStyle(0);
   Graph_Graph3->SetMarkerStyle(20);
   Graph_Graph3->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph3->GetXaxis()->SetLabelFont(42);
   Graph_Graph3->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph3->GetXaxis()->SetTitleFont(42);
   Graph_Graph3->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph3->GetYaxis()->SetLabelFont(42);
   Graph_Graph3->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph3->GetYaxis()->SetTitleFont(42);
   Graph_Graph3->GetZaxis()->SetLabelFont(42);
   Graph_Graph3->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph3->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph3->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph3);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4243624,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_400_600");
   pt->Draw();
   eta_vs_ratio_in_pT_400_600->Modified();
   eta_vs_ratio_in_pT_400_600->cd();
   eta_vs_ratio_in_pT_400_600->SetSelected(eta_vs_ratio_in_pT_400_600);
}
