#%%
from spacy.lang.en import English

# %%
nlp = English()

# %%
os.chdir('/Users/douglasvalentine/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/Python')
filepath = 'BOM_ANALYSIS/BoM.txt'

file1 = open(filepath, 'r')
bom = file1.read()
file1.close()


# %%
doc = nlp(bom)

# %%
