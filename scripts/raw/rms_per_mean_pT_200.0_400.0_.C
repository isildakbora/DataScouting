{
//=========Macro generated from canvas: rms_pT_200_/rms_pT_200_
//=========  (Tue Jan  6 15:46:26 2015) by ROOT version5.34/05
   TCanvas *rms_pT_200_ = new TCanvas("rms_pT_200_", "rms_pT_200_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_pT_200_->SetHighLightColor(2);
   rms_pT_200_->Range(-0.4360759,0.01377899,2.601899,0.04556972);
   rms_pT_200_->SetFillColor(0);
   rms_pT_200_->SetBorderMode(0);
   rms_pT_200_->SetBorderSize(2);
   rms_pT_200_->SetTickx(1);
   rms_pT_200_->SetTicky(1);
   rms_pT_200_->SetLeftMargin(0.16);
   rms_pT_200_->SetRightMargin(0.05);
   rms_pT_200_->SetTopMargin(0.05);
   rms_pT_200_->SetBottomMargin(0.13);
   rms_pT_200_->SetFrameFillStyle(0);
   rms_pT_200_->SetFrameBorderMode(0);
   rms_pT_200_->SetFrameFillStyle(0);
   rms_pT_200_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_eta_vs_ratio_in_pT_200.0_400.0");
   graph->SetFillColor(1);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.02008415126);
   graph->SetPoint(1,0.75,0.02293622416);
   graph->SetPoint(2,1.25,0.02594042828);
   graph->SetPoint(3,1.75,0.02242331651);
   graph->SetPoint(4,2.25,0.04180781664);
   
   TH1F *Graph_Graph4 = new TH1F("Graph_Graph4","rms_per_mean_eta_vs_ratio_in_pT_200.0_400.0",100,0.05,2.45);
   Graph_Graph4->SetMinimum(0.01791178);
   Graph_Graph4->SetMaximum(0.04398018);
   Graph_Graph4->SetDirectory(0);
   Graph_Graph4->SetStats(0);
   Graph_Graph4->SetLineStyle(0);
   Graph_Graph4->SetMarkerStyle(20);
   Graph_Graph4->GetXaxis()->SetTitle("eta");
   Graph_Graph4->GetXaxis()->SetLabelFont(42);
   Graph_Graph4->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph4->GetXaxis()->SetTitleFont(42);
   Graph_Graph4->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph4->GetYaxis()->SetLabelFont(42);
   Graph_Graph4->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph4->GetYaxis()->SetTitleFont(42);
   Graph_Graph4->GetZaxis()->SetLabelFont(42);
   Graph_Graph4->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph4->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph4->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph4);
   
   graph->Draw("ap");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.02089203843);
   graph->SetPoint(1,0.75,0.02456289395);
   graph->SetPoint(2,1.25,0.0243979283);
   graph->SetPoint(3,1.75,0.02153162852);
   graph->SetPoint(4,2.25,0.03065398148);
   
   TH1F *Graph_Graph5 = new TH1F("Graph_Graph5","Graph",100,0.05,2.45);
   Graph_Graph5->SetMinimum(0.01991584);
   Graph_Graph5->SetMaximum(0.03163018);
   Graph_Graph5->SetDirectory(0);
   Graph_Graph5->SetStats(0);
   Graph_Graph5->SetLineStyle(0);
   Graph_Graph5->SetMarkerStyle(20);
   Graph_Graph5->GetXaxis()->SetTitle("eta");
   Graph_Graph5->GetXaxis()->SetLabelFont(42);
   Graph_Graph5->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph5->GetXaxis()->SetTitleFont(42);
   Graph_Graph5->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph5->GetYaxis()->SetLabelFont(42);
   Graph_Graph5->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph5->GetYaxis()->SetTitleFont(42);
   Graph_Graph5->GetZaxis()->SetLabelFont(42);
   Graph_Graph5->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph5->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph5->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph5);
   
   graph->Draw("p");
   
   graph = new TGraph(5);
   graph->SetName("Graph");
   graph->SetTitle("Graph");
   graph->SetFillColor(1);
   graph->SetMarkerColor(3);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,0.25,0.02010349668);
   graph->SetPoint(1,0.75,0.02335040799);
   graph->SetPoint(2,1.25,0.02442542734);
   graph->SetPoint(3,1.75,0.02096676289);
   graph->SetPoint(4,2.25,0.02922394304);
   
   TH1F *Graph_Graph6 = new TH1F("Graph_Graph6","Graph",100,0.05,2.45);
   Graph_Graph6->SetMinimum(0.01919145);
   Graph_Graph6->SetMaximum(0.03013599);
   Graph_Graph6->SetDirectory(0);
   Graph_Graph6->SetStats(0);
   Graph_Graph6->SetLineStyle(0);
   Graph_Graph6->SetMarkerStyle(20);
   Graph_Graph6->GetXaxis()->SetTitle("eta");
   Graph_Graph6->GetXaxis()->SetLabelFont(42);
   Graph_Graph6->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetXaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph6->GetXaxis()->SetTitleFont(42);
   Graph_Graph6->GetYaxis()->SetTitle("RMS/MEAN");
   Graph_Graph6->GetYaxis()->SetLabelFont(42);
   Graph_Graph6->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetYaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetYaxis()->SetTitleOffset(1.6);
   Graph_Graph6->GetYaxis()->SetTitleFont(42);
   Graph_Graph6->GetZaxis()->SetLabelFont(42);
   Graph_Graph6->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph6->GetZaxis()->SetLabelSize(0.035);
   Graph_Graph6->GetZaxis()->SetTitleFont(42);
   graph->SetHistogram(Graph_Graph6);
   
   graph->Draw("p");
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.3253691,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_eta_vs_ratio_in_pT_200.0_400.0");
   pt->Draw();
   rms_pT_200_->Modified();
   rms_pT_200_->cd();
   rms_pT_200_->SetSelected(rms_pT_200_);
}
