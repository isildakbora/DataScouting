{
//=========Macro generated from canvas: rms_pT_1000_/rms_pT_1000_
//=========  (Tue Jan  6 15:46:28 2015) by ROOT version5.34/05
   TCanvas *rms_pT_1000_ = new TCanvas("rms_pT_1000_", "rms_pT_1000_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_1000_->SetHighLightColor(2);
   rms_pT_1000_->Range(-0.4360759,-0.004152024,2.601899,0.02778662);
   rms_pT_1000_->SetFillColor(0);
   rms_pT_1000_->SetBorderMode(0);
   rms_pT_1000_->SetBorderSize(2);
   rms_pT_1000_->SetTickx(1);
   rms_pT_1000_->SetTicky(1);
   rms_pT_1000_->SetLeftMargin(0.16);
   rms_pT_1000_->SetRightMargin(0.05);
   rms_pT_1000_->SetTopMargin(0.05);
   rms_pT_1000_->SetBottomMargin(0.13);
   rms_pT_1000_->SetFrameFillStyle(0);
   rms_pT_1000_->SetFrameBorderMode(0);
   rms_pT_1000_->SetFrameFillStyle(0);
   rms_pT_1000_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_1000.0_1200.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.02380880841);
   graph->SetPoint(1,0.75,0.012);
   graph->SetPoint(2,1.25,0.0125);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph16 = new TH1F("Graph_Graph16","rms_per_mean_eta_vs_ratio_in_pT_1000.0_1200.0",100,0.05,2.45);
   Graph_Graph16->SetMinimum(0);
   Graph_Graph16->SetMaximum(0.02618969);
   Graph_Graph16->SetDirectory(0);
   Graph_Graph16->SetStats(0);
   Graph_Graph16->SetLineStyle(0);
   Graph_Graph16->SetMarkerStyle(20);
   Graph_Graph16->GetXaxis()->SetTitle("eta");
   Graph_Graph16->GetXaxis()->SetLabelFont(42);
   Graph_Graph16->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph16->GetXaxis()->SetTitleFont(42);
   Graph_Graph16->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph16->GetYaxis()->SetLabelFont(42);
   Graph_Graph16->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph16->GetYaxis()->SetTitleFont(42);
   Graph_Graph16->GetZaxis()->SetLabelFont(42);
   Graph_Graph16->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph16->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph16->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph16);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.02266503722);
   graph->SetPoint(1,0.75,0.02094292322);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph17 = new TH1F("Graph_Graph17","Graph",100,0.05,2.45);
   Graph_Graph17->SetMinimum(0);
   Graph_Graph17->SetMaximum(0.02493154);
   Graph_Graph17->SetDirectory(0);
   Graph_Graph17->SetStats(0);
   Graph_Graph17->SetLineStyle(0);
   Graph_Graph17->SetMarkerStyle(20);
   Graph_Graph17->GetXaxis()->SetTitle("eta");
   Graph_Graph17->GetXaxis()->SetLabelFont(42);
   Graph_Graph17->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph17->GetXaxis()->SetTitleFont(42);
   Graph_Graph17->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph17->GetYaxis()->SetLabelFont(42);
   Graph_Graph17->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph17->GetYaxis()->SetTitleFont(42);
   Graph_Graph17->GetZaxis()->SetLabelFont(42);
   Graph_Graph17->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph17->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph17->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph17);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01598275113);
   graph->SetPoint(1,0.75,0.03238866397);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph18 = new TH1F("Graph_Graph18","Graph",100,0.05,2.45);
   Graph_Graph18->SetMinimum(0);
   Graph_Graph18->SetMaximum(0.03562753);
   Graph_Graph18->SetDirectory(0);
   Graph_Graph18->SetStats(0);
   Graph_Graph18->SetLineStyle(0);
   Graph_Graph18->SetMarkerStyle(20);
   Graph_Graph18->GetXaxis()->SetTitle("eta");
   Graph_Graph18->GetXaxis()->SetLabelFont(42);
   Graph_Graph18->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph18->GetXaxis()->SetTitleFont(42);
   Graph_Graph18->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph18->GetYaxis()->SetLabelFont(42);
   Graph_Graph18->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph18->GetYaxis()->SetTitleFont(42);
   Graph_Graph18->GetZaxis()->SetLabelFont(42);
   Graph_Graph18->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph18->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph18->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph18);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_1000.0_1200.0");
   pt->Draw();
   rms_pT_1000_->Modified();
   rms_pT_1000_->cd();
   rms_pT_1000_->SetSelected(rms_pT_1000_);
}
