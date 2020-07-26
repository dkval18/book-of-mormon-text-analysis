#%%
import boto3
import pandas as pd 
import os

# %%
cred = pd.read_csv('credentials.csv')

# %%
access_key = cred.iloc[0,2]
secret = cred.iloc[0,3]


# %%
s3 = boto3.client('s3',aws_access_key_id=access_key, aws_secret_access_key=secret)

# %%
s3.create_bucket(Bucket='bom-analysis')

# %%
s3.upload_file(Filename='names_of_christ.html',
    Bucket='bom-analysis', Key='names_of_christ.html',
    ExtraArgs = {
                 # Set proper content type
                 'ContentType':'text/html',
                 # Set proper ACL
                 'ACL': 'public-read'})


# %%
print("http://{}.s3.amazonaws.com/{}".format('bom-analysis', 'names_of_christ.html'))

# %%
link = 'http://bom-analysis.s3.amazonaws.com/names_of_christ.html'

# %%
s3.upload_file(Filename='BOM_WC.png',
    Bucket='bom-analysis', Key='BOM_WC.png',
    ExtraArgs = {
                 # Set proper content type
                 'ContentType':'image/png',
                 # Set proper ACL
                 'ACL': 'public-read'})



# %%
