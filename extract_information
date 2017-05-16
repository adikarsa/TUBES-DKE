# extracting names, emails and phone
import re
import nltk

# string = open('10.txt', 'r').read()
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i) < 128)
    
def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_phone_numbers(string):
	r = re.compile(r'(\d{3}[-\.\s]??\d{7}|\d{4}[-\.\s]??\d{7}|\d{3}[-\.\s]??\d{8}|\d{4}[-\.\s]??\d{8})')
	return r.findall(string)
	
def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)

def extract_names(document):
    names = []
    sentences = ie_preprocess(document)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

def extract_organizations(document):
   organizations = []
   sentences = ie_preprocess(document)
   for tagged_sentence in sentences:
       for chunk in nltk.ne_chunk(tagged_sentence):
           if type(chunk) == nltk.tree.Tree:
               if chunk.label() == 'ORGANIZATION':
                   organizations.append(' '.join([c[0] for c in chunk]))
   return organizations


# numbers = extract_phone_numbers(string)
# emails = extract_email_addresses(string)
# names = extract_names(string)
# organizations = extract_organizations(string)

# print (numbers)
# print (emails)
# print (names)
# print (organizations)

entity = []
for i in range(1, 10):
  file = open(str(i) + ".txt", "r")
  string = remove_non_ascii(file.read())
  names = extract_names(string)
  names = list(set(names))
  entity.append(names)

print(entity)
