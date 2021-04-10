#!/usr/bin/python

import os,sys,pickle

shift = sys.argv[1]
inputDir = '/uscms_data/d3/ssagir/FWLJMET102X_1lep2017_Oct2019_4t_032721_step1hadds/'+shift+'/'
resubmit_err = False
resubmit_out = False
resubmit_fail = False
resubmit_running = False  # Make sure you know what you are doing with this option!
resubmit = False

N_totjobs = 0
N_running = 0
N_err  = 0
N_out  = 0
N_fail = 0

samples = [x[:-4] for x in os.listdir(inputDir) if '.job' in x]
for sample in samples:
	N_totjobs+=1
	jFile = inputDir+'/'+sample+'.job'
	lFile = inputDir+'/'+sample+'.log'
	eFile = inputDir+'/'+sample+'.err'
	oFile = inputDir+'/'+sample+'.out'

	isOutFileExist = False
	isOutFileOK = False
	isErrFileExist = False
	isThereError = False
	isLogFileExist = False
	isJobDone = False
	isJobFailed = False

	if os.path.exists(oFile): isLogFileExist = True
	if isLogFileExist: 
		logFdata = open(lFile).read()
		if 'Normal termination' in logFdata: 
			isJobDone = True
			if 'Normal termination (return value 0)' not in logFdata: isJobFailed = True
		
	if os.path.exists(oFile): isOutFileExist = True
	if isOutFileExist: 
		outFdata = open(oFile).read()
		if 'Error' not in outFdata and 'error' not in outFdata and 'Fatal' not in outFdata and 'fatal' not in outFdata: isOutFileOK = True

	if os.path.exists(eFile): isErrFileExist = True
	if isErrFileExist: 
		errFdata = open(eFile,'r').read()
		errFlines = errFdata.split('\n')
		for errline in errFlines:
			if 'error' in errFdata or 'Error' in errFdata: isThereError = True
			if 'Error in <TNetXNGFile::Close>: [ERROR] Socket error' in errFdata: isThereError = False
		statement33 = "Permission denied" in errFdata
	statement = isOutFileExist and isOutFileOK
	statement = statement and isErrFileExist and not isThereError 
	statement = statement and isLogFileExist and isJobDone and not isJobFailed
	if not statement or statement33:
		print "        FILE:",sample
		if not (isLogFileExist and isJobDone):
			print "              --Job still running!"
			N_running+=1
			if resubmit_running:
				print "                RESUBMITTING ..."
				os.chdir(inputDir)
				os.system('rm ' + lFile)
				os.system('rm ' + eFile)
				os.system('rm ' + oFile)
				os.system('condor_submit ' + jFile)
		elif isJobFailed:
			print "              --Job failed!"
			N_fail+=1
			if resubmit or resubmit_fail:
				print "                RESUBMITTING ..."
				os.chdir(inputDir)
				os.system('rm ' + lFile)
				os.system('rm ' + eFile)
				os.system('rm ' + oFile)
				os.system('condor_submit ' + jFile)
		elif not (isOutFileExist and isOutFileOK):
			print "              --Problem in out file!"
			N_out+=1
			if resubmit or resubmit_out:
				print "                RESUBMITTING ..."
				os.chdir(inputDir)
				os.system('rm ' + lFile)
				os.system('rm ' + eFile)
				os.system('rm ' + oFile)
				os.system('condor_submit ' + jFile)
		elif not (isErrFileExist and not isThereError):
			print "              --There is error!"
			N_err+=1
			if resubmit or resubmit_err:
				print "                RESUBMITTING ..."
				os.chdir(inputDir)
				os.system('rm ' + lFile)
				os.system('rm ' + eFile)
				os.system('rm ' + oFile)
				os.system('condor_submit ' + jFile)

print N_running, "jobs are still running!"
print N_err, "jobs have error in .err file!"
print N_out, "jobs have error in .out file!"
print N_fail, "jobs failed!"
print N_running+N_err+N_out+N_fail,"/",N_totjobs, "jobs resubmitted in total!"

