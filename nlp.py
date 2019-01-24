import spacy
from spacy.lang.es.stop_words import STOP_WORDS
#es-core-news-sm-2.0.0


def text_processor(text):
    nlp = spacy.load('es')
    doc = nlp(text)

    doc = [word for word in doc if not word.is_stop] #delete stopwords
    response = {}

    for token in doc:
        attr = []
        attr.extend([token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha])

        response['{}'.format(token.text)] = attr.copy()

    return response