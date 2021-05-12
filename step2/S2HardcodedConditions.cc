#define S2HardcodedConditions_cxx

#include <cmath>
#include "S2HardcodedConditions.h"
#include <unordered_map>

using namespace std;

S2HardcodedConditions::S2HardcodedConditions() {}

S2HardcodedConditions::S2HardcodedConditions(Int_t Year) {

  TString sfFileName("HT_njets_SF_FourTops_sys.root");
  TString year_ext("");

  if(Year == 2018) {
    sfFileName = "HT_njets_SF_FourTops_sys_Run2018.root ";
    year_ext = "_2018";
  }
  else if(Year == 2016) {
    sfFileName = "HT_njets_SF_FourTops_sys_Run2016.root";
    year_ext = "_2016";
  }

  cout << "Reading SF file -- " << sfFileName << endl;
  if(!(tfile_HTNJ_SF=TFile::Open(sfFileName))){
    std::cout<<"WARNING! SF file doesn't exist! Exiting" << std::endl;
    exit(1);
  }
  
std::string SYSs[19] = {"", "_HFup", "_HFdn", "_LFup", "_LFdn", "_jesup", "_jesdn", "_hfstats1up", "_hfstats1dn", "_hfstats2up", "_hfstats2dn", "_cferr1up", "_cferr1dn", "_cferr2up", "_cferr2dn", "_lfstats1up", "_lfstats1dn", "_lfstats2up", "_lfstats2dn"};
	for(size_t isys = 0; isys<19; isys++){
  hscale_tttt_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tttt_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_ttjj_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttjj_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_ttbb_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttbb_dcsv"+SYSs[isys]+year_ext)->Clone();  
  hscale_ttcc_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttcc_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_tt2b_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tt2b_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_tt1b_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tt1b_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_HT500Njet9_ttjj_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttjj_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_HT500Njet9_ttbb_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttbb_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_HT500Njet9_ttcc_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttcc_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_HT500Njet9_tt2b_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_tt2b_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_HT500Njet9_tt1b_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_tt1b_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_STs_dcsv[SYSs[isys]]     = (TH2F*)tfile_HTNJ_SF->Get("hscale_STs_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_STtw_dcsv[SYSs[isys]]    = (TH2F*)tfile_HTNJ_SF->Get("hscale_STtw_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_STt_dcsv[SYSs[isys]]     = (TH2F*)tfile_HTNJ_SF->Get("hscale_STt_dcsv"+SYSs[isys]+year_ext)->Clone();
  hscale_WJets_dcsv[SYSs[isys]]   = (TH2F*)tfile_HTNJ_SF->Get("hscale_WJets_dcsv"+SYSs[isys]+year_ext)->Clone();
}
  hscale_tttt_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tttt_djet"+year_ext)->Clone(); 
  hscale_ttjj_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttjj_djet"+year_ext)->Clone();
  hscale_ttbb_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttbb_djet"+year_ext)->Clone();
  hscale_ttcc_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_ttcc_djet"+year_ext)->Clone();
  hscale_tt2b_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tt2b_djet"+year_ext)->Clone();
  hscale_tt1b_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_tt1b_djet"+year_ext)->Clone();
  hscale_HT500Njet9_ttjj_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttjj_djet"+year_ext)->Clone();
  hscale_HT500Njet9_ttbb_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttbb_djet"+year_ext)->Clone();
  hscale_HT500Njet9_ttcc_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_ttcc_djet"+year_ext)->Clone();
  hscale_HT500Njet9_tt2b_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_tt2b_djet"+year_ext)->Clone();
  hscale_HT500Njet9_tt1b_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_HT500Njet9_tt1b_djet"+year_ext)->Clone();
  hscale_STs_djet     = (TH2F*)tfile_HTNJ_SF->Get("hscale_STs_djet"+year_ext)->Clone();
  hscale_STtw_djet    = (TH2F*)tfile_HTNJ_SF->Get("hscale_STtw_djet"+year_ext)->Clone();
  hscale_STt_djet     = (TH2F*)tfile_HTNJ_SF->Get("hscale_STt_djet"+year_ext)->Clone();
  hscale_WJets_djet   = (TH2F*)tfile_HTNJ_SF->Get("hscale_WJets_djet"+year_ext)->Clone();

}

S2HardcodedConditions::~S2HardcodedConditions() {
}

float S2HardcodedConditions::GetCSVRenorm2DSF_HTnj(float HT, int njets, std::string sampleType, std::string sysType){

  int tmp_njets = njets;
  if(tmp_njets>6) tmp_njets=6;

  if (sampleType == "tttt"){
      return hscale_tttt_dcsv[sysType]->GetBinContent(hscale_tttt_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "ttjj"){
      return hscale_ttjj_dcsv[sysType]->GetBinContent(hscale_ttjj_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "ttcc"){
      return hscale_ttcc_dcsv[sysType]->GetBinContent(hscale_ttcc_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "ttbb"){
      return hscale_ttbb_dcsv[sysType]->GetBinContent(hscale_ttbb_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "tt2b"){
      return hscale_tt2b_dcsv[sysType]->GetBinContent(hscale_tt2b_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "tt1b"){
      return hscale_tt1b_dcsv[sysType]->GetBinContent(hscale_tt1b_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "HT500Njet9_ttjj"){
      return hscale_HT500Njet9_ttjj_dcsv[sysType]->GetBinContent(hscale_HT500Njet9_ttjj_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_ttcc"){
      return hscale_HT500Njet9_ttcc_dcsv[sysType]->GetBinContent(hscale_HT500Njet9_ttcc_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_ttbb"){
      return hscale_HT500Njet9_ttbb_dcsv[sysType]->GetBinContent(hscale_HT500Njet9_ttbb_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_tt2b"){
      return hscale_HT500Njet9_tt2b_dcsv[sysType]->GetBinContent(hscale_HT500Njet9_tt2b_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_tt1b"){
      return hscale_HT500Njet9_tt1b_dcsv[sysType]->GetBinContent(hscale_HT500Njet9_tt1b_dcsv[sysType]->FindBin(tmp_njets, HT));
  }

  if (sampleType == "STs"){
      return hscale_STs_dcsv[sysType]->GetBinContent(hscale_STs_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "STt"){
      return hscale_STt_dcsv[sysType]->GetBinContent(hscale_STt_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "STtw"){
      return hscale_STtw_dcsv[sysType]->GetBinContent(hscale_STtw_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "WJets"){
      return hscale_WJets_dcsv[sysType]->GetBinContent(hscale_WJets_dcsv[sysType]->FindBin(tmp_njets, HT));  
  }

  return 1.0;
}


float S2HardcodedConditions::GetDeepJetRenorm2DSF_HTnj(float HT, int njets, std::string sampleType){

  int tmp_njets = njets;
  if(tmp_njets>6) tmp_njets=6;

  if (sampleType == "tttt"){
      return hscale_tttt_djet->GetBinContent(hscale_tttt_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "ttjj"){
      return hscale_ttjj_djet->GetBinContent(hscale_ttjj_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "ttcc"){
      return hscale_ttcc_djet->GetBinContent(hscale_ttcc_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "ttbb"){
      return hscale_ttbb_djet->GetBinContent(hscale_ttbb_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "tt2b"){
      return hscale_tt2b_djet->GetBinContent(hscale_tt2b_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "tt1b"){
      return hscale_tt1b_djet->GetBinContent(hscale_tt1b_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "HT500Njet9_ttjj"){
      return hscale_HT500Njet9_ttjj_djet->GetBinContent(hscale_HT500Njet9_ttjj_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_ttcc"){
      return hscale_HT500Njet9_ttcc_djet->GetBinContent(hscale_HT500Njet9_ttcc_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_ttbb"){
      return hscale_HT500Njet9_ttbb_djet->GetBinContent(hscale_HT500Njet9_ttbb_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_tt2b"){
      return hscale_HT500Njet9_tt2b_djet->GetBinContent(hscale_HT500Njet9_tt2b_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "HT500Njet9_tt1b"){
      return hscale_HT500Njet9_tt1b_djet->GetBinContent(hscale_HT500Njet9_tt1b_djet->FindBin(tmp_njets, HT));
  }

  if (sampleType == "STs"){
      return hscale_STs_djet->GetBinContent(hscale_STs_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "STt"){
      return hscale_STt_djet->GetBinContent(hscale_STt_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "STtw"){
      return hscale_STtw_djet->GetBinContent(hscale_STtw_djet->FindBin(tmp_njets, HT));  
  }

  if (sampleType == "WJets"){
      return hscale_WJets_djet->GetBinContent(hscale_WJets_djet->FindBin(tmp_njets, HT));  
  }

  return 1.0;
}

