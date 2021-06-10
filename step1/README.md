## Quick Structure Explanation
* `hadd.sh` calls `haddoutput.py` which is newer than  `haddoutputbrux.py`
    * `haddoutput.py` runs hadd for list of files

* `compileStep1.C` loads `step1.cc` and `HardcodedConditions.cc`
* `makeStep1.C` macro for running `step1.cc` event loop for shifts (nominal, JEC/R up/down) and all
    files given as argument
* `makeStep1.sh` shell to actually run `makeStep1.C` with arguments

* `submitSlimmerJobs.sh` runs `submitCondorSlimmerJobs.py` for all the different shifts
*  `runCondorSLimmerJobs.py` creates files to submit to condor and then submits them to HTCondor

*  `submitQsubSlimmerJobs.sh` runs `submitQsubSlimmerJobs.py` for all the different shifts
*  `runQsubSlimmerJobs.py` creates big .txt files with qsub commands to submit to qsub batch system

*  `BtagCSVReshaping.h(cc)` for Btag discriminator reshaping <br/>
    Please download `BTagCalibrationStandalone.h(cpp)` from https://github.com/cms-sw/cmssw/tree/CMSSW_10_0_X/CondTools/BTau/test 

## What to run for :
  ### Run step1 without CMSSW:
   ```
        source /cvmfs/sft.cern.ch/lcg/views/LCG_96/x86_64-centos7-gcc8-opt/setup.csh
        root -l testStep1.C
   ```

  ### Condor (BRU or lxplus or UoB):
   ``` 
        condor_submit <file> 
   ```
   For multiple condor jobsrun `runCondorSlimmerJobs.py`
   To submit all jobs for all the shifts, run:
   ```
        source submitSlimmerJobs
   ```
   
   
  ### Qsub (VUB):
  ```
        qsub -q localgrid -v LIST=of,CMD=line,ARGUMENTS=for <File.sh>
   ```
   `<Files.sh>` sets the environment, copies over the needed files and runs a python script in a
   `$TMPDIR`
   To run many qsub commands run:
    ```
        source   submitQsubSlimmerJobs.sh
    ```
    to produce a txt file and run:
   ```
        bigsubmission fileWithQsubCommands.txt
   ```
  
