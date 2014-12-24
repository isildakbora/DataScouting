void TProfile3D(){

{
  TCanvas *c1 = new TCanvas("c1","Profile histogram example",200,10,700,500);
    hprof3d  = new TProfile3D("hprof3d","Profile of pt versus px, py and pz",40,-4,4,40,-4,4,40,0,20);
      Double_t px, py, pz, pt;
        TRandom3 r(0);
	  for ( Int_t i=0; i<25000; i++) {
	       r.Rannor(px,py);
	            pz = px*px + py*py;
		         pt = r.Landau(0,1);
			      hprof3d->Fill(px,py,pz,pt,1);
			        }
				  hprof3d->Draw();
				  }

}
