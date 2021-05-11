# 
# Texto
# Par Jeremy Demange
# 

from pkg_resources import resource_filename
import pandas as pd
import spacy
from re import search
import re
import collections
import math
from nltk.stem.snowball import SnowballStemmer
import pkgutil


class Ramer():
    """
    Classe pour utiliser Ramer.
    """

    def __init__(self, corpus="fr_core_news_md"):
        """..."""
        # Stem
        self.stemmer = SnowballStemmer(language='french')

        # NLP load
        self.nlp = spacy.load(corpus)
        # Save
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab1.pkl"))
        self.lab1 = df2.values.tolist()
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab2.pkl"))
        self.lab2 = df2.values.tolist()
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab3.pkl"))
        self.lab3 = df2.values.tolist()

        # Save
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab1s.pkl"))
        self.lab1s = df2.values.tolist()
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab2s.pkl"))
        self.lab2s = df2.values.tolist()
        df2 = pd.read_pickle(resource_filename(__name__, "../cache/lab3s.pkl"))
        self.lab3s = df2.values.tolist()


    def view_thematic(self, texte):
        # Mount doc 
        doc = self.nlp(texte)
        doc = [self.stemmer.stem(X.text) for X in doc]

        # Results
        resLab1 = []
        resLab2 = []
        resLab3 = []
        
        # Token
        for token in doc:
            entry = token.lower()
            for i in range(0, len(self.lab3)):
                # if (entry).find(lab3[i]) is not -1:
                if entry == self.lab3s[i][0]:
                    if self.lab3[i][0] != "nan":
                        resLab3.append(self.lab3[i][0])
                    if self.lab2[i][0] != "nan":
                        resLab2.append(self.lab2[i][0])
                    if self.lab1[i][0] != "nan":
                        resLab1.append(self.lab1[i][0])
                # if (entry).find(lab2[i]) is not -1:
                if entry == self.lab2s[i][0]:
                    # if lab3[i] != "nan":
                    #     resLab3.append(lab3[i])
                    if self.lab2[i][0] != "nan":
                        resLab2.append(self.lab2[i][0])
                    if self.lab1[i][0] != "nan":
                        resLab1.append(self.lab1[i][0])
                # if (entry).find(lab1[i]) is not -1:
                if entry == self.lab1s[i][0]:
                    # if lab3[i] != "nan":
                    #     resLab3.append(lab3[i])
                    # if lab2[i] != "nan":
                    #     resLab2.append(lab2[i])
                    if self.lab1[i][0] != "nan":
                        resLab1.append(self.lab1[i][0])

        # Interprete
        cat1 = []
        cat2 = []
        cat3 = []
        bestCat = ""
        if len(resLab1):
            counts = collections.Counter(resLab1)
            new_list = sorted(resLab1, key=lambda x: -counts[x])
            if new_list[0] != "nan":
                cat1 = collections.OrderedDict((x, True) for x in new_list).keys()
                bestCat = new_list[0]
            if len(resLab2):
                counts = collections.Counter(resLab2)
                new_list = sorted(resLab2, key=lambda x: -counts[x])
                if new_list[0] != "nan":
                    cat2 = collections.OrderedDict((x, True) for x in new_list).keys()
                if len(resLab3):
                    # print(resLab3)
                    counts = collections.Counter(resLab3)
                    new_list = sorted(resLab3, key=lambda x: -counts[x])
                    if new_list[0] != "nan":
                        cat3 = collections.OrderedDict((x, True) for x in new_list).keys()


        res = {"cat1": list(cat1), "cat2": list(cat2), "cat3": list(cat3), "bestCat": bestCat}
        return res

    def run(self, texte):
        """..."""
        return self.view_thematic(texte)

    # def view(self, requete):
    #     """..."""
    #     self.requete = requete
    #     return self.txt.concordance(requete)

    # def export(self, requete = "", output = "./output.txt", formatage = "classic"):
    #     """..."""
    #     if requete == "":
    #         requete = self.requete
    #     result = self.txt.concordance(requete)
    #     if formatage == "classic":
    #         with open(output, 'w') as f:
    #             f.write(str(result))

