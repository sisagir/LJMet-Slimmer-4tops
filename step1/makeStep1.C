#include <TSystem.h>
#include "step1.cc"
#include "BTagCalibForLJMet.cpp"
#include "HardcodedConditions.cc"
#include <vector>
#include <string>
using namespace std;

void makeStep1(TString macroDir, TString inputFile, TString outputFile, Int_t Year){

  gROOT->SetMacroPath(macroDir);

  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");

  TString incl("-I");
  incl+=macroDir;
  gSystem->AddIncludePath(incl);
  
  outputFile.ReplaceAll(".root",""); // extension will be added back below with the shift names

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

void makeStep1(TString macroDir, string filelist, Int_t Year){

  gROOT->SetMacroPath(macroDir);

  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");

  TString incl("-I");
  incl+=macroDir;
  gSystem->AddIncludePath(incl);

  string line;
  ifstream myfile (filelist);
  vector<pair<string,string> > Files;
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      auto pos = line.find(",");
      Files.emplace_back(line.substr(0, pos),line.substr(pos + 1));
    }
    myfile.close();

    std::string btagcsvfile("DeepCSV_94XSF_V5_B_F.csv");
    if (Year== 2018) {
      btagcsvfile = "DeepCSV_102XSF_V2.csv"; 
    }
    if (Year== 2016) {
      btagcsvfile = "DeepCSV_2016LegacySF_V1.csv";
    }
    cout << "CSV reshaping file " << btagcsvfile << endl;
    auto calib = new const BTagCalibrationForLJMet("DeepCSV", btagcsvfile); 
    for (auto f : Files)
    {
      TString inputFile(f.first);
      TString outputFile(f.second);
      outputFile.ReplaceAll(".root",""); // extension will be added back below with the shift names
      if ( inputFile.Contains("Run2017") || inputFile.Contains("Run2018") || inputFile.Contains("Single") || inputFile.Contains("Double") || inputFile.Contains("MuonEG") || inputFile.Contains("EGamma") || inputFile.Contains("JetHT") )
      { 
        step1 t(inputFile,outputFile+"nominal.root",Year,"nominal");
        t.Loop("ljmet", "ljmet",calib); 
      }
      else
      {
        //vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown" };
        vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown","JEC_Totalup","JEC_Totaldown",
        "JEC_FlavorQCDup","JEC_RelativeBalup","JEC_RelativeSample_YEARup","JEC_Absoluteup","JEC_Absolute_YEARup","JEC_HFup","JEC_HF_YEARup","JEC_EC2up","JEC_EC2_YEARup","JEC_BBEC1up","JEC_BBEC1_YEARup",
        "JEC_FlavorQCDdown","JEC_RelativeBaldown","JEC_RelativeSample_YEARdown","JEC_Absolutedown","JEC_Absolute_YEARdown","JEC_HFdown","JEC_HF_YEARdown","JEC_EC2down","JEC_EC2_YEARdown","JEC_BBEC1down","JEC_BBEC1_YEARdown" };
        for (size_t i =0; i<shifts.size(); ++i)
        {
          shifts[i].ReplaceAll("YEAR",Form("%d",Year));
          cout << endl << "Running shift " << shifts[i] << endl;
          if ( shifts[i]!="nominal" && (inputFile.Contains("_hdampDOWN_") || inputFile.Contains("hdampUP") || inputFile.Contains("_TuneCP5up_") || inputFile.Contains("_TuneCP5down_")) ) continue;
          TString tName = "ljmet";
          if ( shifts[i]=="JECup" || shifts[i]=="JECdown" || shifts[i]=="JERup" || shifts[i]=="JERdown" )
          {
            tName.Append("_"); tName.Append(shifts[i]);
          }
          step1 t(inputFile,outputFile+shifts[i]+".root",Year,shifts[i]);
          t.saveHistograms();
          t.Loop(tName, "ljmet",calib);
        }
      }
    }
  }
  else cout << "Unable to open filelist"; 
}
