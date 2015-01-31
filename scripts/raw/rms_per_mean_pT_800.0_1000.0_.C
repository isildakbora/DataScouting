{
//=========Macro generated from canvas: rms_pT_800_/rms_pT_800_
//=========  (Tue Jan  6 15:46:28 2015) by ROOT version5.34/05
   TCanvas *rms_pT_800_ = new TCanvas("rms_pT_800_", "rms_pT_800_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_800_->SetHighLightColor(2);
   rms_pT_800_->Range(-0.4360759,-0.004922305,2.601899,0.03294158);
   rms_pT_800_->SetFillColor(0);
   rms_pT_800_->SetBorderMode(0);
   rms_pT_800_->SetBorderSize(2);
   rms_pT_800_->SetTickx(1);
   rms_pT_800_->SetTicky(1);
   rms_pT_800_->SetLeftMargin(0.16);
   rms_pT_800_->SetRightMargin(0.05);
   rms_pT_800_->SetTopMargin(0.05);
   rms_pT_800_->SetBottomMargin(0.13);
   rms_pT_800_->SetFrameFillStyle(0);
   rms_pT_800_->SetFrameBorderMode(0);
   rms_pT_800_->SetFrameFillStyle(0);
   rms_pT_800_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_800.0_1000.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.0172437655);
   graph->SetPoint(1,0.75,0.02125710869);
   graph->SetPoint(2,1.25,0.02822580645);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph13 = new TH1F("Graph_Graph13","rms_per_mean_eta_vs_ratio_in_pT_800.0_1000.0",100,0.05,2.45);
   Graph_Graph13->SetMinimum(0);
   Graph_Graph13->SetMaximum(0.03104839);
   Graph_Graph13->SetDirectory(0);
   Graph_Graph13->SetStats(0);
   Graph_Graph13->SetLineStyle(0);
   Graph_Graph13->SetMarkerStyle(20);
   Graph_Graph13->GetXaxis()->SetTitle("eta");
   Graph_Graph13->GetXaxis()->SetLabelFont(42);
   Graph_Graph13->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph13->GetXaxis()->SetTitleFont(42);
   Graph_Graph13->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph13->GetYaxis()->SetLabelFont(42);
   Graph_Graph13->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph13->GetYaxis()->SetTitleFont(42);
   Graph_Graph13->GetZaxis()->SetLabelFont(42);
   Graph_Graph13->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph13->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph13->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph13);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01763157545);
   graph->SetPoint(1,0.75,0.02357569464);
   graph->SetPoint(2,1.25,0.0209782273);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph14 = new TH1F("Graph_Graph14","Graph",100,0.05,2.45);
   Graph_Graph14->SetMinimum(0);
   Graph_Graph14->SetMaximum(0.02593326);
   Graph_Graph14->SetDirectory(0);
   Graph_Graph14->SetStats(0);
   Graph_Graph14->SetLineStyle(0);
   Graph_Graph14->SetMarkerStyle(20);
   Graph_Graph14->GetXaxis()->SetTitle("eta");
   Graph_Graph14->GetXaxis()->SetLabelFont(42);
   Graph_Graph14->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph14->GetXaxis()->SetTitleFont(42);
   Graph_Graph14->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph14->GetYaxis()->SetLabelFont(42);
   Graph_Graph14->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph14->GetYaxis()->SetTitleFont(42);
   Graph_Graph14->GetZaxis()->SetLabelFont(42);
   Graph_Graph14->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph14->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph14->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph14);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.01744111853);
   graph->SetPoint(1,0.75,0.02571550613);
   graph->SetPoint(2,1.25,0.0103638608);
   graph->SetPoint(3,1.75,0);
   graph->SetPoint(4,2.25,0);
   
   TH1F *Graph_Graph15 = new TH1F("Graph_Graph15","Graph",100,0.05,2.45);
   Graph_Graph15->SetMinimum(0);
   Graph_Graph15->SetMaximum(0.02828706);
   Graph_Graph15->SetDirectory(0);
   Graph_Graph15->SetStats(0);
   Graph_Graph15->SetLineStyle(0);
   Graph_Graph15->SetMarkerStyle(20);
   Graph_Graph15->GetXaxis()->SetTitle("eta");
   Graph_Graph15->GetXaxis()->SetLabelFont(42);
   Graph_Graph15->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph15->GetXaxis()->SetTitleFont(42);
   Graph_Graph15->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph15->GetYaxis()->SetLabelFont(42);
   Graph_Graph15->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph15->GetYaxis()->SetTitleFont(42);
   Graph_Graph15->GetZaxis()->SetLabelFont(42);
   Graph_Graph15->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph15->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph15->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph15);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3320805,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_800.0_1000.0");
   pt->Draw();
   rms_pT_800_->Modified();
   rms_pT_800_->cd();
   rms_pT_800_->SetSelected(rms_pT_800_);
}
