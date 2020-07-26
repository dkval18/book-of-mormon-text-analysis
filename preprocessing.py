#%%
import pandas as pd 
import numpy as np
import re

#%%
# Import BOM
# os.chdir('/Users/douglasvalentine/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Python')
filepath = 'BoM.txt'

file1 = open(filepath, 'r')
bom = file1.read()
file1.close()

#%%
test_seq = '''
1 Nephi 10
Chapter 10

1 Nephi 10:15
 15 And after this manner of language did my father prophesy and
speak unto my brethren, and also many more things which I do not
write in this book; for I have written as many of them as were
expedient for me in mine other book.

1 Nephi 10:16
 16 And all these things, of which I have spoken, were done as my
father dwelt in a tent, in the valley of Lemuel.
'''

# %%
chap_verse_pat = r'\d*\D+ \d+\:\d+'
book_pat = r'\d*\D+'
chapter_pat = r'\d+\:'
verse_pat = r'\:\d+'
header_chap_num_pat = r'\d* \D+ \d+'
header_chap_pat = r'Chapter'

data = []
verse_text = ""
book, chapter, verse = ('','','')
for line in bom.split('\n'):
    chap_verse = re.match(chap_verse_pat, line)
    header_chap_num = re.match(header_chap_num_pat, line)
    header_chap = re.match(header_chap_pat, line)

    if chap_verse is not None:
        data.append([book,chapter,verse,verse_text])
        verse_text = '' #reset text
        book = re.match(book_pat, line)[0]
        chapter = re.search(chapter_pat, line)[0].split(':')[0]
        verse = re.search(verse_pat, line)[0][1:]

    elif chap_verse is None and header_chap is None and header_chap_num is None and line != '':
        newline = re.sub('\d+','',line)
        verse_text = verse_text + ' ' + newline
    
data.append([book,chapter,verse,verse_text])

# %%
df = pd.DataFrame(data, columns=['book', 'chapter', 'verse', 'verse_text'])

# %%
