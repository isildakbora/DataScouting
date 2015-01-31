{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_1400_1900/eta_vs_ratio_in_pT_1400_1900
//=========  (Wed Jan  7 11:55:48 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_1400_1900 = new TCanvas("eta_vs_ratio_in_pT_1400_1900", "eta_vs_ratio_in_pT_1400_1900",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_1400_1900->SetHighLightColor(2);
   eta_vs_ratio_in_pT_1400_1900->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_1400_1900->SetFillColor(0);
   eta_vs_ratio_in_pT_1400_1900->SetBorderMode(0);
   eta_vs_ratio_in_pT_1400_1900->SetBorderSize(2);
   eta_vs_ratio_in_pT_1400_1900->SetTickx(1);
   eta_vs_ratio_in_pT_1400_1900->SetTicky(1);
   eta_vs_ratio_in_pT_1400_1900->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_1400_1900->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_1400_1900->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_1400_1900->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_1400_1900->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_1400_1900->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_1400_1900->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_1400_1900->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_1400_1900");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,0.9733333);
   gre->SetPointError(0,0.25,0.005786318);
   gre->SetPoint(1,0.75,0.964);
   gre->SetPointError(1,0.25,0);
   gre->SetPoint(2,1.25,0);
   gre->SetPointError(2,0.25,0);
   gre->SetPoint(3,1.75,0);
   gre->SetPointError(3,0.25,0);
   gre->SetPoint(4,2.25,0);
   gre->SetPointError(4,0.25,0);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","eta_vs_ratio_in_pT_1400_1900",100,0,2.75);
   Graph_Graph8->SetMinimum(0.9);
   Graph_Graph8->SetMaximum(1.1);
   Graph_Graph8->SetDirectory(0);
   Graph_Graph8->SetStats(0);
   Graph_Graph8->SetLineStyle(0);
   Graph_Graph8->SetMarkerStyle(20);
   Graph_Graph8->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph8->GetXaxis()->SetLabelFont(42);
   Graph_Graph8->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph8->GetXaxis()->SetTitleFont(42);
   Graph_Graph8->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph8->GetYaxis()->SetLabelFont(42);
   Graph_Graph8->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph8->GetYaxis()->SetTitleFont(42);
   Graph_Graph8->GetZaxis()->SetLabelFont(42);
   Graph_Graph8->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph8);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4579195,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_1400_1900");
   pt->Draw();
   eta_vs_ratio_in_pT_1400_1900->Modified();
   eta_vs_ratio_in_pT_1400_1900->cd();
   eta_vs_ratio_in_pT_1400_1900->SetSelected(eta_vs_ratio_in_pT_1400_1900);
}
