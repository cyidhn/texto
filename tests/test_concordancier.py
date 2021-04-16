from texto.algorithms.concordancier import Concordancier

def test_concordancier():
    corpus = "Bonjour à tous !"
    traitement = Concordancier()
    traitement.run(corpus)
    traitement.view("bonjour")