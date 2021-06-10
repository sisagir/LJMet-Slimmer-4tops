import os,shutil,datetime,time,subprocess,math,getpass
from ROOT import *
execfile("/uscms_data/d3/jmanagan/EOSSafeUtils.py")

start_time = time.time()

#IO directories must be full paths
shift = sys.argv[1]
Year = 2018
inputDir='/eos/uscms/store/user/ssagir/FWLJMET102X_1lep'+str(Year)+'_Oct2019_4t_032721_step1/'+shift+'/'
outputDir='/eos/uscms/store/user/ssagir/FWLJMET102X_1lep'+str(Year)+'_Oct2019_4t_032721_step1hadds/'+shift+'/'
condorDir='/uscms_data/d3/ssagir/FWLJMET102X_1lep'+str(Year)+'_Oct2019_4t_032721_step1hadds/'+shift+'/'
inDir=inputDir[10:]
outDir=outputDir[10:]
runDir=os.getcwd()

os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outDir)

dirList16 = [
'DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTHH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTTJ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_correctnPartonsInBorn',
'TTTW_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTWH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
'TTWW_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTWZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTZH_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
'TTZToLL_M-1to10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'TTZZ_TuneCUETP8M2T4_13TeV-madgraph-pythia8',
'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
'WW_TuneCUETP8M1_13TeV-pythia8',
'WZ_TuneCUETP8M1_13TeV-pythia8',
'ZZ_TuneCUETP8M1_13TeV-pythia8',
'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8',
'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8',
]

dirList17 = [
'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
'ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia',
'ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia',
'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTHH_TuneCP5_13TeV-madgraph-pythia8',
'TTTJ_TuneCP5_13TeV-madgraph-pythia8',
'TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_correctnPartonsInBorn',
'TTTW_TuneCP5_13TeV-madgraph-pythia8',
'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TTWH_TuneCP5_13TeV-madgraph-pythia8',
'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
'TTWW_TuneCP5_13TeV-madgraph-pythia8',
'TTWZ_TuneCP5_13TeV-madgraph-pythia8',
'TTZH_TuneCP5_13TeV-madgraph-pythia8',
'TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8',
'TTZZ_TuneCP5_13TeV-madgraph-pythia8',
'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'WW_TuneCP5_13TeV-pythia8',
'WZ_TuneCP5_13TeV-pythia8',
'ZZ_TuneCP5_13TeV-pythia8',
'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8',
'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8',
]

dirList18 = [
'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8',
'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8',
'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',
'TTHH_TuneCP5_13TeV-madgraph-pythia8',
'TTTJ_TuneCP5_13TeV-madgraph-pythia8',
'TTTT_TuneCP5_13TeV-amcatnlo-pythia8',
'TTTT_TuneCP5_13TeV-amcatnlo-pythia8_ext',
'TTTW_TuneCP5_13TeV-madgraph-pythia8',
'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
'TTToSemiLepton_HT500Njet9_TuneCP5_13TeV-powheg-pythia8',
'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
'TTWH_TuneCP5_13TeV-madgraph-pythia8', 
'TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
'TTWW_TuneCP5_13TeV-madgraph-pythia8',
'TTWZ_TuneCP5_13TeV-madgraph-pythia8',
'TTZH_TuneCP5_13TeV-madgraph-pythia8',
'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8',
'TTZZ_TuneCP5_13TeV-madgraph-pythia8',
'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'WW_TuneCP5_PSweights_13TeV-pythia8',
'WZ_TuneCP5_PSweights_13TeV-pythia8',
'ZZ_TuneCP5_13TeV-pythia8',
'ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8',
'ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8',
]

dirList = dirList16[:]
if Year==2017: dirList = dirList17[:]
if Year==2018: dirList = dirList18[:]

