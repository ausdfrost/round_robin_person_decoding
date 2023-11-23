import glob

data_dir = "/projects/csnl/shared/round_robin_qc/analysis/endorsement/merged_sl/yes"
sub_dirs = glob.glob("/projects/csnl/shared/round_robin_qc/analysis/endorsement/merged_sl/yes/G[0-9][0-9]S[0-9][0-9]_merged.nii.gz")
sub_dirs.sort()

f = open("sub_dir_list_endorsement_yes.txt", "a")

for sub in list(sub_dirs):
    
    # gets each subject directory and presents it to the sub_dir_list.txt
    line = '%s\n'%(sub)
    f.write(line)
    
f.close()