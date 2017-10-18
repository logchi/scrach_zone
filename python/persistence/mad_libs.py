import sys

src_path = argv[1]
words_blank = ('ADJECTIVE', 'NOUN', 'ADVERB', 'VERB')

src_file = open(src_path)
setence = src_file.read()
src_file.close()
word_list = setence.split(' ')

word_tmpl = [(index, word.lower()) for index, word in enumerate(word_list) if word in words_blank]

cursor = 0
for tmpl in word_tmpl:
    print('Enter an %s:' % tmpl)
    word_list