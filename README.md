# round_robin_person_decoding
My contributions to the CSNL Round Robin Person Decoding analysis, a large project that occupied my third year at the University of Oregon.

## The directory structure
There are preprocessing and analysis pipelines for the study:

1. Preprocessing [(~/preprocessing)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing)
    1. Convert DICOM data to BIDS format [(~/conversion)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/conversion)
    2. Clean-up BIDS data [(~/cleanup)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/cleanup)
    3. Finish preprocessing BIDS data in fMRIPrep [(~/fmriprep)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/fmriprep)
    4. Registering subject data run by run to first run (to create similar masks) [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
    5. Merging zstat files [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
2. Analysis [(~/searchlight)]()

## The study

Some info about the study...

- - - -
A project for Dr. Robert Chavez's Computational Social Neuroscience Lab at the University of Oregon. <br />
Code by Aussie Frost, supervised by Taylor Guthrie. <br />
Using the [BrainIAK framework](https://github.com/brainiak/brainiak), an open-source brain analysis package.

* Started: 2022/08/01 (preprocessing) -> 2023/03/20 (analysis)
* Finished: 2022/11/01 (preprocessing) -> 2023/??/?? (analysis)
