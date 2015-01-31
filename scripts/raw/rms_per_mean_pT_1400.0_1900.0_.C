{
//=========Macro generated from canvas: rms_pT_1400_/rms_pT_1400_
//=========  (Tue Jan  6 15:46:30 2015) by ROOT version5.34/05
   TCanvas *rms_pT_1400_ = new TCanvas("rms_pT_1400_", "rms_pT_1400_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_1400_->SetHighLightColor(2);
   rms_pT_1400_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_1400_->SetFillColor(0);
   rms_pT_1400_->SetBorderMode(0);
   rms_pT_1400_->SetBorderSize(2);
   rms_pT_1400_->SetTickx(1);
   rms_pT_1400_->SetTicky(1);
   rms_pT_1400_->SetLeftMargin(0.16);
   rms_pT_1400_->SetRightMargin(0.05);
   rms_pT_1400_->SetTopMargin(0.05);
   rms_pT_1400_->SetBottomMargin(0.13);
   rms_pT_1400_->SetFrameFillStyle(0);
   rms_pT_1400_->SetFrameBorderMode(0);
   rms_pT_1400_->SetFrameFillStyle(0);
   rms_pT_1400_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_1400.0_1900.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph22 = new TH1F("Graph_Graph22","rms_per_mean_eta_vs_ratio_in_pT_1400.0_1900.0",100,0.05,2.45);
   Graph_Graph22->SetMinimum(0);
   Graph_Graph22->SetMaximum(1.1);
   Graph_Graph22->SetDirectory(0);
   Graph_Graph22->SetStats(0);
   Graph_Graph22->SetLineStyle(0);
   Graph_Graph22->SetMarkerStyle(20);
   Graph_Graph22->GetXaxis()->SetTitle("eta");
   Graph_Graph22->GetXaxis()->SetLabelFont(42);
   Graph_Graph22->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph22->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph22->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph22->GetXaxis()->SetTitleFont(42);
   Graph_Graph22->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph22->GetYaxis()->SetLabelFont(42);
   Graph_Graph22->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph22->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph22->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph22->GetYaxis()->SetTitleFont(42);
   Graph_Graph22->GetZaxis()->SetLabelFont(42);
   Graph_Graph22->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph22->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph22->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph22);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01763466857);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph23 = new TH1F("Graph_Graph23","Graph",100,0.05,2.45);
   Graph_Graph23->SetMinimum(0);
   Graph_Graph23->SetMaximum(0.01939814);
   Graph_Graph23->SetDirectory(0);
   Graph_Graph23->SetStats(0);
   Graph_Graph23->SetLineStyle(0);
   Graph_Graph23->SetMarkerStyle(20);
   Graph_Graph23->GetXaxis()->SetTitle("eta");
   Graph_Graph23->GetXaxis()->SetLabelFont(42);
   Graph_Graph23->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph23->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph23->GetXaxis()->SetTitleFont(42);
   Graph_Graph23->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph23->GetYaxis()->SetLabelFont(42);
   Graph_Graph23->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph23->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph23->GetYaxis()->SetTitleFont(42);
   Graph_Graph23->GetZaxis()->SetLabelFont(42);
   Graph_Graph23->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph23->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph23->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph23);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.003901278793);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph24 = new TH1F("Graph_Graph24","Graph",100,0.05,2.45);
   Graph_Graph24->SetMinimum(0);
   Graph_Graph24->SetMaximum(0.004291407);
   Graph_Graph24->SetDirectory(0);
   Graph_Graph24->SetStats(0);
   Graph_Graph24->SetLineStyle(0);
   Graph_Graph24->SetMarkerStyle(20);
   Graph_Graph24->GetXaxis()->SetTitle("eta");
   Graph_Graph24->GetXaxis()->SetLabelFont(42);
   Graph_Graph24->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph24->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph24->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph24->GetXaxis()->SetTitleFont(42);
   Graph_Graph24->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph24->GetYaxis()->SetLabelFont(42);
   Graph_Graph24->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph24->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph24->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph24->GetYaxis()->SetTitleFont(42);
   Graph_Graph24->GetZaxis()->SetLabelFont(42);
   Graph_Graph24->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph24->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph24->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph24);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_1400.0_1900.0");
   pt->Draw();
   rms_pT_1400_->Modified();
   rms_pT_1400_->cd();
   rms_pT_1400_->SetSelected(rms_pT_1400_);
}
