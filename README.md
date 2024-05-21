# Round Robin Person Decoding
My contributions to the CSNL Round Robin Person Decoding analysis, a large project that occupied my third year at the University of Oregon. The analysis publication is titled as 'Decoding Person Identity of Known Others' and is currently in review.

## directory structure
There are preprocessing and analysis pipelines for the study:

1. Preprocessing [(~/preprocessing)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing)
    1. Convert DICOM data to BIDS format [(~/conversion)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/conversion)
    2. Clean-up BIDS data [(~/cleanup)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/cleanup)
    3. Finish preprocessing BIDS data in fMRIPrep [(~/fmriprep)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/fmriprep)
    4. Registering subject data run by run to first run (to create similar masks) [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
    5. Merging zstat files [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
2. Classification Searchlight Analysis Pipeline [(~/searchlight_pipeline)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/searchlight_pipeline)
    1. Jupyter notebook(s) for building and testing the pipeline on a single subject
    2. Run various 'rr_pd_sl_[...].py' for desired initial_accuracy, endorsement_no, endorsement_yes

## outline
We wish to predict who in a group of 6 acquanted individuals a respective person in the group is thinking of by running a multi-voxel pattern analysis (MVPA). This analysis consisted of a SKLearn-based SVM classification deployed on each voxel, or datapoint, in the brain on all subjects in the study. We have 20 groups of 6 individuals that we ran this analysis on.

## data
The dataset (to be published at a later date) consisted of Functional magnetic resonance imaging (fMRI) brain scans 20 groups of 6 subjects (114 subjects total) collected by our lab. Each subject contains 5 runs, where in each run they are thinking about randomized members of their group. For each brain scan, there roughly are 250,000 voxels, or data points, so we are working with a massive 142,500,000 data points across the 5 runs per 114 subjects.

## model 
The model is built using Sci-Kit Learn's `sklearn.svm.LinearSVC()` SVM classifier and BrainIAK's Searchlight Classification analysis framework to deploy it on the brain data. Leave one run out cross validation was utilized such that our classifications would hold little bias, and we could perform classifications on a very large dataset. A multi-class classification model was used since the data is labeled for which of 5 other subjects a person is (presumably) thinking of at the given moment in the time series. Performing these comptations across all of our data was very computationally expensive, and thus the analysis was deployed in parallel on the university's supercomputer. Various Jupyter notebooks can be found [here](searchlight_pipeline/exploration) demonstrating some of my process to building our model from the BrainIAK framework. Metrics of accuracy, sensitivity, and specificity were generated to evaluate the model performance.

## results
The model was able to successfuly predict who someone is thinking about above chance by running a classification model on their whole brain. We concluded that representations of individuals are distinct to locations in the brain, and that we can look at brain images and decode who someone is thinking about at a given point.

## publications
* Decoding Person Identity of Known Others - *TD Guthrie, AD Frost, RS Chavez*

* Round Robin Data Paper (In Review) - *TD Guthrie, AD Frost, RS Chavez*

- - - -
A project for Dr. Robert Chavez's Computational Social Neuroscience Lab [(CSNL)](https://csnl.uoregon.edu/) at the University of Oregon. <br />
Code by Aussie Frost, supervised by Taylor Guthrie. <br />
Using the [BrainIAK framework](https://github.com/brainiak/brainiak), an open-source brain analysis package.

* Started: 2022/08/01 (preprocessing) -> 2023/03/20 (analysis)
* Finished: 2022/11/01 (preprocessing) -> 2023/09/06 (analysis pass1) -> 2023/11/22 (analysis pass2)

> TODO: finish code annotation, publish finalized code, revise organisation, update readme, inform on endorsement_no/yes
