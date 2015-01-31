{
//=========Macro generated from canvas: rms_eta_2_/rms_eta_2_
//=========  (Fri Jan 23 11:22:30 2015) by ROOT version5.34/05
   TCanvas *rms_eta_2_ = new TCanvas("rms_eta_2_", "rms_eta_2_",11,73,600,300);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   rms_eta_2_->SetHighLightColor(2);
   rms_eta_2_->Range(-304.4354,-3.459868e+154,1598.286,4.64368e+153);
   rms_eta_2_->SetFillColor(0);
   rms_eta_2_->SetBorderMode(0);
   rms_eta_2_->SetBorderSize(2);
   rms_eta_2_->SetTickx(1);
   rms_eta_2_->SetTicky(1);
   rms_eta_2_->SetLeftMargin(0.16);
   rms_eta_2_->SetRightMargin(0.05);
   rms_eta_2_->SetTopMargin(0.05);
   rms_eta_2_->SetBottomMargin(0.13);
   rms_eta_2_->SetFrameFillStyle(0);
   rms_eta_2_->SetFrameBorderMode(0);
   rms_eta_2_->SetFrameFillStyle(0);
   rms_eta_2_->SetFrameBorderMode(0);
   
   TGraph *graph = new TGraph(13);
   graph->SetName("Graph");
   graph->SetTitle("rms_per_mean_pT_vs_ratio_in_eta_2_2");
   graph->SetFillColor(1);
   graph->SetMarkerColor(2);
   graph->SetMarkerStyle(21);
   graph->SetPoint(0,100,0.03413844654);
   graph->SetPoint(1,300,-2.681561586e+154);
   graph->SetPoint(2,500,-2.534429146e-93);
   graph->SetPoint(3,700,-2.864951024e-54);
   graph->SetPoint(4,900,2.152470685e-314);
   graph->SetPoint(5,1100,3.131513063e-294);
   graph->SetPoint(6,1300,2.152458337e-314);
   graph->SetPoint(7,1650,0);
   graph->SetPoint(8,2150,0);
   graph->SetPoint(9,2650,-0.001223325729);
   graph->SetPoint(10,3150,0);
   graph->SetPoint(11,3650,0);
   graph->SetPoint(12,4150,0);
   
   TH1F *Graph_Graph12 = new TH1F("Graph_Graph12","rms_per_mean_pT_vs_ratio_in_eta_2_2",100,0,4555);
   Graph_Graph12->SetMinimum(-2.949718e+154);
   Graph_Graph12->SetMaximum(2.681562e+153);
   Graph_Graph12->SetDirectory(0);
   Graph_Graph12->SetStats(0);
   Graph_Graph12->SetLineStyle(0);
   Graph_Graph12->SetMarkerStyle(20);
   Graph_Graph12->GetXaxis()->SetTitle("pT");
   Graph_Graph12->GetXaxis()->SetRange(1,33);
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
   
   graph->Draw("ap");
   
   TLegend *leg = new TLegend(0.6,0.7,0.9,0.9,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillColor(0);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph","nPVzbins_7_15","lp");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(1);
   entry->SetMarkerColor(2);
   entry->SetMarkerStyle(21);
   entry->SetMarkerSize(1);
   leg->Draw();
   
   TPaveText *pt = new TPaveText(0,0.9502941,0.2733557,0.99,"blNDC");
   pt->SetName("title");
   pt->SetBorderSize(2);
   pt->SetFillColor(10);
   TText *text = pt->AddText("rms_per_mean_pT_vs_ratio_in_eta_2_2");
   pt->Draw();
   rms_eta_2_->Modified();
   rms_eta_2_->cd();
   rms_eta_2_->SetSelected(rms_eta_2_);
}
