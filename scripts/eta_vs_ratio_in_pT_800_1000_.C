{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_800_1000/eta_vs_ratio_in_pT_800_1000
//=========  (Wed Jan  7 23:21:51 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_800_1000 = new TCanvas("eta_vs_ratio_in_pT_800_1000", "eta_vs_ratio_in_pT_800_1000",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_800_1000->SetHighLightColor(2);
   eta_vs_ratio_in_pT_800_1000->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_800_1000->SetFillColor(0);
   eta_vs_ratio_in_pT_800_1000->SetBorderMode(0);
   eta_vs_ratio_in_pT_800_1000->SetBorderSize(2);
   eta_vs_ratio_in_pT_800_1000->SetTickx(1);
   eta_vs_ratio_in_pT_800_1000->SetTicky(1);
   eta_vs_ratio_in_pT_800_1000->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_800_1000->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_800_1000->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_800_1000->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_800_1000->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_800_1000->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_800_1000->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_800_1000->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_800_1000");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0.9896728);
   gre->SetPointError(0,0.25,0.0005775499);
   gre->SetPoint(1,0.75,0.986483);
   gre->SetPointError(1,0.25,0.0008984706);
   gre->SetPoint(2,1.25,0.9842815);
   gre->SetPointError(2,0.25,0.001852523);
   gre->SetPoint(3,1.75,2.781342e-309);
   gre->SetPointError(3,0.25,3.474954e-309);
   gre->SetPoint(4,2.25,2.183532e-314);
   gre->SetPointError(4,0.25,2.202936e-314);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","eta_vs_ratio_in_pT_800_1000",100,0,2.75);
   Graph_Graph5->SetMinimum(0.9);
   Graph_Graph5->SetMaximum(1.1);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph5);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4411409,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_800_1000");
   pt->Draw();
   eta_vs_ratio_in_pT_800_1000->Modified();
   eta_vs_ratio_in_pT_800_1000->cd();
   eta_vs_ratio_in_pT_800_1000->SetSelected(eta_vs_ratio_in_pT_800_1000);
}
