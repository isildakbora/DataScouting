{
//=========Macro generated from canvas: rms_pT_2400_/rms_pT_2400_
//=========  (Tue Jan  6 15:46:31 2015) by ROOT version5.34/05
   TCanvas *rms_pT_2400_ = new TCanvas("rms_pT_2400_", "rms_pT_2400_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_2400_->SetHighLightColor(2);
   rms_pT_2400_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_2400_->SetFillColor(0);
   rms_pT_2400_->SetBorderMode(0);
   rms_pT_2400_->SetBorderSize(2);
   rms_pT_2400_->SetTickx(1);
   rms_pT_2400_->SetTicky(1);
   rms_pT_2400_->SetLeftMargin(0.16);
   rms_pT_2400_->SetRightMargin(0.05);
   rms_pT_2400_->SetTopMargin(0.05);
   rms_pT_2400_->SetBottomMargin(0.13);
   rms_pT_2400_->SetFrameFillStyle(0);
   rms_pT_2400_->SetFrameBorderMode(0);
   rms_pT_2400_->SetFrameFillStyle(0);
   rms_pT_2400_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_2400.0_2900.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph28 = new TH1F("Graph_Graph28","rms_per_mean_eta_vs_ratio_in_pT_2400.0_2900.0",100,0.05,2.45);
   Graph_Graph28->SetMinimum(0);
   Graph_Graph28->SetMaximum(1.1);
   Graph_Graph28->SetDirectory(0);
   Graph_Graph28->SetStats(0);
   Graph_Graph28->SetLineStyle(0);
   Graph_Graph28->SetMarkerStyle(20);
   Graph_Graph28->GetXaxis()->SetTitle("eta");
   Graph_Graph28->GetXaxis()->SetLabelFont(42);
   Graph_Graph28->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph28->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph28->GetXaxis()->SetTitleFont(42);
   Graph_Graph28->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph28->GetYaxis()->SetLabelFont(42);
   Graph_Graph28->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph28->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph28->GetYaxis()->SetTitleFont(42);
   Graph_Graph28->GetZaxis()->SetLabelFont(42);
   Graph_Graph28->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph28->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph28->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph28);
   
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
   
   TH1F *Graph_Graph29 = new TH1F("Graph_Graph29","Graph",100,0.05,2.45);
   Graph_Graph29->SetMinimum(0);
   Graph_Graph29->SetMaximum(1.1);
   Graph_Graph29->SetDirectory(0);
   Graph_Graph29->SetStats(0);
   Graph_Graph29->SetLineStyle(0);
   Graph_Graph29->SetMarkerStyle(20);
   Graph_Graph29->GetXaxis()->SetTitle("eta");
   Graph_Graph29->GetXaxis()->SetLabelFont(42);
   Graph_Graph29->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph29->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph29->GetXaxis()->SetTitleFont(42);
   Graph_Graph29->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph29->GetYaxis()->SetLabelFont(42);
   Graph_Graph29->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph29->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph29->GetYaxis()->SetTitleFont(42);
   Graph_Graph29->GetZaxis()->SetLabelFont(42);
   Graph_Graph29->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph29->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph29->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph29);
   
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
   
   TH1F *Graph_Graph30 = new TH1F("Graph_Graph30","Graph",100,0.05,2.45);
   Graph_Graph30->SetMinimum(0);
   Graph_Graph30->SetMaximum(1.1);
   Graph_Graph30->SetDirectory(0);
   Graph_Graph30->SetStats(0);
   Graph_Graph30->SetLineStyle(0);
   Graph_Graph30->SetMarkerStyle(20);
   Graph_Graph30->GetXaxis()->SetTitle("eta");
   Graph_Graph30->GetXaxis()->SetLabelFont(42);
   Graph_Graph30->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph30->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph30->GetXaxis()->SetTitleFont(42);
   Graph_Graph30->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph30->GetYaxis()->SetLabelFont(42);
   Graph_Graph30->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph30->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph30->GetYaxis()->SetTitleFont(42);
   Graph_Graph30->GetZaxis()->SetLabelFont(42);
   Graph_Graph30->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph30->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph30->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph30);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_2400.0_2900.0");
   pt->Draw();
   rms_pT_2400_->Modified();
   rms_pT_2400_->cd();
   rms_pT_2400_->SetSelected(rms_pT_2400_);
}
