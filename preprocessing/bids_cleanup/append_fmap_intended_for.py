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
    # open ap
    fmap_jsons = glob.glob('%s/%s/ses-wave1/fmap/%s_ses-wave1_dir-ap_epi.json'%(bids_dir, sub, sub))
    fmap_jsons = np.array(fmap_jsons)
    fmap_jsons.sort()
    for i, j in enumerate(fmap_jsons, 0):
        # open rr file for file in files
        file = open(j, 'r+')
        # append fmap intendedfor
        lines = file.readlines()
        for k, line in enumerate(lines):
            if line.startswith('    "Dcm2bidsVersion": "2.1.7"'):
                lines[k] = '    ' + lines[k].strip() + ',\n    \"IntendedFor\": [\n' + '        \"ses-wave1/func/%s_ses-wave1_task-loc_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-A_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-B_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-C_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-D_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-E_bold.nii.gz\"\n'%(sub) + '    ]\n'
        file.seek(0)
        for line in lines:
            file.write(line)
    # open pa
    fmap_jsons = glob.glob('%s/%s/ses-wave1/fmap/%s_ses-wave1_dir-pa_epi.json'%(bids_dir, sub, sub))
    fmap_jsons = np.array(fmap_jsons)
    fmap_jsons.sort()
    for i, j in enumerate(fmap_jsons, 0):
        # open rr file for file in files
        file = open(j, 'r+')
        # append fmap intendedfor
        lines = file.readlines()
        for k, line in enumerate(lines):
            if line.startswith('    "Dcm2bidsVersion": "2.1.7"'):
                lines[k] = '    ' + lines[k].strip() + ',\n    \"IntendedFor\": [\n' + '        \"ses-wave1/func/%s_ses-wave1_task-loc_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-A_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-B_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-C_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-D_bold.nii.gz\",\n'%(sub) + '        \"ses-wave1/func/%s_ses-wave1_task-RR_acq-E_bold.nii.gz\"\n'%(sub) + '    ]\n'
        file.seek(0)
        for line in lines:
            file.write(line)
