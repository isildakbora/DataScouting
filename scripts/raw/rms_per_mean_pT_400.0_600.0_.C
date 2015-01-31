{
//=========Macro generated from canvas: rms_pT_400_/rms_pT_400_
//=========  (Tue Jan  6 15:46:27 2015) by ROOT version5.34/05
   TCanvas *rms_pT_400_ = new TCanvas("rms_pT_400_", "rms_pT_400_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_400_->SetHighLightColor(2);
   rms_pT_400_->Range(-0.4360759,0.015018,2.601899,0.04078913);
   rms_pT_400_->SetFillColor(0);
   rms_pT_400_->SetBorderMode(0);
   rms_pT_400_->SetBorderSize(2);
   rms_pT_400_->SetTickx(1);
   rms_pT_400_->SetTicky(1);
   rms_pT_400_->SetLeftMargin(0.16);
   rms_pT_400_->SetRightMargin(0.05);
   rms_pT_400_->SetTopMargin(0.05);
   rms_pT_400_->SetBottomMargin(0.13);
   rms_pT_400_->SetFrameFillStyle(0);
   rms_pT_400_->SetFrameBorderMode(0);
   rms_pT_400_->SetFrameFillStyle(0);
   rms_pT_400_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_400.0_600.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.020129272);
   graph->SetPoint(1,0.75,0.0234486043);
   graph->SetPoint(2,1.25,0.02399400032);
   graph->SetPoint(3,1.75,0.02138643725);
   graph->SetPoint(4,2.25,0.03773954392);
   
   TH1F *Graph_Graph7 = new TH1F("Graph_Graph7","rms_per_mean_eta_vs_ratio_in_pT_400.0_600.0",100,0.05,2.45);
   Graph_Graph7->SetMinimum(0.01836824);
   Graph_Graph7->SetMaximum(0.03950057);
   Graph_Graph7->SetDirectory(0);
   Graph_Graph7->SetStats(0);
   Graph_Graph7->SetLineStyle(0);
   Graph_Graph7->SetMarkerStyle(20);
   Graph_Graph7->GetXaxis()->SetTitle("eta");
   Graph_Graph7->GetXaxis()->SetLabelFont(42);
   Graph_Graph7->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph7->GetXaxis()->SetTitleFont(42);
   Graph_Graph7->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph7->GetYaxis()->SetLabelFont(42);
   Graph_Graph7->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph7->GetYaxis()->SetTitleFont(42);
   Graph_Graph7->GetZaxis()->SetLabelFont(42);
   Graph_Graph7->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph7->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph7->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph7);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01902939388);
   graph->SetPoint(1,0.75,0.02341305304);
   graph->SetPoint(2,1.25,0.02437114781);
   graph->SetPoint(3,1.75,0.02331108418);
   graph->SetPoint(4,2.25,0.03214935243);
   
   TH1F *Graph_Graph8 = new TH1F("Graph_Graph8","Graph",100,0.05,2.45);
   Graph_Graph8->SetMinimum(0.0177174);
   Graph_Graph8->SetMaximum(0.03346135);
   Graph_Graph8->SetDirectory(0);
   Graph_Graph8->SetStats(0);
   Graph_Graph8->SetLineStyle(0);
   Graph_Graph8->SetMarkerStyle(20);
   Graph_Graph8->GetXaxis()->SetTitle("eta");
   Graph_Graph8->GetXaxis()->SetLabelFont(42);
   Graph_Graph8->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph8->GetXaxis()->SetTitleFont(42);
   Graph_Graph8->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph8->GetYaxis()->SetLabelFont(42);
   Graph_Graph8->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph8->GetYaxis()->SetTitleFont(42);
   Graph_Graph8->GetZaxis()->SetLabelFont(42);
   Graph_Graph8->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph8->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph8->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph8);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01970084973);
   graph->SetPoint(1,0.75,0.02278689086);
   graph->SetPoint(2,1.25,0.02235974595);
   graph->SetPoint(3,1.75,0.02086461456);
   graph->SetPoint(4,2.25,0.02558902427);
   
   TH1F *Graph_Graph9 = new TH1F("Graph_Graph9","Graph",100,0.05,2.45);
   Graph_Graph9->SetMinimum(0.01911203);
   Graph_Graph9->SetMaximum(0.02617784);
   Graph_Graph9->SetDirectory(0);
   Graph_Graph9->SetStats(0);
   Graph_Graph9->SetLineStyle(0);
   Graph_Graph9->SetMarkerStyle(20);
   Graph_Graph9->GetXaxis()->SetTitle("eta");
   Graph_Graph9->GetXaxis()->SetLabelFont(42);
   Graph_Graph9->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph9->GetXaxis()->SetTitleFont(42);
   Graph_Graph9->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph9->GetYaxis()->SetLabelFont(42);
   Graph_Graph9->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph9->GetYaxis()->SetTitleFont(42);
   Graph_Graph9->GetZaxis()->SetLabelFont(42);
   Graph_Graph9->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph9->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph9->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph9);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3253691,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_400.0_600.0");
   pt->Draw();
   rms_pT_400_->Modified();
   rms_pT_400_->cd();
   rms_pT_400_->SetSelected(rms_pT_400_);
}
