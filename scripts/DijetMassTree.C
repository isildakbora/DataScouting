

void DijetMassTree()
{
   gROOT->ProcessLine(".L DSComp.C");

   TRandom* r = new TRandom3();

   float pTbins[]  = {30., 103., 206., 309., 413., 515., 618., 721., 1237.};
   const Int_t   n_pTbins  = sizeof(pTbins)/sizeof(float)-1;

   float etaBins[] = {0., 0.5, 1.0, 1.5, 2.0, 2.5};
   const Int_t   n_etaBins = sizeof(etaBins)/sizeof(float)-1;

   float massBins[88] = {1, 3, 6, 10, 16, 23, 31, 40, 50, 61, 74, 88, 103, 119, 137, 156, 176, 197, 220, 244, 270, 296, 325, 354, 386, 419, 453, 489, 526, 565, 606, 649,  693, 740, 788, 838, 890, 944, 1000, 1058, 1118, 1181, 1246, 1313, 1383, 1455, 1530, 1607, 1687, 1770, 1856, 1945, 2037, 2132, 2231, 2332, 2438, 2546, 2659, 2775, 2895, 3019, 3147, 3279, 3416, 3558, 3704, 3854, 4010, 4171, 4337, 4509, 4686, 4869, 5058, 5253, 5455, 5663, 5877, 6099, 6328, 6564, 6808, 7000, 7250,7500,7750,8000}; 

   const Int_t   n_massBins = sizeof(massBins)/sizeof(float)-1;

   TH1F *h_dsMjj              = new TH1F("ds Mjj", "ds Mjj", n_massBins, massBins);
   TH1F *h_recoMjj            = new TH1F("reco Mjj", "reco Mjj", n_massBins, massBins);
   TH1F *h_reco_smeared_Mjj   = new TH1F("reco_smeared Mjj", "reco_smeared Mjj", n_massBins, massBins);
   h_dsMjj->Sumw2();
   h_recoMjj->Sumw2();
   h_reco_smeared_Mjj->Sumw2();

   TH1F *h_delta_Mjj_after_smearing = new TH1F("h_delta_Mjj_after_smearing", "h_delta_Mjj_after_smearing", 2400,-2.4, 2.4);
   TH1F *h_delta_Mjj                = new TH1F("h_delta_Mjj", "h_delta_Mjj", 2400,-2.4, 2.4);
   h_delta_Mjj->Sumw2();
   h_delta_Mjj_after_smearing->Sumw2();

   TFile *f   = new TFile("dijet.root");
   TFile *res = new TFile("Delta_pT_Resolution.root");
   TTree *t_dijemass = f->FindObjectAny("DijetMassTree");
   // Declaration of leaf types
   Float_t         dsMjj;
   Float_t         recoMjj;
   Float_t         reco_smeared_Mjj;
   Int_t           runNo;
   Int_t           evtNo;

  Float_t recoMjj, dsMjj, dsJetPt0, dsJetE0, dsJetE1, dsJetPt1, dsJetEta0, dsJetEta1, dsJetPhi0, dsJetPhi1, recoJetPt0, recoJetPt1, recoJetE0, recoJetE1, recoJetEta0, recoJetEta1, recoJetPhi0, recoJetPhi1;

   // List of branches
   TBranch        *b_dsMjj;   //!
   TBranch        *b_recoMjj;   //!
   TBranch        *b_runNo;   //!
   TBranch        *b_evtNo;

   TBranch        *b_dsJetEta0;  //!
   TBranch        *b_dsJetEta1;   //!
   TBranch        *b_dsJetPhi0;   //!
   TBranch        *b_dsJetPhi1;   //!
   TBranch        *b_dsJetPt0;   //!
   TBranch        *b_dsJetPt1;   //!
   TBranch        *b_dsJetE0;  //!
   TBranch        *b_dsJetE1;   //!

   TBranch        *b_recoJetEta0;  //!
   TBranch        *b_recoJetEta1;   //!
   TBranch        *b_recoJetPhi0;   //!
   TBranch        *b_recoJetPhi1;   //!
   TBranch        *b_recoJetPt0;   //!
   TBranch        *b_recoJetPt1;   //!
   TBranch        *b_recoJetE0;  //!
   TBranch        *b_recoJetE1;   //!


   t_dijemass->SetBranchAddress("dsMjj", &dsMjj, &b_dsMjj);
   t_dijemass->SetBranchAddress("recoMjj", &recoMjj, &b_recoMjj);
   t_dijemass->SetBranchAddress("runNo", &runNo, &b_runNo);
   t_dijemass->SetBranchAddress("evtNo", &evtNo, &b_evtNo);

   t_dijemass->SetBranchAddress("dsJetEta0", &dsJetEta0, &b_dsJetEta0);
   t_dijemass->SetBranchAddress("dsJetEta1", &dsJetEta1, &b_dsJetEta1);

   t_dijemass->SetBranchAddress("dsJetPhi0", &dsJetPhi0, &b_dsJetPhi0);
   t_dijemass->SetBranchAddress("dsJetPhi1", &dsJetPhi1, &b_dsJetPhi1);

   t_dijemass->SetBranchAddress("dsJetPt0", &dsJetPt0, &b_dsJetPt0);
   t_dijemass->SetBranchAddress("dsJetPt1", &dsJetPt1, &b_dsJetPt1);

   t_dijemass->SetBranchAddress("dsJetPt0", &dsJetE0, &b_dsJetE0);
   t_dijemass->SetBranchAddress("dsJetPt1", &dsJetE1, &b_dsJetE1);

   t_dijemass->SetBranchAddress("recoJetEta0", &recoJetEta0, &b_recoJetEta0);
   t_dijemass->SetBranchAddress("recoJetEta1", &recoJetEta1, &b_recoJetEta1);

   t_dijemass->SetBranchAddress("recoJetPhi0", &recoJetPhi0, &b_recoJetPhi0);
   t_dijemass->SetBranchAddress("recoJetPhi1", &recoJetPhi1, &b_recoJetPhi1);

   t_dijemass->SetBranchAddress("recoJetPt0", &recoJetPt0, &b_recoJetPt0);
   t_dijemass->SetBranchAddress("recoJetPt1", &recoJetPt1, &b_recoJetPt1);

   t_dijemass->SetBranchAddress("recoJetPt0", &recoJetE0, &b_recoJetE0);
   t_dijemass->SetBranchAddress("recoJetPt1", &recoJetE1, &b_recoJetE1);

   if (t_dijemass == 0) return;

   // Get the smearing functions and hold in the mem
   TF1 *cbfit[8][5];
   TString name;
   for (int i = 0; i < n_pTbins; ++i)
   {
      for (int j=0; j<n_etaBins; ++j)
      {
         name = "Delta_pT_"+TString::Format("%.0f",pTbins[i])+"_"+TString::Format("%.0f",pTbins[i+1])+"_eta_"+TString::Format("%2.1f",j*0.5)+"_"+TString::Format("%2.1f",(j+1)*0.5);
         std::cout << name << std::endl;
         cbfit[i][j] = (TF1*)res->FindObjectAny(name);
      }
   }

   int decade = 0;
   Long64_t nentries = t_dijemass->GetEntriesFast();
   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries/10;jentry++) 
   {
   	nb = t_dijemass->GetEntry(jentry);
   	nbytes += nb;
      
      //----------- progress report -------------
      double progress = 100.*jentry/nentries;
      int k = TMath::FloorNint(progress);
      std::cout << "\r" << progress << "% completed: ";
      //std::cout << "[" << std::string(k, '|') << std::string(99-k, ' ') << "]";
      std::cout.flush();
      decade = k; 

      int pTbin0     = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsJetPt0, dsJetEta0).first;
      int etabin0    = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsJetPt0, dsJetEta0).second;

      int pTbin1     = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsJetPt1, dsJetEta1).first;
      int etabin1    = Get_ij(pTbins, n_pTbins, etaBins, n_etaBins, dsJetPt1, dsJetEta1).second;

      double x_min0 = cbfit[pTbin0][etabin0]->GetMinimumX();
      double x_max0 = cbfit[pTbin0][etabin0]->GetMaximumX();

      double x_min1 = cbfit[pTbin1][etabin1]->GetMinimumX();
      double x_max1 = cbfit[pTbin1][etabin1]->GetMaximumX();

      Float_t smearPt0 = GetRand(cbfit[pTbin0][etabin0], x_min0, x_max0, r->Integer(1e+10));
      Float_t smearPt1 = GetRand(cbfit[pTbin1][etabin1], x_min1, x_max1, r->Integer(1e+10));
      
      // TLorentzVector is extremely slow in CINT, so using by hand calculation

      dsMjj   = CalculateDijetMass(dsJetPt0, dsJetPt1, dsJetE0,  dsJetE1, dsJetEta0, dsJetEta1, dsJetPhi0, dsJetPhi1);
      recoMjj = CalculateDijetMass(recoJetPt0, recoJetPt1, recoJetE0,  recoJetE1, recoJetEta0, recoJetEta1, recoJetPhi0, recoJetPhi1);

      // smearing factor should be applied as (1+smearpT)*recopT
      // since;
      // (dspT-recopT)/recopT = smearpT
      // (dspT-recopT) = recopT*smearpT
      // dspT =recopT*smearpT+recopT = (1+smearpT)*recopT

      reco_smeared_Mjj = CalculateDijetMass((1.+smearPt0)*recoJetPt0, (1.+smearPt1)*recoJetPt1, (1.+smearPt0)*recoJetE0, (1.+smearPt1)*recoJetE1, recoJetEta0, recoJetEta1, recoJetPhi0, recoJetPhi1);
      
      h_dsMjj->Fill(dsMjj);
      h_recoMjj->Fill(recoMjj);
      h_reco_smeared_Mjj->Fill(reco_smeared_Mjj);

      h_delta_Mjj->Fill((dsMjj-recoMjj)/(recoMjj));
      h_delta_Mjj_after_smearing->Fill((dsMjj-reco_smeared_Mjj)/(reco_smeared_Mjj));

      std::cout << dsMjj<< "\t" << recoMjj << "\t" << reco_smeared_Mjj << "\t" << (dsMjj-reco_smeared_Mjj)/reco_smeared_Mjj <<   "\t" << (dsMjj-recoMjj)/recoMjj << std::endl;
   }
   
   std::cout << nentries << std::endl;

   h_dsMjj->SetLineColor(kBlack);
   h_recoMjj->SetLineColor(kBlue);
   h_reco_smeared_Mjj->SetLineColor(kRed);

   TCanvas *c1 = new TCanvas("can1");
   c1->cd();
   h_delta_Mjj_after_smearing->SetLineColor(kRed);
   h_delta_Mjj_after_smearing->Draw("HIST");

   TCanvas *c2 = new TCanvas("can2");
   c2->cd();
   h_delta_Mjj->Draw("HIST");

   TCanvas *c3 = new TCanvas("can3");
   c3->cd();
   h_dsMjj->Divide(h_reco_smeared_Mjj);
   h_dsMjj->Draw("HIST");
}

