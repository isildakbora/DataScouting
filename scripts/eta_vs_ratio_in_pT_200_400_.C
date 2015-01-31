{
//=========Macro generated from canvas: eta_vs_ratio_in_pT_200_400/eta_vs_ratio_in_pT_200_400
//=========  (Wed Jan  7 23:21:49 2015) by ROOT version5.34/05
   TCanvas *eta_vs_ratio_in_pT_200_400 = new TCanvas("eta_vs_ratio_in_pT_200_400", "eta_vs_ratio_in_pT_200_400",200,222,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   eta_vs_ratio_in_pT_200_400->SetHighLightColor(2);
   eta_vs_ratio_in_pT_200_400->Range(-0.556962,0.8682927,2.924051,1.112195);
   eta_vs_ratio_in_pT_200_400->SetFillColor(0);
   eta_vs_ratio_in_pT_200_400->SetBorderMode(0);
   eta_vs_ratio_in_pT_200_400->SetBorderSize(2);
   eta_vs_ratio_in_pT_200_400->SetTickx(1);
   eta_vs_ratio_in_pT_200_400->SetTicky(1);
   eta_vs_ratio_in_pT_200_400->SetLeftMargin(0.16);
   eta_vs_ratio_in_pT_200_400->SetRightMargin(0.05);
   eta_vs_ratio_in_pT_200_400->SetTopMargin(0.05);
   eta_vs_ratio_in_pT_200_400->SetBottomMargin(0.13);
   eta_vs_ratio_in_pT_200_400->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_200_400->SetFrameBorderMode(0);
   eta_vs_ratio_in_pT_200_400->SetFrameFillStyle(0);
   eta_vs_ratio_in_pT_200_400->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(5);
   gre->SetName("Graph");
   gre->SetTitle("eta_vs_ratio_in_pT_200_400");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,0.25,1.004754);
   gre->SetPointError(0,0.25,4.036801e-05);
   gre->SetPoint(1,0.75,0.9989269);
   gre->SetPointError(1,0.25,5.049976e-05);
   gre->SetPoint(2,1.25,0.9896635);
   gre->SetPointError(2,0.25,6.451672e-05);
   gre->SetPoint(3,1.75,0.990174);
   gre->SetPointError(3,0.25,8.83653e-05);
   gre->SetPoint(4,2.25,0.9808511);
   gre->SetPointError(4,0.25,0.0002957407);
   
   TH1F *Graph_Graph2 = new TH1F("Graph_Graph2","eta_vs_ratio_in_pT_200_400",100,0,2.75);
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
   TText *text = pt->AddText("eta_vs_ratio_in_pT_200_400");
   pt->Draw();
   eta_vs_ratio_in_pT_200_400->Modified();
   eta_vs_ratio_in_pT_200_400->cd();
   eta_vs_ratio_in_pT_200_400->SetSelected(eta_vs_ratio_in_pT_200_400);
}
