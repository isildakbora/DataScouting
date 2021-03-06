{
//=========Macro generated from canvas: pT_vs_ratio_in_eta_0_5/pT_vs_ratio_in_eta_0_5
//=========  (Fri Jan 23 11:16:59 2015) by ROOT version5.34/05
   TCanvas *pT_vs_ratio_in_eta_0_5 = new TCanvas("pT_vs_ratio_in_eta_0_5", "pT_vs_ratio_in_eta_0_5",0,22,600,600);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   pT_vs_ratio_in_eta_0_5->SetHighLightColor(2);
   pT_vs_ratio_in_eta_0_5->Range(-980.2531,0.8682927,5146.329,1.112195);
   pT_vs_ratio_in_eta_0_5->SetFillColor(0);
   pT_vs_ratio_in_eta_0_5->SetBorderMode(0);
   pT_vs_ratio_in_eta_0_5->SetBorderSize(2);
   pT_vs_ratio_in_eta_0_5->SetTickx(1);
   pT_vs_ratio_in_eta_0_5->SetTicky(1);
   pT_vs_ratio_in_eta_0_5->SetLeftMargin(0.16);
   pT_vs_ratio_in_eta_0_5->SetRightMargin(0.05);
   pT_vs_ratio_in_eta_0_5->SetTopMargin(0.05);
   pT_vs_ratio_in_eta_0_5->SetBottomMargin(0.13);
   pT_vs_ratio_in_eta_0_5->SetFrameFillStyle(0);
   pT_vs_ratio_in_eta_0_5->SetFrameBorderMode(0);
   pT_vs_ratio_in_eta_0_5->SetFrameFillStyle(0);
   pT_vs_ratio_in_eta_0_5->SetFrameBorderMode(0);
   
   TGraphErrors *gre = new TGraphErrors(13);
   gre->SetName("Graph");
   gre->SetTitle("pT_vs_ratio_in_eta_0_5");
   gre->SetFillColor(1);
   gre->SetMarkerColor(4);
   gre->SetMarkerStyle(21);
   gre->SetPoint(0,100,1.014795);
   gre->SetPointError(0,100,0.0003825243);
   gre->SetPoint(1,300,1.014167);
   gre->SetPointError(1,100,0.000291476);
   gre->SetPoint(2,500,2.121963e-314);
   gre->SetPointError(2,100,5.33044e+228);
   gre->SetPoint(3,700,3.330014e-309);
   gre->SetPointError(3,100,4.771918e-10);
   gre->SetPoint(4,900,2.17808e-314);
   gre->SetPointError(4,100,3.105036e+231);
   gre->SetPoint(5,1100,6.929427e-310);
   gre->SetPointError(5,100,3.105036e+231);
   gre->SetPoint(6,1300,6.929427e-310);
   gre->SetPointError(6,100,2.121963e-314);
   gre->SetPoint(7,1650,6.929427e-310);
   gre->SetPointError(7,250,2.854972e+242);
   gre->SetPoint(8,2150,2.17808e-314);
   gre->SetPointError(8,250,9.569456e-315);
   gre->SetPoint(9,2650,6.929427e-310);
   gre->SetPointError(9,250,6.929427e-310);
   gre->SetPoint(10,3150,6.929427e-310);
   gre->SetPointError(10,250,3.105036e+231);
   gre->SetPoint(11,3650,6.929427e-310);
   gre->SetPointError(11,250,3.11108e+231);
   gre->SetPoint(12,4150,2.17808e-314);
   gre->SetPointError(12,250,3.105039e+231);
   
   TH1F *Graph_Graph1 = new TH1F("Graph_Graph1","pT_vs_ratio_in_eta_0_5",100,0,4840);
   Graph_Graph1->SetMinimum(0.9);
   Graph_Graph1->SetMaximum(1.1);
   Graph_Graph1->SetDirectory(0);
   Graph_Graph1->SetStats(0);
   Graph_Graph1->SetLineStyle(0);
   Graph_Graph1->SetMarkerStyle(20);
   Graph_Graph1->GetXaxis()->SetTitle("pT [GeV]");
   Graph_Graph1->GetXaxis()->SetLabelFont(42);
   Graph_Graph1->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1->GetXaxis()->SetTitleFont(42);
   Graph_Graph1->GetYaxis()->SetTitle("p_{T}^{HLT}/p_{T}^{RECO}");
   Graph_Graph1->GetYaxis()->SetLabelFont(42);
   Graph_Graph1->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph1->GetYaxis()->SetTitleFont(42);
   Graph_Graph1->GetZaxis()->SetLabelFont(42);
   Graph_Graph1->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph1->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1);
   
   gre->Draw("ap");
   
   TPaveText *pt = new TPaveText(0,0.9522378,0.3572483,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("pT_vs_ratio_in_eta_0_5");
   pt->Draw();
   pT_vs_ratio_in_eta_0_5->Modified();
   pT_vs_ratio_in_eta_0_5->cd();
   pT_vs_ratio_in_eta_0_5->SetSelected(pT_vs_ratio_in_eta_0_5);
}
