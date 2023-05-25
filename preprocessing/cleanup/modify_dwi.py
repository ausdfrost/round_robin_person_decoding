import os
import glob
import subprocess
import numpy as np 
import re
import pathlib

# this script modifies the dwi information

beh_dir = '/Users/chavezlabadmin/Desktop/bidsWorkshop/behavioral'
bids_dir = '/Users/chavezlabadmin/Desktop/bidsWorkshop/batch_data'

run_files = glob.glob('%s/group_[0-9][0-9]/G[0-9][0-9]_S[0-9][0-9]/experiment_setup/run_order.txt'%(beh_dir))
run_files = np.array(run_files)
run_files.sort()

for f in run_files:
    run_order = [line.rstrip('\r\n') for line in open(f)]
    run_order = run_order[1:6]
    sub = 'sub-' + re.findall('G[0-9][0-9]', f)[0] + re.findall('S[0-9][0-9]', f)[0]

    # RL: add '-dir' before RL, find and replace '_MR' with '_dwi'
    dwi_RL = glob.glob('%s/%s/ses-wave1/dwi/%s_ses-wave1_RL_MR.*'%(bids_dir, sub, sub))
    dwi_RL = np.array(dwi_RL)
    dwi_RL.sort()
    for i,j in enumerate(dwi_RL, 0):
        filename_zero = '%s/%s/ses-wave1/dwi/%s_ses-wave1_dir-RL_dwi'%(bids_dir, sub, sub)
        filename_ext = pathlib.Path(j).suffixes
        new_filename = filename_zero + ''.join(filename_ext)
        os.rename(j, new_filename)


    # LR: add '-dir' before LR, find and replace '_MR' with '_dwi'
    dwi_LR = glob.glob('%s/%s/ses-wave1/dwi/%s_ses-wave1_LR_MR.*'%(bids_dir, sub, sub))
    dwi_LR = np.array(dwi_LR)
    dwi_LR.sort()
    for i,j in enumerate(dwi_LR, 0):
        filename_zero = '%s/%s/ses-wave1/dwi/%s_ses-wave1_dir-LR_dwi'%(bids_dir, sub, sub)
        filename_ext = pathlib.Path(j).suffixes
        new_filename = filename_zero + ''.join(filename_ext)
        os.rename(j, new_filename)
