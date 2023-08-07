import tensorflow as tf
import re
import syllable_break
sb_obj = syllable_break.syllable_break()

MODEL_PATH = "/home/user/Documents/workspace_mt/Spell_checker/translator"

class SpellChecker():
    def __init__(self):
        self.model_cache = {}  # Dictionary to store cached models

    def get_cached_model(self):
        # Check if the model is already in the cache
        if MODEL_PATH in self.model_cache:
            return self.model_cache[MODEL_PATH]

        # If not, load the model and cache it
        model = tf.saved_model.load(MODEL_PATH)
        self.model_cache[MODEL_PATH] = model
        return model

    def correct_spell(self, sent_list):
        corrected_sent = []
        if isinstance(sent_list, tf.Tensor):
            sent_list = tf.strings.unicode_decode(sent_list, 'UTF-8').numpy().tolist()

        if isinstance(sent_list, str):
            sent_list = [sent_list]
            
        #syllable break
        syl_sent_list = []
        for sent in sent_list:
            syl_sent_list.append(sb_obj.sylseg(sent))

        # Load the model from the cache
        model = self.get_cached_model()

        for t in syl_sent_list:
            corrected_sent.append(model.translate([t])[0].numpy().decode())
        return corrected_sent