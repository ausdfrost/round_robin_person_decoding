import os, re, glob

# This batch script was created by Aussie Frost on 7/5/2023
# to deploy my round robin personal decoding searchlight on all subjects

# Set your directories
sub_dirs = glob.glob("/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/merged_sl/G[0-9][0-9]S[0-9][0-9]_merged.nii.gz")
sub_dirs.sort()

# Submit fmriprep jobs for each subject
for sub in sub_dirs:
    subnum = re.findall('G[0-9][0-9]S[0-9][0-9]', sub)[0]
    sl_command = 'python rr_pd_sl_accuracy.py %s'%(sub)
    print(sub)
    print(subnum)
    print(sl_command)

    with open('srun_sl/%s.srun'%(subnum), 'w') as file:
        slurm = '#!/bin/bash\n#SBATCH --job-name=%s_rr_searchlight\n#SBATCH --partition=longfat\n#SBATCH --mem=100G\n\n module load python\n %s'%(subnum, sl_command)
        file.write(slurm)
    os.system('sbatch -A csnl srun_sl/%s.srun'%(subnum))