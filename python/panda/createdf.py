#!/usr/bin/env python 

import pandas as pd


df = pd.DataFrame(columns=['authorName', 'journal', 'date'])

print(df)

df = df.append({'authorName':'Bob Smith','journal':'Journal of Witchcraft','date':2018},ignore_index=True)
df = df.append({'authorName':'Mary Elizabeth','journal':'Duck Duck Goose Transactions','date':2019},ignore_index=True)
df = df.append({'authorName':'Cris Jane','journal':'Journal of Ambiguity','date':2017},ignore_index=True)

df['comment']="completed"

print(df)


df['newcolumn']=df.date+2000
print(df)