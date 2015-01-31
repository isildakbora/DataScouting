{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_1000_1200/eta_vs_ratio_in_pT_1000_1200
//=========  (Wed Jan  7 23:21:52 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_1000_1200 = new TCanvas("eta_vs_ratio_in_pT_1000_1200", "eta_vs_ratio_in_pT_1000_1200",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_1000_1200->SetHighLightColor(2);
   eta_vs_ratio_in_pT_1000_1200->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_1000_1200->SetFillColor(0);
   eta_vs_ratio_in_pT_1000_1200->SetBorderMode(0);
   eta_vs_ratio_in_pT_1000_1200->SetBorderSize(2);
   eta_vs_ratio_in_pT_1000_1200->SetTickx(1);
   eta_vs_ratio_in_pT_1000_1200->SetTicky(1);
   eta_vs_ratio_in_pT_1000_1200->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_1000_1200->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_1000_1200->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_1000_1200->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_1000_1200->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_1000_1200->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_1000_1200->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_1000_1200->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_1000_1200");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0.9887097);
   gre->SetPointError(0,0.25,0.001223749);
   gre->SetPoint(1,0.75,0.9872157);
   gre->SetPointError(1,0.25,0.00219523);
   gre->SetPoint(2,1.25,1.482197e-323);
   gre->SetPointError(2,0.25,0);
   gre->SetPoint(3,1.75,0);
   gre->SetPointError(3,0.25,0);
   gre->SetPoint(4,2.25,-1.29074e-231);
   gre->SetPointError(4,0.25,2.183532e-314);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","eta_vs_ratio_in_pT_1000_1200",100,0,2.75);
   Graph_Graph6->SetMinimum(0.9);
   Graph_Graph6->SetMaximum(1.1);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph6);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4579195,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_1000_1200");
   pt->Draw();
   eta_vs_ratio_in_pT_1000_1200->Modified();
   eta_vs_ratio_in_pT_1000_1200->cd();
   eta_vs_ratio_in_pT_1000_1200->SetSelected(eta_vs_ratio_in_pT_1000_1200);
}
