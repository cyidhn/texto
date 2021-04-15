import spacy

def transform_token_lem(corpus, lang="fr"):
    if lang == "fr":
        nlp = spacy.load("fr_core_news_md")
    else:
        except print("Merci de choisir la langue fr")

    doc = nlp(corpus)

    token = []
    for tok in doc:
        if not tok.is_punct and not tok.is_stop:
            if len(tok.lemma_) > 1 and "\n" not in tok.lemma_ and "qu" not in tok.lemma_:
                token.append(tok.lemma_.lower())

    return token

def transform_token_all(corpus, lang="fr"):
    if lang == "fr":
        nlp = spacy.load("fr_core_news_md")
    else:
        except print("Merci de choisir la langue fr")

    doc = nlp(corpus)

    token = []
    for tok in doc:
        if "\n" not in tok.text:
            token.append(tok.text.lower())
        
    return token