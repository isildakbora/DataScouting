{
//=========Macro generated from canvas: rms_pT_1200_/rms_pT_1200_
//=========  (Tue Jan  6 15:46:29 2015) by ROOT version5.34/05
   TCanvas *rms_pT_1200_ = new TCanvas("rms_pT_1200_", "rms_pT_1200_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_1200_->SetHighLightColor(2);
   rms_pT_1200_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_1200_->SetFillColor(0);
   rms_pT_1200_->SetBorderMode(0);
   rms_pT_1200_->SetBorderSize(2);
   rms_pT_1200_->SetTickx(1);
   rms_pT_1200_->SetTicky(1);
   rms_pT_1200_->SetLeftMargin(0.16);
   rms_pT_1200_->SetRightMargin(0.05);
   rms_pT_1200_->SetTopMargin(0.05);
   rms_pT_1200_->SetBottomMargin(0.13);
   rms_pT_1200_->SetFrameFillStyle(0);
   rms_pT_1200_->SetFrameBorderMode(0);
   rms_pT_1200_->SetFrameFillStyle(0);
   rms_pT_1200_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_1200.0_1400.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph19 = new TH1F("Graph_Graph19","rms_per_mean_eta_vs_ratio_in_pT_1200.0_1400.0",100,0.05,2.45);
   Graph_Graph19->SetMinimum(0);
   Graph_Graph19->SetMaximum(1.1);
   Graph_Graph19->SetDirectory(0);
   Graph_Graph19->SetStats(0);
   Graph_Graph19->SetLineStyle(0);
   Graph_Graph19->SetMarkerStyle(20);
   Graph_Graph19->GetXaxis()->SetTitle("eta");
   Graph_Graph19->GetXaxis()->SetLabelFont(42);
   Graph_Graph19->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph19->GetXaxis()->SetTitleFont(42);
   Graph_Graph19->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph19->GetYaxis()->SetLabelFont(42);
   Graph_Graph19->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph19->GetYaxis()->SetTitleFont(42);
   Graph_Graph19->GetZaxis()->SetLabelFont(42);
   Graph_Graph19->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph19->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph19->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph19);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01076611194);
   graph->SetPoint(1,0.75,0.04098824425);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph20 = new TH1F("Graph_Graph20","Graph",100,0.05,2.45);
   Graph_Graph20->SetMinimum(0);
   Graph_Graph20->SetMaximum(0.04508707);
   Graph_Graph20->SetDirectory(0);
   Graph_Graph20->SetStats(0);
   Graph_Graph20->SetLineStyle(0);
   Graph_Graph20->SetMarkerStyle(20);
   Graph_Graph20->GetXaxis()->SetTitle("eta");
   Graph_Graph20->GetXaxis()->SetLabelFont(42);
   Graph_Graph20->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph20->GetXaxis()->SetTitleFont(42);
   Graph_Graph20->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph20->GetYaxis()->SetLabelFont(42);
   Graph_Graph20->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph20->GetYaxis()->SetTitleFont(42);
   Graph_Graph20->GetZaxis()->SetLabelFont(42);
   Graph_Graph20->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph20->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph20->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph20);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01379978217);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph21 = new TH1F("Graph_Graph21","Graph",100,0.05,2.45);
   Graph_Graph21->SetMinimum(0);
   Graph_Graph21->SetMaximum(0.01517976);
   Graph_Graph21->SetDirectory(0);
   Graph_Graph21->SetStats(0);
   Graph_Graph21->SetLineStyle(0);
   Graph_Graph21->SetMarkerStyle(20);
   Graph_Graph21->GetXaxis()->SetTitle("eta");
   Graph_Graph21->GetXaxis()->SetLabelFont(42);
   Graph_Graph21->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph21->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph21->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph21->GetXaxis()->SetTitleFont(42);
   Graph_Graph21->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph21->GetYaxis()->SetLabelFont(42);
   Graph_Graph21->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph21->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph21->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph21->GetYaxis()->SetTitleFont(42);
   Graph_Graph21->GetZaxis()->SetLabelFont(42);
   Graph_Graph21->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph21->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph21->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph21);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_1200.0_1400.0");
   pt->Draw();
   rms_pT_1200_->Modified();
   rms_pT_1200_->cd();
   rms_pT_1200_->SetSelected(rms_pT_1200_);
}
