{
//=========Macro generated from canvas: rms_pT_1900_/rms_pT_1900_
//=========  (Tue Jan  6 15:46:30 2015) by ROOT version5.34/05
   TCanvas *rms_pT_1900_ = new TCanvas("rms_pT_1900_", "rms_pT_1900_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_1900_->SetHighLightColor(2);
   rms_pT_1900_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_1900_->SetFillColor(0);
   rms_pT_1900_->SetBorderMode(0);
   rms_pT_1900_->SetBorderSize(2);
   rms_pT_1900_->SetTickx(1);
   rms_pT_1900_->SetTicky(1);
   rms_pT_1900_->SetLeftMargin(0.16);
   rms_pT_1900_->SetRightMargin(0.05);
   rms_pT_1900_->SetTopMargin(0.05);
   rms_pT_1900_->SetBottomMargin(0.13);
   rms_pT_1900_->SetFrameFillStyle(0);
   rms_pT_1900_->SetFrameBorderMode(0);
   rms_pT_1900_->SetFrameFillStyle(0);
   rms_pT_1900_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_1900.0_2400.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph25 = new TH1F("Graph_Graph25","rms_per_mean_eta_vs_ratio_in_pT_1900.0_2400.0",100,0.05,2.45);
   Graph_Graph25->SetMinimum(0);
   Graph_Graph25->SetMaximum(1.1);
   Graph_Graph25->SetDirectory(0);
   Graph_Graph25->SetStats(0);
   Graph_Graph25->SetLineStyle(0);
   Graph_Graph25->SetMarkerStyle(20);
   Graph_Graph25->GetXaxis()->SetTitle("eta");
   Graph_Graph25->GetXaxis()->SetLabelFont(42);
   Graph_Graph25->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph25->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph25->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph25->GetXaxis()->SetTitleFont(42);
   Graph_Graph25->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph25->GetYaxis()->SetLabelFont(42);
   Graph_Graph25->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph25->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph25->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph25->GetYaxis()->SetTitleFont(42);
   Graph_Graph25->GetZaxis()->SetLabelFont(42);
   Graph_Graph25->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph25->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph25->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph25);
   
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
   
   TH1F *Graph_Graph26 = new TH1F("Graph_Graph26","Graph",100,0.05,2.45);
   Graph_Graph26->SetMinimum(0);
   Graph_Graph26->SetMaximum(1.1);
   Graph_Graph26->SetDirectory(0);
   Graph_Graph26->SetStats(0);
   Graph_Graph26->SetLineStyle(0);
   Graph_Graph26->SetMarkerStyle(20);
   Graph_Graph26->GetXaxis()->SetTitle("eta");
   Graph_Graph26->GetXaxis()->SetLabelFont(42);
   Graph_Graph26->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph26->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph26->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph26->GetXaxis()->SetTitleFont(42);
   Graph_Graph26->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph26->GetYaxis()->SetLabelFont(42);
   Graph_Graph26->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph26->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph26->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph26->GetYaxis()->SetTitleFont(42);
   Graph_Graph26->GetZaxis()->SetLabelFont(42);
   Graph_Graph26->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph26->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph26->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph26);
   
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
   
   TH1F *Graph_Graph27 = new TH1F("Graph_Graph27","Graph",100,0.05,2.45);
   Graph_Graph27->SetMinimum(0);
   Graph_Graph27->SetMaximum(1.1);
   Graph_Graph27->SetDirectory(0);
   Graph_Graph27->SetStats(0);
   Graph_Graph27->SetLineStyle(0);
   Graph_Graph27->SetMarkerStyle(20);
   Graph_Graph27->GetXaxis()->SetTitle("eta");
   Graph_Graph27->GetXaxis()->SetLabelFont(42);
   Graph_Graph27->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph27->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph27->GetXaxis()->SetTitleFont(42);
   Graph_Graph27->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph27->GetYaxis()->SetLabelFont(42);
   Graph_Graph27->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph27->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph27->GetYaxis()->SetTitleFont(42);
   Graph_Graph27->GetZaxis()->SetLabelFont(42);
   Graph_Graph27->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph27->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph27->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph27);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_1900.0_2400.0");
   pt->Draw();
   rms_pT_1900_->Modified();
   rms_pT_1900_->cd();
   rms_pT_1900_->SetSelected(rms_pT_1900_);
}
