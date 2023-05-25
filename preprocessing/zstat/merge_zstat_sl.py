import os
import glob
import subprocess
import re
import numpy as np

# a modified script for the round robin searchlight analysis
# originally by Taylor Guthrie, heavily modified by Aussie Frost
# deployed by Aussie Frost on 5/23/2023

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
    sub_targets = np.empty(0)
 
    for run in list(run_dirs):
	# get all zstat paths and store them
        zstat_dirs = glob.glob('%s/stats/zstat[1-6]-registered.nii.gz'%(run))
        zstat_dirs = np.array(zstat_dirs)
        zstat_dirs.sort()

	# exclude subjects own zstat
	#sub_index = int(subnum[5])-1
	#zstat_dirs = np.delete(zstat_dirs, sub_index)	
	
	# append to sub_targets
	sub_targets = np.append(sub_targets, zstat_dirs)
	
    # testing
    #print(subnum)
    
    # assign to variables (tedious)
    #sub_targets = np.delete(sub_targets, 0)
    print(sub_targets)
    
    runA_tar1 = sub_targets[0]
    runA_tar2 = sub_targets[1]
    runA_tar3 = sub_targets[2]
    runA_tar4 = sub_targets[3]
    runA_tar5 = sub_targets[4]

    runB_tar1 = sub_targets[5]
    runB_tar2 = sub_targets[6]
    runB_tar3 = sub_targets[7]
    runB_tar4 = sub_targets[8]
    runB_tar5 = sub_targets[9]

    runC_tar1 = sub_targets[10]
    runC_tar2 = sub_targets[11]
    runC_tar3 = sub_targets[12]
    runC_tar4 = sub_targets[13]
    runC_tar5 = sub_targets[14]

    runD_tar1 = sub_targets[15]
    runD_tar2 = sub_targets[16]
    runD_tar3 = sub_targets[17]
    runD_tar4 = sub_targets[18]
    runD_tar5 = sub_targets[19]

    runE_tar1 = sub_targets[20]
    runE_tar2 = sub_targets[21]
    runE_tar3 = sub_targets[22]
    runE_tar4 = sub_targets[23]
    runE_tar5 = sub_targets[24]
	
    # var assn verification
    #print(runA_tar1, runA_tar2, runA_tar3, runA_tar4, runA_tar5, runB_tar1, runB_tar2, runB_tar3, runB_tar4, runB_tar5, runC_tar1, runC_tar2, runC_tar3, runC_tar4, runC_tar5, runD_tar1, runD_tar2, runD_tar3, runD_tar4, runD_tar5, runE_tar1, runE_tar2, runE_tar3, runE_tar4, runE_tar5)

    #runA_tar1, runA_tar2, runA_tar3, runA_tar4, runA_tar5, runB_tar1, runB_tar2, runB_tar3, runB_tar4, runB_tar5, runC_tar1, runC_tar2, runC_tar3, runC_tar4, runC_tar5, runD_tar1, runD_tar2, runD_tar3, runD_tar4, runD_tar5, runE_tar1, runE_tar2, runE_tar3, runE_tar4, runE_tar5)

    # send to fsl
    print(subnum)
    merge_command = 'fslmerge -t %s/merged_sl/%s_merged %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s'%(analysis_dir, subnum, runA_tar1, runA_tar2, runA_tar3, runA_tar4, runA_tar5, runB_tar1, runB_tar2, runB_tar3, runB_tar4, runB_tar5, runC_tar1, runC_tar2, runC_tar3, runC_tar4, runC_tar5, runD_tar1, runD_tar2, runD_tar3, runD_tar4, runD_tar5, runE_tar1, runE_tar2, runE_tar3, runE_tar4, runE_tar5)
    print(merge_command)
    with open('srun_sl/%s.srun'%(subnum), 'w') as file:
        slurm = '#!/bin/bash\n#SBATCH --job-name=merge \n#SBATCH --partition=short\n#SBATCH --nodes=1\n#SBATCH --ntasks=1\n#SBATCH --mem=4G\n#SBATCH --output=merge_%s.out\n#SBATCH --error=merge_%s.err\n\nmodule load fsl/6.0.1\n\n%s'%(subnum,subnum,merge_command)
        file.write(slurm)
    os.system('sbatch -A csnl srun_sl/%s.srun'%(subnum))
