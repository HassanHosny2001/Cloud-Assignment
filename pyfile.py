file1 = open(r"Pride and Prejudice.txt", "r", encoding="utf-8")
p = file1.read()
c = p.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

inp_str = c

no_punc = ""
for char in inp_str:
    if char not in punctuations:
        no_punc = no_punc + char

file2 = open(r"Beyond the Wall of Sleep.txt", "r", encoding="utf-8")
r = file2.read()
l = r.lower()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

inp_str = l

nopunc = ""
for char in inp_str:
    if char not in punctuations:
        nopunc = nopunc + char

document_1_text = no_punc
document_2_text = nopunc

document_1_words = document_1_text.split()
document_2_words = document_2_text.split()

common = set(document_1_words).intersection(set(document_2_words))

print(common)