{
//=========Macro generated from canvas: nPVz_eta_1_/nPVz_eta_1_
//=========  (Fri Jan 23 11:22:29 2015) by ROOT version5.34/05
   TCanvas *nPVz_eta_1_ = new TCanvas("nPVz_eta_1_", "nPVz_eta_1_",11,73,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   nPVz_eta_1_->SetHighLightColor(2);
   nPVz_eta_1_->Range(-303.8785,0.8682927,1595.362,1.112195);
   nPVz_eta_1_->SetFillColor(0);
   nPVz_eta_1_->SetBorderMode(0);
   nPVz_eta_1_->SetBorderSize(2);
   nPVz_eta_1_->SetTickx(1);
   nPVz_eta_1_->SetTicky(1);
   nPVz_eta_1_->SetLeftMargin(0.16);
   nPVz_eta_1_->SetRightMargin(0.05);
   nPVz_eta_1_->SetTopMargin(0.05);
   nPVz_eta_1_->SetBottomMargin(0.13);
   nPVz_eta_1_->SetFrameFillStyle(0);
   nPVz_eta_1_->SetFrameBorderMode(0);
   nPVz_eta_1_->SetFrameFillStyle(0);
   nPVz_eta_1_->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("pT_vs_ratio_in_eta_1.5_2.0");
   gre->SetFillColor(1);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.010059);
   gre->SetPointError(0,100,0.001275313);
   gre->SetPoint(1,300,3.111098e+231);
   gre->SetPointError(1,100,-2.681562e+154);
   gre->SetPoint(2,500,9.881313e-324);
   gre->SetPointError(2,100,6.950504e-310);
   gre->SetPoint(3,700,2.781385e-309);
   gre->SetPointError(3,100,6.950505e-310);
   gre->SetPoint(4,900,9.172407e+170);
   gre->SetPointError(4,100,0.01798946);
   gre->SetPoint(5,1100,4.012974e+35);
   gre->SetPointError(5,100,-2.681562e+154);
   gre->SetPoint(6,1300,5.200764e+98);
   gre->SetPointError(6,100,-2.681562e+154);
   gre->SetPoint(7,1650,1.673022e-76);
   gre->SetPointError(7,250,6.950504e-310);
   gre->SetPoint(8,2150,4.336581e+150);
   gre->SetPointError(8,250,-2.681562e+154);
   gre->SetPoint(9,2650,1.743889e-76);
   gre->SetPointError(9,250,-2.681562e+154);
   gre->SetPoint(10,3150,3.694142e-86);
   gre->SetPointError(10,250,2.167683e-314);
   gre->SetPoint(11,3650,6.257735e-309);
   gre->SetPointError(11,250,3.476393e-309);
   gre->SetPoint(12,4150,9.172407e+170);
   gre->SetPointError(12,250,2.152471e-314);
   
   TH1F *Graph_Graph10 = new TH1F("Graph_Graph10","pT_vs_ratio_in_eta_1.5_2.0",100,0,4840);
   Graph_Graph10->SetMinimum(0.9);
   Graph_Graph10->SetMaximum(1.1);
   Graph_Graph10->SetDirectory(0);
   Graph_Graph10->SetStats(0);
   Graph_Graph10->SetLineStyle(0);
   Graph_Graph10->SetMarkerStyle(20);
   Graph_Graph10->GetXaxis()->SetTitle("pT [GeV]");
   Graph_Graph10->GetXaxis()->SetRange(1,31);
   Graph_Graph10->GetXaxis()->SetLabelFont(42);
   Graph_Graph10->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph10->GetXaxis()->SetTitleFont(42);
   Graph_Graph10->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph10->GetYaxis()->SetLabelFont(42);
   Graph_Graph10->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph10->GetYaxis()->SetTitleFont(42);
   Graph_Graph10->GetZaxis()->SetLabelFont(42);
   Graph_Graph10->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph10);
   
   gre->Draw("ap");
   
   gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.009361);
   gre->SetPointError(0,100,0.001010807);
   gre->SetPoint(1,300,-2.681562e+154);
   gre->SetPointError(1,100,-2.681562e+154);
   gre->SetPoint(2,500,9.881313e-324);
   gre->SetPointError(2,100,6.950505e-310);
   gre->SetPoint(3,700,2.781385e-309);
   gre->SetPointError(3,100,6.950505e-310);
   gre->SetPoint(4,900,2.152426e-314);
   gre->SetPointError(4,100,-2.681562e+154);
   gre->SetPoint(5,1100,0);
   gre->SetPointError(5,100,1.730606e-77);
   gre->SetPoint(6,1300,6.950505e-310);
   gre->SetPointError(6,100,2.152471e-314);
   gre->SetPoint(7,1650,6.950505e-310);
   gre->SetPointError(7,250,3.131513e-294);
   gre->SetPoint(8,2150,2.171699e-314);
   gre->SetPointError(8,250,2.152458e-314);
   gre->SetPoint(9,2650,3.131537e-294);
   gre->SetPointError(9,250,0);
   gre->SetPoint(10,3150,2.152458e-314);
   gre->SetPointError(10,250,0);
   gre->SetPoint(11,3650,1.124658e-312);
   gre->SetPointError(11,250,4.630132e-66);
   gre->SetPoint(12,4150,6.950505e-310);
   gre->SetPointError(12,250,0);
   
   TH1F *Graph_Graph11 = new TH1F("Graph_Graph11","Graph",100,0,4840);
   Graph_Graph11->SetMinimum(0.9);
   Graph_Graph11->SetMaximum(1.1);
   Graph_Graph11->SetDirectory(0);
   Graph_Graph11->SetStats(0);
   Graph_Graph11->SetLineStyle(0);
   Graph_Graph11->SetMarkerStyle(20);
   Graph_Graph11->GetXaxis()->SetTitle("pT [GeV]");
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
   
   gre->Draw("p");
   
   TLegend *leg = new TLegend(0.6,0.7,0.9,0.9,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","nPVzbins_0_7","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   entry=leg->AddEntry("Graph","nPVzbins_7_15","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4075839,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("pT_vs_ratio_in_eta_1.5_2.0");
   pt->Draw();
   nPVz_eta_1_->Modified();
   nPVz_eta_1_->cd();
   nPVz_eta_1_->SetSelected(nPVz_eta_1_);
}
