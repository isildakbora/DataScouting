{
//=========Macro generated from canvas: rms_pT_3400_/rms_pT_3400_
//=========  (Tue Jan  6 15:46:33 2015) by ROOT version5.34/05
   TCanvas *rms_pT_3400_ = new TCanvas("rms_pT_3400_", "rms_pT_3400_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_3400_->SetHighLightColor(2);
   rms_pT_3400_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_3400_->SetFillColor(0);
   rms_pT_3400_->SetBorderMode(0);
   rms_pT_3400_->SetBorderSize(2);
   rms_pT_3400_->SetTickx(1);
   rms_pT_3400_->SetTicky(1);
   rms_pT_3400_->SetLeftMargin(0.16);
   rms_pT_3400_->SetRightMargin(0.05);
   rms_pT_3400_->SetTopMargin(0.05);
   rms_pT_3400_->SetBottomMargin(0.13);
   rms_pT_3400_->SetFrameFillStyle(0);
   rms_pT_3400_->SetFrameBorderMode(0);
   rms_pT_3400_->SetFrameFillStyle(0);
   rms_pT_3400_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_3400.0_3900.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph34 = new TH1F("Graph_Graph34","rms_per_mean_eta_vs_ratio_in_pT_3400.0_3900.0",100,0.05,2.45);
   Graph_Graph34->SetMinimum(0);
   Graph_Graph34->SetMaximum(1.1);
   Graph_Graph34->SetDirectory(0);
   Graph_Graph34->SetStats(0);
   Graph_Graph34->SetLineStyle(0);
   Graph_Graph34->SetMarkerStyle(20);
   Graph_Graph34->GetXaxis()->SetTitle("eta");
   Graph_Graph34->GetXaxis()->SetLabelFont(42);
   Graph_Graph34->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph34->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph34->GetXaxis()->SetTitleFont(42);
   Graph_Graph34->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph34->GetYaxis()->SetLabelFont(42);
   Graph_Graph34->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph34->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph34->GetYaxis()->SetTitleFont(42);
   Graph_Graph34->GetZaxis()->SetLabelFont(42);
   Graph_Graph34->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph34->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph34->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph34);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph35 = new TH1F("Graph_Graph35","Graph",100,0.05,2.45);
   Graph_Graph35->SetMinimum(0);
   Graph_Graph35->SetMaximum(1.1);
   Graph_Graph35->SetDirectory(0);
   Graph_Graph35->SetStats(0);
   Graph_Graph35->SetLineStyle(0);
   Graph_Graph35->SetMarkerStyle(20);
   Graph_Graph35->GetXaxis()->SetTitle("eta");
   Graph_Graph35->GetXaxis()->SetLabelFont(42);
   Graph_Graph35->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph35->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph35->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph35->GetXaxis()->SetTitleFont(42);
   Graph_Graph35->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph35->GetYaxis()->SetLabelFont(42);
   Graph_Graph35->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph35->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph35->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph35->GetYaxis()->SetTitleFont(42);
   Graph_Graph35->GetZaxis()->SetLabelFont(42);
   Graph_Graph35->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph35->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph35->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph35);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph36 = new TH1F("Graph_Graph36","Graph",100,0.05,2.45);
   Graph_Graph36->SetMinimum(0);
   Graph_Graph36->SetMaximum(1.1);
   Graph_Graph36->SetDirectory(0);
   Graph_Graph36->SetStats(0);
   Graph_Graph36->SetLineStyle(0);
   Graph_Graph36->SetMarkerStyle(20);
   Graph_Graph36->GetXaxis()->SetTitle("eta");
   Graph_Graph36->GetXaxis()->SetLabelFont(42);
   Graph_Graph36->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph36->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph36->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph36->GetXaxis()->SetTitleFont(42);
   Graph_Graph36->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph36->GetYaxis()->SetLabelFont(42);
   Graph_Graph36->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph36->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph36->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph36->GetYaxis()->SetTitleFont(42);
   Graph_Graph36->GetZaxis()->SetLabelFont(42);
   Graph_Graph36->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph36->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph36->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph36);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_3400.0_3900.0");
   pt->Draw();
   rms_pT_3400_->Modified();
   rms_pT_3400_->cd();
   rms_pT_3400_->SetSelected(rms_pT_3400_);
}
