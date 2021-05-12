#ifndef S2HardcodedConditions_h
#define S2HardcodedConditions_h

#include <iostream>
#include <vector>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <algorithm>


typedef std::map<std::string, TH2F*> SFmap;

class S2HardcodedConditions{
    
public:
    
    S2HardcodedConditions();
    S2HardcodedConditions(Int_t Year);
    ~S2HardcodedConditions();

    float GetDeepJetRenorm2DSF_HTnj(float HT, int njets, std::string sampleType);
    float GetCSVRenorm2DSF_HTnj(float HT, int njets, std::string sampleType, std::string sysType);

    TFile *tfile_HTNJ_SF;

    SFmap hscale_tttt_dcsv;
    SFmap hscale_ttjj_dcsv;
    SFmap hscale_ttbb_dcsv;
    SFmap hscale_ttcc_dcsv;
    SFmap hscale_tt2b_dcsv;
    SFmap hscale_tt1b_dcsv;
    SFmap hscale_HT500Njet9_ttjj_dcsv;
    SFmap hscale_HT500Njet9_ttbb_dcsv;
    SFmap hscale_HT500Njet9_ttcc_dcsv;
    SFmap hscale_HT500Njet9_tt2b_dcsv;
    SFmap hscale_HT500Njet9_tt1b_dcsv;
    SFmap hscale_STs_dcsv;
    SFmap hscale_STt_dcsv;
    SFmap hscale_STtw_dcsv;
    SFmap hscale_WJets_dcsv;   

    TH2F* hscale_tttt_djet;
    TH2F* hscale_ttjj_djet;
    TH2F* hscale_ttbb_djet;
    TH2F* hscale_ttcc_djet;
    TH2F* hscale_tt2b_djet;
    TH2F* hscale_tt1b_djet;
    TH2F* hscale_HT500Njet9_ttjj_djet;
    TH2F* hscale_HT500Njet9_ttbb_djet;
    TH2F* hscale_HT500Njet9_ttcc_djet;
    TH2F* hscale_HT500Njet9_tt2b_djet;
    TH2F* hscale_HT500Njet9_tt1b_djet;
    TH2F* hscale_STs_djet;
    TH2F* hscale_STt_djet;
    TH2F* hscale_STtw_djet;
    TH2F* hscale_WJets_djet;

};


#endif

