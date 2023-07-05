# Preprocessing

Here is how I preprocessed the data:

1. Convert DICOM data to BIDS format [(~/conversion)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/conversion)
2. Clean-up BIDS data [(~/cleanup)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/cleanup)
3. Finish preprocessing BIDS data in fMRIPrep [(~/fmriprep)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/fmriprep)
4. Registering subject data run by run to first run (to create similar masks) [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)
5. Merging zstat files [(~/zstat)](https://github.com/austinfroste/round_robin_person_decoding/tree/main/preprocessing/zstat)

- - - -

Data is now ready to use!

A project by Aussie Frost supervised by Taylor Guthrie.
* Started: 2022/06/01
* Finished: 2022/11/01 -> 2023/05/20
