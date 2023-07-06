# Burmese-Spell-Checker
Burmese Spell Checker (Seq-to-Seq model with attention)

This project aims to build a spell checker model for the Burmese language using a sequence-to-sequence model with attention. The model is trained on a parallel dataset of corrected spelling data along with corresponding incorrect spelling data, comprising over 100,000 sentences with syllable break information.

## Dataset
The dataset used for training the spell checker model can be found in the dataset directory.
Each line in file represents a single sentence, where the corrected and wrong spellings are separated by a tab character.

## Testing Dataset
The testing dataset for evaluating the spell checker model can be found in the testing_dataset directory. It includes two files:

tgt-test.txt: This file contains a subset of sentences with correct spelling for evaluation.
src-test.txt: This file contains a subset of sentences with incorrect spelling for evaluation.

## Training Pipeline
The training pipeline used to train the spell checker model is provided as a Jupyter Notebook file (Seq_to_Seq_Burmse_Spell_Checker.ipynb). You can run this notebook to reproduce the training process and train the model on your own dataset if desired. The notebook includes step-by-step instructions and explanations of the various components involved in training the model.

## Model File
The pretrained model files are stored in Google Drive. You can download the exported model from the following link:

[Google Drive Link to Pretrained Model](https://drive.google.com/drive/folders/1dsaMqduycRURGl84BPplUfDU7J2lIYN-?usp=sharing)

## Usage
To generate text using the trained model, you can utilize the translation code within the training pipeline notebook file. Refer to the training pipeline notebook file for instructions on how to utilize the translation code and translate text using the trained model.

## Evaluation
To evaluate the performance of the spell checker model, you can use the evaluate.ipynb notebook. This notebook includes the evaluation of the model using the testing dataset. It calculates the Word Error Rate (WER) to assess the accuracy of the model's corrected spellings compared to the ground truth.

Reference --> https://www.tensorflow.org/text/tutorials/nmt_with_attention




