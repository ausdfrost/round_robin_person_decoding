#!/bin/bash
#
# This batch file calls on your subject
# list (named subject_list.txt). And 
# runs the rr_pd_sl_batch.py file for 
# each subject.
#

# Set your directories
group_dir='~/round_robin_brainiak'
study=round_robin_sl

# Set subject list
sublist=`cat sub_dir_list_endorsement_no.txt`

# Submit fmriprep jobs for each subject
for sub in ${sublist}; do

SUBID=`echo $sub|awk '{print $1}' FS=,`
SESSID=`echo $sub|awk '{print $2}' FS=,`

sbatch --export ALL,subid=${sub},group_dir=${group_dir},study=${study} \
    --job-name fmriprep \
    --partition=longfat \
    --mem=100G \
    --account=csnl \
    python rr_pd_sl_accuracy.py ${sub} &
done