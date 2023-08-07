# Burmese-Spell-Checker
Burmese Spell Checker (Seq-to-Seq model with attention)

## Introduction
This project aims to build a spell checker model for the Burmese language using a sequence-to-sequence model with attention. The model is trained on a parallel dataset of corrected spelling data along with corresponding incorrect spelling data, comprising over 100,000 sentences with syllable break information.

## Artificial Error Making Pipeline
The training pipeline for the spell checker model is provided as a Jupyter Notebook file (data_preparation.ipynb). 

To effectively train the spell checker model, I created artificial spelling errors in the incorrect sentences. The process for preparing the data with artificial errors is as follows:

1. Research Spelling Error Patterns: I conduct comprehensive research to identify common spelling error patterns in the Burmese language. This includes analyzing various sources such as social media text, user-generated content, and other informal text data.

2. Identify Social Media Text Spell Errors: I specifically focus on common spelling errors found in social media texts, as these tend to exhibit a wide range of informal language usage and errors.

3. Error Injection: With the identified spelling error patterns, I inject artificial errors into the original sentences from the dataset. I modify the sentences by introducing spelling errors that align with the researched patterns.

4. Create Incorrect Sentences: After introducing the artificial errors, I store the modified sentences as the "incorrect" version, which will be used for training the spell checker model.

## Training Pipeline
The training pipeline used to train the spell checker model is provided as a Jupyter Notebook file (Seq_to_Seq_Burmse_Spell_Checker.ipynb). You can run this notebook to reproduce the training process and train the model on your own dataset if desired. The notebook includes step-by-step instructions and explanations of the various components involved in training the model.

## Prediction Pipeline
The pretrained model file is stored in Google Drive. You can download the exported model from the following link:
[Google Drive Link to Pretrained Model](https://drive.google.com/file/d/1BgIQ3dxqWJYweaa_rvU0b5BeUTCtgnkt/view?usp=sharing)

#### SpellChecker.py
The SpellChecker.py file contains the Python script for the Burmese Spell Checker prediction pipeline. This pipeline takes as input a sentence with potential spelling errors and returns the corrected version of the sentence.

#### test_spell_check.ipynb
The test_spell_check.ipynb notebook provides an example of how to use the prediction pipeline to test the Burmese Spell Checker on multiple sentences. It demonstrates how to load the model, perform spelling correction, and view the results.

Reference --> https://www.tensorflow.org/text/tutorials/nmt_with_attention




