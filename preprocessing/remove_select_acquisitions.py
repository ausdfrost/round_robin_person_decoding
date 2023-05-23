import os
import glob
import subprocess
import numpy as np 
import re

beh_dir = '/Users/chavezlabadmin/Desktop/bidsWorkshop/behavioral'
bids_dir = '/Users/chavezlabadmin/Desktop/bidsWorkshop/batch_data'

run_files = glob.glob('%s/group_[0-9][0-9]/G[0-9][0-9]_S[0-9][0-9]/experiment_setup/run_order.txt'%(beh_dir))
run_files = np.array(run_files)
run_files.sort()

for f in run_files:
    run_order = [line.rstrip('\r\n') for line in open(f)]
    run_order = run_order[1:6]
    sub = 'sub-' + re.findall('G[0-9][0-9]', f)[0] + re.findall('S[0-9][0-9]', f)[0]
    func_niftis = glob.glob('%s/%s/ses-wave1/func/%s_ses-wave1_task-RR_acq-[1-5]_bold.nii.gz'%(bids_dir, sub, sub))
    func_niftis = np.array(func_niftis)
    func_niftis.sort()
    for i,j in enumerate(func_niftis, 0):
        os.remove(j)
    func_jsons = glob.glob('%s/%s/ses-wave1/func/%s_ses-wave1_task-RR_acq-[1-5]_bold.json'%(bids_dir, sub, sub))
    func_jsons = np.array(func_jsons)
    func_jsons.sort()
    for i,j in enumerate(func_jsons, 0):
        os.remove(j)
