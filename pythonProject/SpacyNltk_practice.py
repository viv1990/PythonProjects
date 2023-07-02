import spacy
import nltk
from nltk.tokenize import sent_tokenize
nlt=spacy.load("en_core_web_sm")
# nlt is the object, so I am using Object oriented programming
# en_core_web_sm is a model already trained on senetence tokenisation, iyt understand how to break a para into
# proper sentences
#.load is to load a trained pipeline, if you want blank instance
#use .blank('en')
doc=nlt("Dr. is checking if I can eat pao-bhaji. However,hulk loves delhi chaat")
for sentence in doc.sents:
    print(sentence)

print(sent_tokenize("Dr. is checking if I can eat pao-bhaji. However,hulk loves delhi chaat"))