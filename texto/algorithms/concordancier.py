from nltk.draw.dispersion import dispersion_plot
import matplotlib.pyplot as plt
from nltk.text import Text
from nltk.probability import FreqDist
import spacy

class Concordancier():

    def __init__(self, corpus="fr_core_news_md"):
        """Construction..."""
        self.nlp = spacy.load(corpus)

    def run(self, texte):
        doc = nlp(texte)
        token = []
        for tok in doc:
            if "\n" not in tok.lemma_:
                token.append(tok.text.lower())
                # tok.append(token.lemma_.lower())
        self.txt = Text(token)
        return self.txt

    def view(self, requete):
        return self.txt.concordance(requete)

