{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_100_200/eta_vs_ratio_in_pT_100_200
//=========  (Sun Jan 25 16:21:18 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_100_200 = new TCanvas("eta_vs_ratio_in_pT_100_200", "eta_vs_ratio_in_pT_100_200",200,222,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_100_200->SetHighLightColor(2);
   eta_vs_ratio_in_pT_100_200->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_100_200->SetFillColor(0);
   eta_vs_ratio_in_pT_100_200->SetBorderMode(0);
   eta_vs_ratio_in_pT_100_200->SetBorderSize(2);
   eta_vs_ratio_in_pT_100_200->SetTickx(1);
   eta_vs_ratio_in_pT_100_200->SetTicky(1);
   eta_vs_ratio_in_pT_100_200->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_100_200->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_100_200->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_100_200->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_100_200->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_100_200->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_100_200->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_100_200->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_100_200");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,1.014777);
   gre->SetPointError(0,0.25,0.0002157344);
   gre->SetPoint(1,0.75,1.012388);
   gre->SetPointError(1,0.25,0.0003156934);
   gre->SetPoint(2,1.25,1.007923);
   gre->SetPointError(2,0.25,0.0003264748);
   gre->SetPoint(3,1.75,1.012474);
   gre->SetPointError(3,0.25,0.0004750869);
   gre->SetPoint(4,2.25,1.052364);
   gre->SetPointError(4,0.25,0.001024686);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","eta_vs_ratio_in_pT_100_200",100,0,2.75);
   Graph_Graph2->SetMinimum(0.9);
   Graph_Graph2->SetMaximum(1.1);
   Graph_Graph2->SetDirectory(0);
   Graph_Graph2->SetStats(0);
   Graph_Graph2->SetLineStyle(0);
   Graph_Graph2->SetMarkerStyle(20);
   Graph_Graph2->GetXaxis()->SetTitle("eta [GeV]");
   Graph_Graph2->GetXaxis()->SetLabelFont(42);
   Graph_Graph2->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph2->GetXaxis()->SetTitleFont(42);
   Graph_Graph2->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph2->GetYaxis()->SetLabelFont(42);
   Graph_Graph2->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph2->GetYaxis()->SetTitleFont(42);
   Graph_Graph2->GetZaxis()->SetLabelFont(42);
   Graph_Graph2->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph2->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph2->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph2);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4243624,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("eta_vs_ratio_in_pT_100_200");
   pt->Draw();
   eta_vs_ratio_in_pT_100_200->Modified();
   eta_vs_ratio_in_pT_100_200->cd();
   eta_vs_ratio_in_pT_100_200->SetSelected(eta_vs_ratio_in_pT_100_200);
}
