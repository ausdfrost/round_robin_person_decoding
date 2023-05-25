import os
import glob
import subprocess
import re
import numpy as np

os.system('module load fsl/6.0.1')

# a script for the round robin searchlight analysis
# to create matrix files for each subject
# deployed by Aussie Frost on 05/10/2023

analysis_dir = '/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/'

sub_dirs = glob.glob('%s/sub-G[0-9][0-9]S0[0-9]'%(analysis_dir))
sub_dirs.sort()

# exclude subjects (if any)
#print(sub_dirs[30])
sub_dirs = np.delete(sub_dirs, 30)

for sub in list(sub_dirs):
    run_dirs = glob.glob('%s/model/run[A-E].feat'%(sub))
    run_dirs.sort()
    subnum = re.findall('sub-(G[0-9][0-9]S[0-9][0-9])', sub)[0] 

    for run in list(run_dirs):
        runA_dir = run_dirs[0]
	os.system('mkdir %s/matrix'%(runA_dir))
        if run == runA_dir:
	    print(run) 
        elif run == run_dirs[1]:
            # create matrix files for [B-E]toA.mat
 	    runs_to_merge = np.delete(run_dirs, 0)
	    for runs in runs_to_merge:
                run_num = re.findall('[B-E]', runs)[0]
		os.system('flirt -in %s/mean_func.nii.gz -ref %s/mean_func.nii.gz -omat %s/matrix/%stoA.mat -dof 6'%(runs, runA_dir, runA_dir, run_num)) 
		print('finished flirt for %s %s'%(sub, run_num))
