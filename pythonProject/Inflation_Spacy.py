import spacy
from spacy import displacy

with open("Inflation_spacy_exercise.txt") as f:
    File=f.readlines()

print(File)
file=('').join(File)
print(file)
nlp=spacy.load('en_core_web_sm')
doc=nlp(file)

# To extract all nouns from the file
Nounextracts=[]
Numextracts=[]
count=doc.count_by(spacy.attrs.POS)
for token in doc:
    if token.pos_ in ['NOUN','PROPN']:
        Nounextracts.append(token)
    if token.pos_ in ['NUM']:
        Numextracts.append(token)

for k,v in count.items():
    print(doc.vocab[k].text,v)
print("All Nouns",Nounextracts)
print("All Numbers",Numextracts)

displacy.render(doc,style="ent")
