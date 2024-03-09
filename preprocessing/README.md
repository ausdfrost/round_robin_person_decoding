# Preprocessing
## Data Overview
The dataset (to be published at a later date) consisted of Functional magnetic resonance imaging (fMRI) brain scans 20 groups of 6 subjects (114 subjects total) collected by our lab. Each subject contains 5 runs, where in each run they are thinking about randomized members of their group. For each brain scan, there roughly are 250,000 voxels, or data points, so we are working with a massive 142,500,000 data points across the 5 runs per 114 subjects.

The CSNL Round Robin brain image dataset was originally in DICOM format, which is a standard format for medical images such as fMRI (which this data is). We wanted to convert it to a more research friendly and standardized format known as BIDS, which is compatable with many research analysis libraries.

## Preprocessing methods
Here is how I preprocessed the data:

1. Convert DICOM data to BIDS format [(~/conversion)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/conversion)
2. Clean-up BIDS data [(~/cleanup)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/cleanup)
3. Finish preprocessing BIDS data in fMRIPrep [(~/fmriprep)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/fmriprep)
4. Registering subject data run by run to first run (to create similar masks) [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
5. Merging zstat files [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)

After these preprocessing steps, our research data is now ready to be used in a variety of analysis methods.

[BIDS (brain imaging data structure) tools](https://bids.neuroimaging.io/benefits) were leveraged to convert the brain images into a standard and shareable format.

- - - -

A project by Aussie Frost supervised by Taylor Guthrie.
* Started: 2022/06/01
* Finished: 2022/11/01 -> 2023/05/20
