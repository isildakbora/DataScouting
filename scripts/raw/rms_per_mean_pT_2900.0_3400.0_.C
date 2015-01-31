{
//=========Macro generated from canvas: rms_pT_2900_/rms_pT_2900_
//=========  (Tue Jan  6 15:46:32 2015) by ROOT version5.34/05
   TCanvas *rms_pT_2900_ = new TCanvas("rms_pT_2900_", "rms_pT_2900_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_2900_->SetHighLightColor(2);
   rms_pT_2900_->Range(-0.4360759,-0.1743902,2.601899,1.167073);
   rms_pT_2900_->SetFillColor(0);
   rms_pT_2900_->SetBorderMode(0);
   rms_pT_2900_->SetBorderSize(2);
   rms_pT_2900_->SetTickx(1);
   rms_pT_2900_->SetTicky(1);
   rms_pT_2900_->SetLeftMargin(0.16);
   rms_pT_2900_->SetRightMargin(0.05);
   rms_pT_2900_->SetTopMargin(0.05);
   rms_pT_2900_->SetBottomMargin(0.13);
   rms_pT_2900_->SetFrameFillStyle(0);
   rms_pT_2900_->SetFrameBorderMode(0);
   rms_pT_2900_->SetFrameFillStyle(0);
   rms_pT_2900_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_2900.0_3400.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0);
   graph->SetPoint(1,0.75,0);
   graph->SetPoint(2,1.25,0);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph31 = new TH1F("Graph_Graph31","rms_per_mean_eta_vs_ratio_in_pT_2900.0_3400.0",100,0.05,2.45);
   Graph_Graph31->SetMinimum(0);
   Graph_Graph31->SetMaximum(1.1);
   Graph_Graph31->SetDirectory(0);
   Graph_Graph31->SetStats(0);
   Graph_Graph31->SetLineStyle(0);
   Graph_Graph31->SetMarkerStyle(20);
   Graph_Graph31->GetXaxis()->SetTitle("eta");
   Graph_Graph31->GetXaxis()->SetLabelFont(42);
   Graph_Graph31->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph31->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph31->GetXaxis()->SetTitleFont(42);
   Graph_Graph31->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph31->GetYaxis()->SetLabelFont(42);
   Graph_Graph31->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph31->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph31->GetYaxis()->SetTitleFont(42);
   Graph_Graph31->GetZaxis()->SetLabelFont(42);
   Graph_Graph31->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph31->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph31->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph31);
   
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
   
   TH1F *Graph_Graph32 = new TH1F("Graph_Graph32","Graph",100,0.05,2.45);
   Graph_Graph32->SetMinimum(0);
   Graph_Graph32->SetMaximum(1.1);
   Graph_Graph32->SetDirectory(0);
   Graph_Graph32->SetStats(0);
   Graph_Graph32->SetLineStyle(0);
   Graph_Graph32->SetMarkerStyle(20);
   Graph_Graph32->GetXaxis()->SetTitle("eta");
   Graph_Graph32->GetXaxis()->SetLabelFont(42);
   Graph_Graph32->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph32->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph32->GetXaxis()->SetTitleFont(42);
   Graph_Graph32->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph32->GetYaxis()->SetLabelFont(42);
   Graph_Graph32->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph32->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph32->GetYaxis()->SetTitleFont(42);
   Graph_Graph32->GetZaxis()->SetLabelFont(42);
   Graph_Graph32->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph32->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph32->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph32);
   
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
   
   TH1F *Graph_Graph33 = new TH1F("Graph_Graph33","Graph",100,0.05,2.45);
   Graph_Graph33->SetMinimum(0);
   Graph_Graph33->SetMaximum(1.1);
   Graph_Graph33->SetDirectory(0);
   Graph_Graph33->SetStats(0);
   Graph_Graph33->SetLineStyle(0);
   Graph_Graph33->SetMarkerStyle(20);
   Graph_Graph33->GetXaxis()->SetTitle("eta");
   Graph_Graph33->GetXaxis()->SetLabelFont(42);
   Graph_Graph33->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph33->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph33->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph33->GetXaxis()->SetTitleFont(42);
   Graph_Graph33->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph33->GetYaxis()->SetLabelFont(42);
   Graph_Graph33->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph33->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph33->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph33->GetYaxis()->SetTitleFont(42);
   Graph_Graph33->GetZaxis()->SetLabelFont(42);
   Graph_Graph33->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph33->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph33->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph33);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3404698,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_2900.0_3400.0");
   pt->Draw();
   rms_pT_2900_->Modified();
   rms_pT_2900_->cd();
   rms_pT_2900_->SetSelected(rms_pT_2900_);
}
