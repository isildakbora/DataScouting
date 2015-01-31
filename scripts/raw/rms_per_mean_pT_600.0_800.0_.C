{
//=========Macro generated from canvas: rms_pT_600_/rms_pT_600_
//=========  (Tue Jan  6 15:46:27 2015) by ROOT version5.34/05
   TCanvas *rms_pT_600_ = new TCanvas("rms_pT_600_", "rms_pT_600_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_600_->SetHighLightColor(2);
   rms_pT_600_->Range(-0.4360759,-0.004603554,2.601899,0.0308084);
   rms_pT_600_->SetFillColor(0);
   rms_pT_600_->SetBorderMode(0);
   rms_pT_600_->SetBorderSize(2);
   rms_pT_600_->SetTickx(1);
   rms_pT_600_->SetTicky(1);
   rms_pT_600_->SetLeftMargin(0.16);
   rms_pT_600_->SetRightMargin(0.05);
   rms_pT_600_->SetTopMargin(0.05);
   rms_pT_600_->SetBottomMargin(0.13);
   rms_pT_600_->SetFrameFillStyle(0);
   rms_pT_600_->SetFrameBorderMode(0);
   rms_pT_600_->SetFrameFillStyle(0);
   rms_pT_600_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_600.0_800.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01900821628);
   graph->SetPoint(1,0.75,0.02249484489);
   graph->SetPoint(2,1.25,0.02639800445);
   graph->SetPoint(3,1.75,0.01883236074);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph10 = new TH1F("Graph_Graph10","rms_per_mean_eta_vs_ratio_in_pT_600.0_800.0",100,0.05,2.45);
   Graph_Graph10->SetMinimum(0);
   Graph_Graph10->SetMaximum(0.0290378);
   Graph_Graph10->SetDirectory(0);
   Graph_Graph10->SetStats(0);
   Graph_Graph10->SetLineStyle(0);
   Graph_Graph10->SetMarkerStyle(20);
   Graph_Graph10->GetXaxis()->SetTitle("eta");
   Graph_Graph10->GetXaxis()->SetLabelFont(42);
   Graph_Graph10->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph10->GetXaxis()->SetTitleFont(42);
   Graph_Graph10->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph10->GetYaxis()->SetLabelFont(42);
   Graph_Graph10->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph10->GetYaxis()->SetTitleFont(42);
   Graph_Graph10->GetZaxis()->SetLabelFont(42);
   Graph_Graph10->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph10->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph10->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph10);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.0203952078);
   graph->SetPoint(1,0.75,0.02302675068);
   graph->SetPoint(2,1.25,0.02465549476);
   graph->SetPoint(3,1.75,0.02066329037);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph11 = new TH1F("Graph_Graph11","Graph",100,0.05,2.45);
   Graph_Graph11->SetMinimum(0);
   Graph_Graph11->SetMaximum(0.02712104);
   Graph_Graph11->SetDirectory(0);
   Graph_Graph11->SetStats(0);
   Graph_Graph11->SetLineStyle(0);
   Graph_Graph11->SetMarkerStyle(20);
   Graph_Graph11->GetXaxis()->SetTitle("eta");
   Graph_Graph11->GetXaxis()->SetLabelFont(42);
   Graph_Graph11->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph11->GetXaxis()->SetTitleFont(42);
   Graph_Graph11->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph11->GetYaxis()->SetLabelFont(42);
   Graph_Graph11->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph11->GetYaxis()->SetTitleFont(42);
   Graph_Graph11->GetZaxis()->SetLabelFont(42);
   Graph_Graph11->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph11->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph11->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph11);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01832437116);
   graph->SetPoint(1,0.75,0.02269230064);
   graph->SetPoint(2,1.25,0.02352234512);
   graph->SetPoint(3,1.75,0.01486486486);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","Graph",100,0.05,2.45);
   Graph_Graph12->SetMinimum(0);
   Graph_Graph12->SetMaximum(0.02587458);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);
   Graph_Graph12->SetLineStyle(0);
   Graph_Graph12->SetMarkerStyle(20);
   Graph_Graph12->GetXaxis()->SetTitle("eta");
   Graph_Graph12->GetXaxis()->SetLabelFont(42);
   Graph_Graph12->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph12->GetXaxis()->SetTitleFont(42);
   Graph_Graph12->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph12->GetYaxis()->SetLabelFont(42);
   Graph_Graph12->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph12->GetYaxis()->SetTitleFont(42);
   Graph_Graph12->GetZaxis()->SetLabelFont(42);
   Graph_Graph12->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph12->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph12->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph12);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3253691,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_600.0_800.0");
   pt->Draw();
   rms_pT_600_->Modified();
   rms_pT_600_->cd();
   rms_pT_600_->SetSelected(rms_pT_600_);
}
