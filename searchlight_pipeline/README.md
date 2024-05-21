# Person Decoding Classification Searchlight Analysis Pipeline

Here is how the analysis pipeline was built and deployed:

1. Utilized [Jupyter notebook(s)](exploration/) for building and testing the pipeline on a single subject
2. Ran ['/deployable/rr_pd_sl_initial_accuracy.py'](deployable/rr_pd_sl_initial_accuracy.py) for single classifier metric, accuracy
3. Ran ['/deployable/rr_pd_sl_endorsement_no.py'](deployable/rr_pd_sl_endorsement_no.py) for single classifier metric accuracy, given endorsement_no
4. Ran ['/deployable/rr_pd_sl_endorsement_yes.py'](deployable/rr_pd_sl_endorsement_yes.py) for single classifier metric accuracy, given endorsement_yes

Note: ['/deployable/rr_pd_sl_batch.py'](deployable/rr_pd_sl_batch.py) is used to run the respective scripts in batch such that the script is deployed for each subject

Analysis has now been run!

- - - -

A project by Aussie Frost, supervised by Taylor Guthrie and Robert Chavez.
* Started: 2023/03/20
* Accuracy SL deployed: 2023/07/05
* Endorsement SL deployed: 2023/11/20
