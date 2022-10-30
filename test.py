import pandas as pd

csv = pd.read_csv('accounts.csv')

df = pd.DataFrame([['riken','khadela','99789','rikenkhadela777','wegyh','now']])
df.to_csv('accounts.csv',mode='a',header=False,index=False)