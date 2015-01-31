{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_2900_3400/eta_vs_ratio_in_pT_2900_3400
//=========  (Wed Jan  7 11:55:52 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_2900_3400 = new TCanvas("eta_vs_ratio_in_pT_2900_3400", "eta_vs_ratio_in_pT_2900_3400",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_2900_3400->SetHighLightColor(2);
   eta_vs_ratio_in_pT_2900_3400->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_2900_3400->SetFillColor(0);
   eta_vs_ratio_in_pT_2900_3400->SetBorderMode(0);
   eta_vs_ratio_in_pT_2900_3400->SetBorderSize(2);
   eta_vs_ratio_in_pT_2900_3400->SetTickx(1);
   eta_vs_ratio_in_pT_2900_3400->SetTicky(1);
   eta_vs_ratio_in_pT_2900_3400->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_2900_3400->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_2900_3400->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_2900_3400->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_2900_3400->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_2900_3400->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_2900_3400->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_2900_3400->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_2900_3400");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0);
   gre->SetPointError(0,0.25,0);
   gre->SetPoint(1,0.75,0);
   gre->SetPointError(1,0.25,0);
   gre->SetPoint(2,1.25,0);
   gre->SetPointError(2,0.25,0);
   gre->SetPoint(3,1.75,0);
   gre->SetPointError(3,0.25,0);
   gre->SetPoint(4,2.25,0);
   gre->SetPointError(4,0.25,0);
   
   TH1F *Graph_Graph11 = new TH1F("Graph_Graph11","eta_vs_ratio_in_pT_2900_3400",100,0,2.75);
   Graph_Graph11->SetMinimum(0.9);
   Graph_Graph11->SetMaximum(1.1);
   Graph_Graph11->SetDirectory(0);
   Graph_Graph11->SetStats(0);
   Graph_Graph11->SetLineStyle(0);
   Graph_Graph11->SetMarkerStyle(20);
   Graph_Graph11->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph11->GetXaxis()->SetLabelFont(42);
   Graph_Graph11->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph11->GetXaxis()->SetTitleFont(42);
   Graph_Graph11->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph11->GetYaxis()->SetLabelFont(42);
   Graph_Graph11->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph11->GetYaxis()->SetTitleFont(42);
   Graph_Graph11->GetZaxis()->SetLabelFont(42);
   Graph_Graph11->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph11);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4579195,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_2900_3400");
   pt->Draw();
   eta_vs_ratio_in_pT_2900_3400->Modified();
   eta_vs_ratio_in_pT_2900_3400->cd();
   eta_vs_ratio_in_pT_2900_3400->SetSelected(eta_vs_ratio_in_pT_2900_3400);
}