if shift=='nominal' and Year==2016:
	dirList.append('SingleElectron')
	dirList.append('SingleMuon')
	dirList.append('TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
if shift=='nominal' and Year==2017:
	dirList.append('SingleElectron')
	dirList.append('SingleMuon')
	dirList.append('TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8')
if shift=='nominal' and Year==2018:
	dirList.append('EGamma')
	dirList.append('SingleMuon')
	dirList.append('TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampDOWN_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTTo2L2Nu_hdampUP_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5down_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_TuneCP5up_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToHadronic_hdampUP_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5down_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_TuneCP5up_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampDOWN_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLepton_HT500Njet9_hdampUP_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5down_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_TuneCP5up_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampDOWN_TuneCP5_13TeV-powheg-pythia8')
	dirList.append('TTToSemiLeptonic_hdampUP_TuneCP5_13TeV-powheg-pythia8')

count=0
for sample in dirList:
	outList = ['none']
	if 'Tprime' in sample: outList = ['BWBW','TZBW','THBW','TZTH','TZTZ','THTH']
	elif 'Bprime' in sample: outList = ['TWTW','BZTW','BHTW','BZBH','BZBZ','BHBH']
	elif 'TTToSemiLeptonic' in sample: outList = ['HT0Njet0','HT500Njet9']
	#elif 'TTTo' in sample: outList = ['Mtt0to700','Mtt700to1000','Mtt1000toInf']
	#if 'TuneCP5down' in sample or 'TuneCP5up' in sample or 'hdampDOWN' in sample or 'hdampUP' in sample: outList = ['none']
	if 'TTTo' in sample or 'TT_Mtt' in sample: 
		if outList==['none']: outList = ['ttbb','tt2b','tt1b','ttcc','ttjj']
		else:
			outList_ = outList[:]
			outList = []
			for outlabel in outList_:
				for flv in ['ttbb','tt2b','tt1b','ttcc','ttjj']: outList.append(outlabel+'_'+flv)
	
	for outlabel in outList:
		outsample = sample+'_'+outlabel
		if outlabel == 'none': outsample = sample
		os.system('mkdir -p '+condorDir)
		
		rootfiles = EOSlist_root_files(inputDir+'/'+outsample)
		
		print "------------ hadding Sample:",outsample,"---------------"
		print 'N root files in',outsample,'=',len(rootfiles)
		
		nFilesPerHadd = 900
		if 'TTToSemiLeptonic' in outsample and ('Mtt0to700' in outsample or 'HT0Njet0_ttjj' in outsample): nFilesPerHadd = 45
		elif 'WJetsToLNu_HT-1200To2500' in outsample: nFilesPerHadd = 120
		elif 'WJetsToLNu_HT-2500ToInf' in outsample: nFilesPerHadd = 13 
		if 'TuneCP5down' in sample or 'TuneCP5up' in sample or 'hdampDOWN' in sample or 'hdampUP' in sample: nFilesPerHadd = 900       
		onefile = ' root://cmseos.fnal.gov/'+inDir+'/'+outsample+'/'+rootfiles[-1]
		manyfiles = nFilesPerHadd*onefile
		lengthcheck = len('hadd -f root://cmseos.fnal.gov/'+outDir+'/'+outsample+'_hadd.root '+manyfiles)
		if lengthcheck > 126000.:
			toolong = lengthcheck - 126000.
			num2remove = math.ceil(toolong/len(onefile))
			nFilesPerHadd = int(nFilesPerHadd - num2remove)
			print 'Length estimate reduced from',lengthcheck,'by',toolong,'via removing',num2remove,'files for nFilesPerHadd of',nFilesPerHadd
		
		if len(rootfiles) < nFilesPerHadd:
			haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+outsample+'_hadd.root '
			for file in rootfiles:
				haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+outsample+'/'+file
			print 'Length of hadd command =',len(haddcommand)
			dict={'CONDIR':condorDir, 'RUNDIR':runDir, 'INPUTDIR':inputDir, 'OUTPUTDIR':outputDir, 'SAMPLE':outsample}
			shell_name = '%(CONDIR)s/%(SAMPLE)s.sh'%dict
			shell=open(shell_name,'w')
			shell.write(
'#!/bin/bash\n\
source /cvmfs/cms.cern.ch/cmsset_default.sh\n\
export SCRAM_ARCH=slc6_amd64_gcc700\n\
scramv1 project CMSSW CMSSW_10_2_10\n\
cd CMSSW_10_2_10\n\
eval `scramv1 runtime -sh`\n\
cd -\n'+haddcommand+'\n')
			shell.close()
		
			jdfName='%(CONDIR)s/%(SAMPLE)s.job'%dict
			print jdfName
			jdf=open(jdfName,'w')
			jdf.write(
"""use_x509userproxy = true
universe = vanilla
Executable = %(CONDIR)s/%(SAMPLE)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = %(SAMPLE)s.out
Error = %(SAMPLE)s.err
Log = %(SAMPLE)s.log
Notification = Never
Arguments =
	
Queue 1"""%dict)
			jdf.close()
			os.chdir('%s'%(condorDir))
			os.system('condor_submit %(SAMPLE)s.job'%dict)
			os.system('sleep 0.5')
			os.chdir('%s'%(runDir))
			count+=1
			print count, "jobs submitted!!!"
		
		else:
			for i in range(int(math.ceil(len(rootfiles)/float(nFilesPerHadd)))):
				haddcommand = 'hadd -f root://cmseos.fnal.gov/'+outDir+'/'+outsample+'_'+str(i+1)+'_hadd.root '
				
				begin=i*nFilesPerHadd
				end=begin+nFilesPerHadd
				if end > len(rootfiles): end=len(rootfiles)
				print 'begin:',begin,'end:',end
				
				for j in range(begin,end):
					haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+outsample+'/'+rootfiles[j]
				print 'Length of hadd command =',len(haddcommand)
				dict={'CONDIR':condorDir, 'RUNDIR':runDir, 'INPUTDIR':inputDir, 'OUTPUTDIR':outputDir, 'SAMPLE':outsample+'_'+str(i+1)}
				shell_name = '%(CONDIR)s/%(SAMPLE)s.sh'%dict
				shell=open(shell_name,'w')
				shell.write(
'#!/bin/bash\n\
source /cvmfs/cms.cern.ch/cmsset_default.sh\n\
export SCRAM_ARCH=slc6_amd64_gcc700\n\
scramv1 project CMSSW CMSSW_10_2_10\n\
cd CMSSW_10_2_10\n\
eval `scramv1 runtime -sh`\n\
cd -\n'+haddcommand+'\n')
				shell.close()
		
				jdfName='%(CONDIR)s/%(SAMPLE)s.job'%dict
				print jdfName
				jdf=open(jdfName,'w')
				jdf.write(
"""use_x509userproxy = true
universe = vanilla
Executable = %(CONDIR)s/%(SAMPLE)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = %(SAMPLE)s.out
Error = %(SAMPLE)s.err
Log = %(SAMPLE)s.log
Notification = Never
Arguments =

Queue 1"""%dict)
				jdf.close()
				os.chdir('%s'%(condorDir))
				os.system('condor_submit %(SAMPLE)s.job'%dict)
				os.system('sleep 0.5')
				os.chdir('%s'%(runDir))
				count+=1
				print count, "jobs submitted!!!"

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))