Float_t CalculateDijetMass(Float_t JetPt0, Float_t JetPt1, Float_t JetE0, Float_t JetE1, Float_t JetEta0, Float_t JetEta1,Float_t JetPhi0, Float_t JetPhi1)
{
   Float_t E0 = JetE0;
   Float_t X0 = JetPt0*TMath::Cos(JetPhi0);
   Float_t Y0 = JetPt0*TMath::Sin(JetPhi0);
   Float_t Z0 = JetPt0*TMath::SinH(JetEta0);
   
   Float_t E1 = JetE1;
   Float_t X1 = JetPt1*TMath::Cos(JetPhi1);
   Float_t Y1 = JetPt1*TMath::Sin(JetPhi1);
   Float_t Z1 = JetPt1*TMath::SinH(JetEta1);

   Float_t Mjj= TMath::Sqrt((E0+E1)**2 - (X0+X1)**2 - (Y0+Y1)**2 - (Z0+Z1)**2);
   return Mjj;
}

Double_t GetRand(TF1 *func, Double_t X_MIN, Double_t X_MAX, int seed )
{
   Double_t Y_MAX;
   Y_MAX = func->GetMaximum();
   TRandom3* r = new TRandom3(seed);
   
   Double_t x   =0;
   Double_t y   = r->Uniform();
   Double_t f_y = 9e+10;
   
   while(1)
   {
      x   = r->Uniform(X_MIN, X_MAX);
      y   = r->Uniform(0, Y_MAX);
      f_y = func->Eval(x);

      if(f_y > y)
         break;
   }
   return x;
}
