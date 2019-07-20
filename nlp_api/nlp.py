import spacy
#es-core-news-sm-2.0.0
from nlp_api.neural_model import obsenities_classification

def data_processor(text):

    nlp = spacy.load('es')
    doc = nlp(text)
    print(doc)
    doc = [word for word in doc if not (word.is_stop or word.is_punct or word.pos_ == "VERB")] #delete stopwords, punctiation & verbs

    doc = obsenities_classification(doc)



    response = {}
    print(doc)

    for token in doc:
        #print(token, token.has_vector, token.vector_norm)
        attr = []
        attr.extend([token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha])

        response['{}'.format(token.text)] = attr.copy()

    return response