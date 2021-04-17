# 
# Texto
# Par Jeremy Demange
# 

from nltk.draw.dispersion import dispersion_plot
import matplotlib.pyplot as plt
from nltk.text import Text
import spacy

class Dispersion():
    """
    Classe pour générer une dispersion de texte.
    """

    def __init__(self, corpus="fr_core_news_md"):
        """..."""
        self.nlp = spacy.load(corpus)

    def run(self, texte, lem=False):
        """..."""
        doc = self.nlp(texte)
        token = []
        for tok in doc:
            token.append(tok.text.lower())
        self.token = token

    def view(self, targets=['je','nous', 'vous'], figsize=(12, 9)):
        """..."""
        return dispersion_plot(self.token, targets, ignore_case=True, title='Lexical Dispersion Plot')

    def export(self, targets=['je','nous', 'vous'], figsize=(12, 9), output = "./output.png", formatage = "classic"):
        """..."""
        fig = plt.figure()
        dplot = dispersion_plot(self.token, targets, ignore_case=True, title='Lexical Dispersion Plot')
        fig.savefig(output)


