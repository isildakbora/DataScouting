{
//=========Macro generated from canvas: nPVz_eta_0_/nPVz_eta_0_
//=========  (Fri Jan 23 11:22:28 2015) by ROOT version5.34/05
   TCanvas *nPVz_eta_0_ = new TCanvas("nPVz_eta_0_", "nPVz_eta_0_",11,73,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   nPVz_eta_0_->SetHighLightColor(2);
   nPVz_eta_0_->Range(-303.8785,0.8682927,1595.362,1.112195);
   nPVz_eta_0_->SetFillColor(0);
   nPVz_eta_0_->SetBorderMode(0);
   nPVz_eta_0_->SetBorderSize(2);
   nPVz_eta_0_->SetTickx(1);
   nPVz_eta_0_->SetTicky(1);
   nPVz_eta_0_->SetLeftMargin(0.16);
   nPVz_eta_0_->SetRightMargin(0.05);
   nPVz_eta_0_->SetTopMargin(0.05);
   nPVz_eta_0_->SetBottomMargin(0.13);
   nPVz_eta_0_->SetFrameFillStyle(0);
   nPVz_eta_0_->SetFrameBorderMode(0);
   nPVz_eta_0_->SetFrameFillStyle(0);
   nPVz_eta_0_->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("pT_vs_ratio_in_eta_0.5_1.0");
   gre->SetFillColor(1);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.01542);
   gre->SetPointError(0,100,0.0007170707);
   gre->SetPoint(1,300,2.003905);
   gre->SetPointError(1,100,-2.681562e+154);
   gre->SetPoint(2,500,9.881313e-324);
   gre->SetPointError(2,100,-2.534429e-93);
   gre->SetPoint(3,700,2.781385e-309);
   gre->SetPointError(3,100,-2.864951e-54);
   gre->SetPoint(4,900,9.172407e+170);
   gre->SetPointError(4,100,0.01642537);
   gre->SetPoint(5,1100,4.012974e+35);
   gre->SetPointError(5,100,-2.681562e+154);
   gre->SetPoint(6,1300,5.200764e+98);
   gre->SetPointError(6,100,-1.706916e-145);
   gre->SetPoint(7,1650,1.673022e-76);
   gre->SetPointError(7,250,8.030682e-64);
   gre->SetPoint(8,2150,4.336581e+150);
   gre->SetPointError(8,250,-4.344065e-311);
   gre->SetPoint(9,2650,2.176372e-76);
   gre->SetPointError(9,250,-2.681562e+154);
   gre->SetPoint(10,3150,3.694142e-86);
   gre->SetPointError(10,250,-1.445591e-286);
   gre->SetPoint(11,3650,5.562685e-309);
   gre->SetPointError(11,250,3.60796e-188);
   gre->SetPoint(12,4150,9.172407e+170);
   gre->SetPointError(12,250,-2.300286e-279);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","pT_vs_ratio_in_eta_0.5_1.0",100,0,4840);
   Graph_Graph4->SetMinimum(0.9);
   Graph_Graph4->SetMaximum(1.1);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);
   Graph_Graph4->SetLineStyle(0);
   Graph_Graph4->SetMarkerStyle(20);
   Graph_Graph4->GetXaxis()->SetTitle("pT [GeV]");
   Graph_Graph4->GetXaxis()->SetRange(1,31);
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
   
   gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetMarkerColor(2);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.011978);
   gre->SetPointError(0,100,0.0004948973);
   gre->SetPoint(1,300,1.00979);
   gre->SetPointError(1,100,0.001041266);
   gre->SetPoint(2,500,9.881313e-324);
   gre->SetPointError(2,100,6.950504e-310);
   gre->SetPoint(3,700,2.781385e-309);
   gre->SetPointError(3,100,3.476393e-309);
   gre->SetPoint(4,900,2.152426e-314);
   gre->SetPointError(4,100,2.152426e-314);
   gre->SetPoint(5,1100,6.950504e-310);
   gre->SetPointError(5,100,6.950504e-310);
   gre->SetPoint(6,1300,6.950504e-310);
   gre->SetPointError(6,100,6.950504e-310);
   gre->SetPoint(7,1650,6.950504e-310);
   gre->SetPointError(7,250,6.950504e-310);
   gre->SetPoint(8,2150,9.172407e+170);
   gre->SetPointError(8,250,-2.320363e+77);
   gre->SetPoint(9,2650,1.71677e+262);
   gre->SetPointError(9,250,1.49458e-154);
   gre->SetPoint(10,3150,2.433617e+35);
   gre->SetPointError(10,250,1.117085e+267);
   gre->SetPoint(11,3650,7.060766e-71);
   gre->SetPointError(11,250,2.56981e+161);
   gre->SetPoint(12,4150,4.62745e-66);
   gre->SetPointError(12,250,1.301389e+36);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","Graph",100,0,4840);
   Graph_Graph5->SetMinimum(0.9);
   Graph_Graph5->SetMaximum(1.1);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetTitle("pT [GeV]");
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
   
   gre->Draw("p");
   
   gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetMarkerColor(3);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.009587);
   gre->SetPointError(0,100,0.0009854723);
   gre->SetPoint(1,300,-1.290745e-231);
   gre->SetPointError(1,100,-1.730606e-77);
   gre->SetPoint(2,500,9.881313e-324);
   gre->SetPointError(2,100,6.950503e-310);
   gre->SetPoint(3,700,2.781385e-309);
   gre->SetPointError(3,100,3.476393e-309);
   gre->SetPoint(4,900,2.152426e-314);
   gre->SetPointError(4,100,2.152426e-314);
   gre->SetPoint(5,1100,6.950504e-310);
   gre->SetPointError(5,100,6.950504e-310);
   gre->SetPoint(6,1300,6.950504e-310);
   gre->SetPointError(6,100,6.950504e-310);
   gre->SetPoint(7,1650,6.950504e-310);
   gre->SetPointError(7,250,6.950504e-310);
   gre->SetPoint(8,2150,3.111098e+231);
   gre->SetPointError(8,250,-2.320363e+77);
   gre->SetPoint(9,2650,-4.344065e-311);
   gre->SetPointError(9,250,3.111098e+231);
   gre->SetPoint(10,3150,2.152471e-314);
   gre->SetPointError(10,250,2.152471e-314);
   gre->SetPoint(11,3650,3.131513e-294);
   gre->SetPointError(11,250,3.131513e-294);
   gre->SetPoint(12,4150,2.152458e-314);
   gre->SetPointError(12,250,2.152458e-314);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","Graph",100,0,4840);
   Graph_Graph6->SetMinimum(0.9);
   Graph_Graph6->SetMaximum(1.1);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetTitle("pT [GeV]");
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
   entry=leg->AddEntry("Graph","nPVzbins_15_25","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(3);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.4075839,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("pT_vs_ratio_in_eta_0.5_1.0");
   pt->Draw();
   nPVz_eta_0_->Modified();
   nPVz_eta_0_->cd();
   nPVz_eta_0_->SetSelected(nPVz_eta_0_);
}
