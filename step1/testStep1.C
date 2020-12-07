#include "step1.cc"
#include "BTagCalibForLJMet.cpp"
#include "HardcodedConditions.cc"
#include<vector>
using namespace std;

void testStep1(){
  
  TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/FWLJMET102X_1lep2017_Oct2019/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/singleLep2017/191031_222012/0000/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_1.root";
  
//  TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/FWLJMET102X_1lep2017_Oct2019/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/singleLep2017/191029_235508/0000/TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_59.root";
  //TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/FWLJMET102X_1lep2018_Oct2019/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/singleLep2018/191110_033632/0000/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_99.root";
  //TString inputFile="root://cmseos.fnal.gov//store/user/lpcljm/FWLJMET102X_1lep2018_Oct2019/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/singleLep2018/191121_205009/0001/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8_1664.root";
  TString outputFile="test";
  Int_t Year=2017;
  
  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");
  
  if ( inputFile.Contains("Run2017") || inputFile.Contains("Run2018") || inputFile.Contains("Single") || inputFile.Contains("Double") || inputFile.Contains("MuonEG") || inputFile.Contains("EGamma") || inputFile.Contains("JetHT") ) { 
    step1 t(inputFile,outputFile+"nominal.root",Year,"nominal");
    t.Loop("ljmet", "ljmet"); 
    }

  else {
    //vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown" };
    vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown","JEC_Totalup","JEC_Totaldown",
    "JEC_FlavorQCDup","JEC_RelativeBalup","JEC_RelativeSample_YEARup","JEC_Absoluteup","JEC_Absolute_YEARup","JEC_HFup","JEC_HF_YEARup","JEC_EC2up","JEC_EC2_YEARup","JEC_BBEC1up","JEC_BBEC1_YEARup",
    "JEC_FlavorQCDdown","JEC_RelativeBaldown","JEC_RelativeSample_YEARdown","JEC_Absolutedown","JEC_Absolute_YEARdown","JEC_HFdown","JEC_HF_YEARdown","JEC_EC2down","JEC_EC2_YEARdown","JEC_BBEC1down","JEC_BBEC1_YEARdown" };
    for (size_t i =0; i<shifts.size(); ++i) {
      shifts[i].ReplaceAll("YEAR",Form("%d",Year));
      cout << endl << "Running shift " << shifts[i] << endl;
      TString tName = "ljmet";
      if ( shifts[i]=="JECup" || shifts[i]=="JECdown" || shifts[i]=="JERup" || shifts[i]=="JERdown" ) { tName.Append("_"); tName.Append(shifts[i]); }
      step1 t(inputFile,outputFile+shifts[i]+".root",Year,shifts[i]);
      t.saveHistograms();
      t.Loop(tName, "ljmet");
      }
    }
}
