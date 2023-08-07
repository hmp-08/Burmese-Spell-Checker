import re

class syllable_break:
    def __init__(self):
        pass

    def sylseg(self, input_text):
        input_text = "Ò" + input_text
        input_text = re.sub("([a-zA-Z]([a-z]+))", r"Ò\1",input_text)
        input_text = re.sub("([0-9])", r"Ò\1", input_text)
        input_text = re.sub("([၀-၉])", r"Ò\1", input_text)
        input_text = re.sub("([\s])", r"Ò\1", input_text)
        input_text = re.sub("([၊။()!@#$%^&*_=+|\\]×\\/-])", r"Ò\1", input_text)
        input_text = re.sub("့်", "့်", input_text)
        input_text = re.sub("([က-ဪဿ၌-၏])", r"Ò\1", input_text)
        input_text = re.sub("([~])", r"Ò\1", input_text)
        input_text = re.sub("Ò([က-အ])([္်])", r"\1\2", input_text)
        input_text = re.sub("([္])Ò([က-အ])", r"\1\2", input_text)
        input_text = re.sub("([~])", r"Ò\1", input_text)
        input_text = re.sub("Ò([က-အ])([့်])", r"\1\2", input_text)
        input_text = re.sub("([Ò]+)", "Ò", input_text)
        input_text = re.split("Ò", input_text)
        syl = ' '.join([str(elem) for elem in input_text])
        syl = re.sub("\s+", " ", syl)
        syl = re.sub("^\s", "", syl)
        return syl
