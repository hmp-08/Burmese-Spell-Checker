# Burmese-Spell-Checker
Burmese Spell Checker (Seq-to-Seq model with attention)

This project aims to build a spell checker model for the Burmese language using a sequence-to-sequence model with attention. The model is trained on a parallel dataset of corrected spelling data along with corresponding incorrect spelling data, comprising over 100,000 sentences with syllable break information.

## Dataset
The dataset used for training the spell checker model can be found in the dataset directory.
Each line in file represents a single sentence, where the corrected and wrong spellings are separated by a tab character.

## Training Pipeline
The training pipeline used to train the spell checker model is provided as a Jupyter Notebook file (Seq_to_Seq_Burmse_Spell_Checker.ipynb). You can run this notebook to reproduce the training process and train the model on your own dataset if desired. The notebook includes step-by-step instructions and explanations of the various components involved in training the model.

## Model File
The pretrained model files are stored in Google Drive. You can download the exported model from the following link:

[Google Drive Link to Pretrained Model](https://drive.google.com/drive/folders/1dsaMqduycRURGl84BPplUfDU7J2lIYN-?usp=sharing)

## Usage
To generate text using the trained model, you can utilize the translation code within the training pipeline notebook file. Refer to the training pipeline notebook file for instructions on how to utilize the translation code and translate text using the trained model.

Reference --> https://www.tensorflow.org/text/tutorials/nmt_with_attention




