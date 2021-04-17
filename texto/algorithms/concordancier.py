# 
# Texto
# Par Jeremy Demange
# 

from nltk.text import Text
from nltk.probability import FreqDist
import spacy

class Concordancier():
    """
    Classe pour générer des concordancier.
    """

    def __init__(self, corpus="fr_core_news_md"):
        """..."""
        self.nlp = spacy.load(corpus)

    def run(self, texte, lem=False):
        """..."""
        doc = self.nlp(texte)
        token = []
        for tok in doc:
            if "\n" not in tok.lemma_:
                if lem:
                    tok.append(token.lemma_.lower())
                else:
                    token.append(tok.text.lower())
        self.txt = Text(token)

    def view(self, requete):
        """..."""
        self.requete = requete
        return self.txt.concordance(requete)

    def export(self, requete = "", output = "./output.txt", formatage = "classic"):
        """..."""
        if requete == "":
            requete = self.requete
        result = self.txt.concordance(requete)
        if formatage == "classic":
            with open(output, 'w') as f:
                f.write(str(result))

