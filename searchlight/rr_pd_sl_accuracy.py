# round robin person decoding classification searchlight analysis
# this script runs on all subjects by using the 'rr_pd_sl_batch.py' script in this dir
# created by Aussie Frost on 02/14/2023 and based on the BrainIAK pipeline
# deployed on 07/05/2023

# Import libraries
import os, sys, glob, re
import pandas as pd
import nibabel as nib
import numpy as np 
import time
from nilearn import plotting
from brainiak.searchlight.searchlight import Searchlight
from brainiak.fcma.preprocessing import prepare_searchlight_mvpa_data
from brainiak import io
from pathlib import Path
from shutil import copyfile

# Import machine learning libraries
from sklearn.model_selection import StratifiedKFold, GridSearchCV, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import PredefinedSplit
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
import sklearn.metrics as skm
from scipy.stats import zscore
from nilearn.masking import compute_epi_mask
from mpi4py import MPI

# Define helper function
def load_epi_data(subject_name):
    # Load MRI file (in Nifti format) of one localizer run
    epi_in = os.path.join(data_dir, "%s_merged.nii.gz" % (subject_name))
    epi_data = nib.load(epi_in)
    print("Loading data from %s" % (epi_in))
    return epi_data

# Define data paths
data_dir = "/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/merged_sl/"
results_dir = "/projects/csnl/shared/round_robin_qc/analysis/braniak_tutorials/output/"
#sub_dirs = glob.glob("/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/merged_sl/G[0-9][0-9]S[0-9][0-9]_merged.nii.gz")
#sub_dirs.sort()

# define sub path from batch file
sub = sys.argv[1]

# Define general subject info
subject_name = re.findall('G[0-9][0-9]S[0-9][0-9]', sub)[0]
n_runs = 5
print(subject_name)

# Define mask path
mask_dir = "/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/sub-%s/model/runA.feat/" % (subject_name)

# Load niftis
epi_in = os.path.join(data_dir, "%s_merged.nii.gz" % (subject_name))
bold_data = nib.load(epi_in)
mask_in = os.path.join(mask_dir, "mask.nii.gz")
mask = nib.load(mask_in)

# Load onsets
onsets = pd.read_csv("/projects/csnl/shared/round_robin_qc/analysis/no_st_qc/sl_train_G01S01.csv")
onsets = onsets.values

# Load run_ids
run_ids = onsets[:,2] - 1
print(run_ids)

# Pull out the MPI information
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

# Output data path TODO ensure doing per subject output
output_path = os.path.join(results_dir,'searchlight_results')
if rank == 0:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        
# Define our mask
mask = mask.get_fdata()
coords = np.where(mask)

# Load the data in rank 0
if rank == 0:
    # Make a function to load the data for one subject's merge file
    def load_data(mask_in, subject_name):
        epi_data = load_epi_data(subject_name)
        print(("Finished load sub %s" % (subject_name)))
        bold_data = epi_data.get_data()
        print(("Finished getdata sub %s" % (subject_name)))
        print(bold_data.shape)
        affine_mat = epi_data.affine
        print(("Finished affine sub %s" % (subject_name)))
        dimsize = epi_data.header.get_zooms()
        print(("Finished dim sub %s" % (subject_name)))
        return bold_data, affine_mat, dimsize
    
    # Use load_data to write to data   
    data, affine_mat, dimsize = load_data(epi_in, subject_name)
    print(data.shape)
    print(mask.shape)
    # extract bold data for non-zero labels
    #data = data[:, :, :, label_index]
else:
    data = None
    
# Load targets (each subject target)
labels = onsets[:,1] - 1

# Split data according to run ids
ps = PredefinedSplit(run_ids)

# Save them as the broadcast variables
bcvar = [labels, ps]

# Preset the variables to be used in the searchlight
data = data
mask = mask
bcvar = bcvar
sl_rad = 1 # (in mm)
max_blk_edge = 5
pool_size = 1

# Start the clock to time searchlight
begin_time = time.time()

# Create the searchlight object
sl = Searchlight(sl_rad=sl_rad,max_blk_edge=max_blk_edge)
print("Setup searchlight inputs")
print("Input data shape: " + str(data.shape))
print("Input mask shape: " + str(mask.shape) + "\n")

# Distribute the information to the searchlights (preparing it to run)
sl.distribute([data], mask)

# Broadcast variables
sl.broadcast(bcvar)

# Set up the kernel function, in this case an SVM (use linear SVM , LORO)
def calc_svm(data, sl_mask, myrad, bcvar):
    if np.sum(sl_mask) < 14:
        return -1
    scores = []
    labels, ps = bcvar[0], bcvar[1]

    # Reshape the data
    sl_num_vx = sl_mask.shape[0] * sl_mask.shape[1] * sl_mask.shape[2]
    num_epoch = data[0].shape[3]
    data_sl = data[0].reshape(sl_num_vx, num_epoch).T
    
    # Classifier: loop over all runs to leave each run out once
    model = LinearSVC()
    for train_index, test_index in ps.split():
        X_train, X_test = data_sl[train_index], data_sl[test_index]
        y_train, y_test = labels[train_index], labels[test_index]
        # Fit a svm
        model.fit(X_train, y_train)
        # Calculate the accuracy for the hold out run
        score = model.score(X_test, y_test)
        scores.append(score)
        
    return np.mean(scores)

# Run the searchlight analysis
print("Begin SearchLight in rank %s\n" % rank)
sl_result = sl.run_searchlight(calc_svm, pool_size=pool_size)
print("End SearchLight in rank %s\n" % rank)

# Only save the data if this is the first core
if rank == 0:
    # Convert NaN to 0 in the output
    sl_result = np.nan_to_num(sl_result[mask==1])
    # Reshape
    result_vol = np.zeros((mask.shape[0], mask.shape[1], mask.shape[2]))  
    result_vol[coords[0], coords[1], coords[2]] = sl_result   
    # Convert the output into what can be used
    result_vol = result_vol.astype('double')   
    # Save the average result
    output_name = os.path.join(output_path, '%s_SL_accuracy.nii.gz' % (subject_name))
    sl_nii = nib.Nifti1Image(result_vol, affine_mat)
    hdr = sl_nii.header
    hdr.set_zooms((dimsize[0], dimsize[1], dimsize[2]))
    nib.save(sl_nii, output_name)  # Save    
    
    print('Finished searchlight')
    end_time = time.time()
    print('Total searchlight duration (including start up time): %.2f' % (end_time - begin_time))

# Submit this file as a job to the supercomputer via 'rr_pd_sl_batch.sh'
