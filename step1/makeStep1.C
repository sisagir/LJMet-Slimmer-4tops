#include <TSystem.h>
#include "step1.cc"
#include "BTagCalibForLJMet.cpp"
#include "HardcodedConditions.cc"
#include<vector>
#include<string>
using namespace std;

void makeStep1(TString macroDir, TString inputFile, TString outputFile, Int_t Year){

  gROOT->SetMacroPath(macroDir);

  gSystem->AddIncludePath("-I$CMSSW_BASE/src/");

  TString incl("-I");
  incl+=macroDir;
  gSystem->AddIncludePath(incl);

  if ( inputFile.Contains("Run2017") || inputFile.Contains("Run2018") || inputFile.Contains("Single") || inputFile.Contains("Double") || inputFile.Contains("MuonEG") || inputFile.Contains("EGamma") || inputFile.Contains("JetHT") ) { 
    step1 t(inputFile,outputFile.ReplaceAll(".root","nominal.root"),Year);
    t.Loop("ljmet", "ljmet"); 
    }

  else {
  	vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown" };
  	for (size_t i =0; i<shifts.size(); ++i) {
      cout << endl << "Running shift " << shifts[i] << endl;
      TString tName = "ljmet";
      if ( !shifts[i].Contains("nominal") ) { tName.Append("_"); tName.Append(shifts[i]); }
      step1 t(inputFile,outputFile.ReplaceAll(".root",shifts[i].Append(".root")),Year); //"shifts[i]" is now changed to "shifts[i].root"
      t.saveHistograms();
      t.Loop(tName, "ljmet");
      outputFile.ReplaceAll(shifts[i],".root"); //Change outputFile back to its original name.
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
      if ( inputFile.Contains("Run2017") || inputFile.Contains("Run2018") || inputFile.Contains("Single") || inputFile.Contains("Double") || inputFile.Contains("MuonEG") || inputFile.Contains("EGamma") || inputFile.Contains("JetHT") )
      { 
        step1 t(inputFile,outputFile.ReplaceAll(".root","nominal.root"),Year);
        t.Loop("ljmet", "ljmet",calib); 
      }
      else
      {
        vector<TString> shifts = { "nominal", "JECup", "JECdown", "JERup", "JERdown" };
        for (size_t i =0; i<shifts.size(); ++i)
        {
          cout << endl << "Running shift " << shifts[i] << endl;
          TString tName = "ljmet";
          if ( !shifts[i].Contains("nominal") )
          {
            tName.Append("_"); tName.Append(shifts[i]);
          }
          step1 t(inputFile,outputFile.ReplaceAll(".root",shifts[i].Append(".root")),Year); //"shifts[i]" is now changed to "shifts[i].root"
          t.saveHistograms();
          t.Loop(tName, "ljmet",calib);
          outputFile.ReplaceAll(shifts[i],".root"); //Change outputFile back to its original name.
        }
      }
    }
  }
  else cout << "Unable to open filelist"; 
}
