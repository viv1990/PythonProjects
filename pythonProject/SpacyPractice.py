import spacy
from spacy.tokens import Span
from nltk.stem import PorterStemmer
nlp=spacy.blank('en')
print("Blank Pipeline components->",nlp.pipe_names)
doc=nlp("Dr. strange loves pao-bhaji in India as it costed him two $ per place. He loved that")
for token in doc:
    print(token,"-->",token.i,"Is-alphanumeric",token.is_alpha,
          "Is currency",token.is_currency, "Like Number",token.like_num,
    "Is Punctuation",token.is_punct)

#Stemming in nltk
object1=PorterStemmer()
#PorterStemmer is a class, object1 is an object of that class so that object1 can use the methods provided by PorterStemmer

words=['Eating','ate','eat','eats','Remarkable','ability','preposterous','amazing', 'broked','better',"isn't"]
sent=["Mando who works in IBM and has a net worth of 45 Billion $ ,talked incessantly for 3 hours but talking isn't his cup of tea"]

for word in words:
    print(word,"Base word->",object1.stem(word))

wordslist=(' ').join(words)
# I need to make it a string to send it to nlp1 object of model en_core_web_sm
sent=('').join(sent)
nlp1=spacy.load('en_core_web_sm')
print("Trained Pipeline Components",nlp1.pipe_names)
doc2=nlp1(wordslist)
for token in doc2:
    print(token,"Base word->",token.lemma_)
print("Lets do the lemmatisation of a sentence:Mando talked incessantly for 3 hours but talking isn't his cup of tea")
doc3=nlp1(sent)
for token in doc3:
    print(token,"Base word->",token.lemma_,"Hash of the word->",token.lemma)
#"Named entity Recognition"
for token in doc3.ents:
    print("Named Entities are->",token,"Lebel is",token.label_)

# "Customisation of my nlp attribute by adding new words, like Bro and Brah denotes Brother. but
# when we lemmatise, bro and Brah  shows brother. Lets customise it

text4="Bro you wanna go? Brah, don't say no! I am exhausted"
ar=nlp1.get_pipe('attribute_ruler')
ar.add([[{"TEXT":"Bro"}],[{"Text":"Brah"}],[{"Text":'bro'}]],{"LEMMA":"Brother"})
doc=nlp1("Bro you wanna go? Brah, don't say no bro! I am exhausted")
for token in doc:
    print(token,"Base word->",token.lemma_)
# How to print Part of Speech

print("Part of Speech")

sent=["Mando who works in IBM and has a net worth of 45 Billion $ ,talked incessantly for 3 hours but talking isn't his cup of tea"]
sent=('').join(sent)
doc4=nlp1(sent)
for token in doc4:
    print(token,"| Part of speech is-> |",token.pos_,"| Explanation |",spacy.explain(token.pos_),
          "| Token Tag is->| ",token.tag_,spacy.explain(token.tag_))
count=doc4.count_by(spacy.attrs.POS)
for k,v in count.items():
    print(doc4.vocab[k].text,v)


# For customisation of Named Entity Recognition, in the below text, Tesla as well as Twitter ate not identified as organisations

doc=nlp1("Tesla is going to acquire twitter in $45 billion, one of the biggest deals")
s1=Span(doc,0,1,label="ORG")
s2=Span(doc,5,6,label="ORG")
doc.set_ents([s1,s2],default="unmodified")

for token in doc.ents:
    print(token, token.label_)