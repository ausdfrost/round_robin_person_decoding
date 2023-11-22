# round_robin_person_decoding
My contributions to the CSNL Round Robin Person Decoding analysis, a large project that occupied my third year at the University of Oregon. The publication is slated as 'Person Decoding Classification Searchlight Analysis' and is currently in review.

## publication
Person Decoding Classification Searchlight Analysis (*In Review, working title*)
* TD Guthrie, AD Frost, RS Chavez

Round Robin Data Paper (*In Review, working title*)
* TD Guthrie, AD Frost, RS Chavez

## directory structure
There are preprocessing and analysis pipelines for the study:

1. Preprocessing [(~/preprocessing)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing)
    1. Convert DICOM data to BIDS format [(~/conversion)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/conversion)
    2. Clean-up BIDS data [(~/cleanup)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/cleanup)
    3. Finish preprocessing BIDS data in fMRIPrep [(~/fmriprep)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/fmriprep)
    4. Registering subject data run by run to first run (to create similar masks) [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
    5. Merging zstat files [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
2. Classification Searchlight Analysis Pipeline [(~/searchlight)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/searchlight)
    1. Jupyter notebook(s) for building and testing the pipeline on a single subject
    2. Run various 'rr_pd_sl_[...].py' for various classifier metrics (accuracy, sensitivity, specificity)

## model
We wish to predict who in a group of 6 acquanted individuals a respective person in the group is thinking of by running a searchlight classification analysis on all subjects in the study. We have 20 groups of 6 individuals that we ran this analysis on.

## data
The dataset (to be published at a later date) consisted of Functional magnetic resonance imaging (fMRI) brain scans 20 groups of 6 subjects (114 subjects total) collected by our lab. Each subject contains 5 runs, where in each run they are thinking about randomized members of their group.

## result
I was able to build a successful predictive model that decoded (above chance) who in a group of 6 acquanted individuals a respective person in the group is thinking of.

- - - -
A project for Dr. Robert Chavez's Computational Social Neuroscience Lab [(CSNL)](https://csnl.uoregon.edu/) at the University of Oregon. <br />
Code by Aussie Frost, supervised by Taylor Guthrie. <br />
Using the [BrainIAK framework](https://github.com/brainiak/brainiak), an open-source brain analysis package.

* Started: 2022/08/01 (preprocessing) -> 2023/03/20 (analysis)
* Finished: 2022/11/01 (preprocessing) -> 2023/09/06 (analysis pass1) -> 2023/11/22 (analysis pass2)

> TODO: finish code annotation, publish finalized code, revise organisation, update readme
