#%%
import numpy as np
import os
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import nltk
import string
from collections import Counter
#%%
# Import BOM
os.chdir('/Users/douglasvalentine/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Python')
filepath = 'BoM.txt'

file1 = open(filepath, 'r')
bom = file1.read()
file1.close()

#%%
#handle then numbers
numbers = []
for i in range(0,101):
    numbers.append(str(i))

#%%
stopwords = set(STOPWORDS)
stopwords.update(["ye", "came", "pass", "behold",'yea','now',
'helaman','nephi','alma','moroni','mormon','mosiah','jacob','may','thus',
'therefore','even','will','unto','upon','thing','come','ether',
'said','3','things','many','hath','thou','hast','thy'])
stopwords.update(string.punctuation)
stopwords.update(numbers)

#%%
wordcloud = WordCloud(stopwords=stopwords,background_color='white', \
    max_words=100,width=800, height=400, \
    colormap='ocean').generate(bom)
plt.figure(figsize=(20,10))
plt.imshow(wordcloud, interpolation='bilinear',aspect='equal')
plt.axis('off')
plt.show()

#%%
wordcloud.to_file('BOM_WC.png')

#%%
bom_data = [i for i in nltk.word_tokenize(bom.lower()) if i not in stopwords]

#%%
counts = dict(Counter(bom_data).most_common(40))

labels, values = zip(*counts.items())

# sort your values in descending order
indSort = np.argsort(values)[::-1]

# rearrange your data
labels = np.array(labels)[indSort]
values = np.array(values)[indSort]

indexes = np.arange(len(labels))

# bar_width = 0.35
plt.figure(figsize=(8,8))
plt.bar(indexes, values, color=['yellow','blue', 'red'])

# add labels
plt.title('BoM Top Words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(indexes, labels, rotation='vertical')
plt.savefig('BoM_hist.png')
plt.show()

#%%
#Make a pandas data frame
counts_all = (Counter(bom_data))
df = pd.DataFrame.from_dict(counts_all,orient='index')
df.columns = ['Counts']
#%%
Jesus_Names = df.loc[['lord','god','jesus','christ','savior',
'redeemer','father','prince']]
Jesus_Names = Jesus_Names.sort_values('Counts', ascending=False)

#%%
labels1 = np.array(Jesus_Names.index)
values1 = np.array(Jesus_Names.Counts)
indexes1 = np.arange(len(labels1))
# bar_width = 0.35
plt.figure(figsize=(8,8))
plt.bar(indexes1, values1, color='green')

# add labels
plt.title('Names of Jesus')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(indexes1, labels1)
plt.savefig('Jesus_hist.png')
plt.show()

#%%
from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, HoverTool

#%%
output_file('bokeh_bar.html')

source = ColumnDataSource(Jesus_Names)

p = figure(plot_height=500,x_range=list(Jesus_Names.index),title='Book of Mormon - Names of Christ')

p.vbar(x='index', top='Counts', width=0.9, source=source, color='red')
p.yaxis.axis_label = 'Frequency'
show(p)

#%%
