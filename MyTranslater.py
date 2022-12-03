import os
from translate import Translator
import goslate


class Mytranslater:
    def goslate(self, text, lang1):
        gs = goslate.Goslate()
        return gs.translate(text, lang1)

    def translate(text, lang):
        translate = Translator(lang)
        return translate.translate(text)
