import os
import glob
import subprocess
import re
import numpy as np

os.system('module load fsl/6.0.1')

# a modified script for the round robin searchlight analysis
# written by Aussie Frost
# to register zstat files to their respective run matrixes
# executed by Aussie Frost on 05/19/2023

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

    for i, run in enumerate(list(run_dirs)):

	# define run to register to
        runA_dir = run_dirs[0]
        	
	# get all zstat paths and store them
        zstat_dirs = glob.glob('%s/stats/zstat[1-6].nii.gz'%(run))
        zstat_dirs = np.array(zstat_dirs)
	zstat_dirs.sort()
	
	# exclude subjects own zstat
	sub_index = int(subnum[5])-1
	zstat_dirs = np.delete(zstat_dirs, sub_index)
		
        # get all matrixes and store them
	matrix_dirs = glob.glob('%s/model/runA.feat/matrix/[B-E]toA.mat'%(sub))
	matrix_dirs.sort()

	# perform registrations	
        if run == runA_dir:
	    print(run)
            # make copy of zstat file such that they match registered format
	    for stat in zstat_dirs:

		# find and replace such to append -registered 
		substr = '.nii.gz'
		insertstr = '-registered'
		stat_split = stat.split(substr)
		stat_formatted = stat_split[0] + insertstr + substr
		
		# create copy of stat DONE
	    	#os.system('cp %s %s'%(stat, stat_formatted))

	# register zstat[n] to respective run matrix and save output as zstat[n]-registered (in same directory as original zstat
	else:

	    # for each zstat, register to runA
	    for stat in zstat_dirs:
	    # append -registered to zstat name
   	        substr = '.nii.gz'
		insertstr = '-registered'
	 	stat_split = stat.split(substr)
		stat_formatted = stat_split[0] + insertstr + substr
	        #output = ('%s/stats/%s'%(run, stat_formatted))
		output = stat_formatted
   		    	
		# prepare flirt command
		ref = run_dirs[0] + '/mean_func.nii.gz'
		matrix = matrix_dirs[i-1]
		print('begin registration')
		print(stat)
		print(ref)
		print(output)
	       	print(matrix)
	        os.system('flirt -in %s -ref %s -out %s -init %s -applyxfm'%(stat, ref, output, matrix))
		print('finished flirt for %s'%(sub))

