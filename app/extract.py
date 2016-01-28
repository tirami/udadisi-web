from collections import defaultdict
import nltk


def extract_terms(text):
    tokens = text.split(' ')
    tagged = nltk.pos_tag(tokens)
    nouns = [word for (word, lexical_type) in tagged if lexical_type == 'NN']
    terms = defaultdict(int)
    for noun in nouns:
        terms[noun] += 1
    return terms
