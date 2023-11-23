import glob, re

data_dir = "/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/merged_sl/"
sub_dirs = glob.glob("/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/merged_sl/G[0-9][0-9]S[0-9][0-9]_merged.nii.gz")
sub_dirs.sort()

f = open("sub_dir_list.txt", "a")

for sub in list(sub_dirs):
    
    # gets each subject number and presents it to the sub_num_list.txt
    line = re.findall('G[0-9][0-9]S[0-9][0-9]', sub)[0]
    f.write(line)
    
f.close()
