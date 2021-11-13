#!/usr/bin/env python 

import pandas as pd
from collections import namedtuple
from dataclasses import dataclass
from dataclasses import asdict


Author = namedtuple('Author', 'authorName journal date')

authorList = []
authorList.append(Author('Bob Smith','Journal of Witchcraft',2018))
authorList.append(Author('Mary Elizabeth','Duck Duck Goose Transactions',2019))
authorList.append(Author('Cris Jane','Journal of Ambiguity',2017))



df = pd.DataFrame.from_records(authorList,columns=Author._fields)

print(df)

# Very nice! 
# Unfortunately, can't build Author named tuple one field at a time... 
# So try a dataclass:

# Can put these one per line, or spread them out to taste
# Have to give a default value if want empty constructor tho... Python, why u gotta make work 4 me?
@dataclass
class AuthorC:
    authorName:str=None
    journal:str=None
    date:int=0
    
# This part is exactly the same:
authorList = []
authorList.append(AuthorC('Bob Smith','Journal of Witchcraft',2018))
authorList.append(AuthorC('Mary Elizabeth','Duck Duck Goose Transactions',2019))
authorList.append(AuthorC('Cris Jane','Journal of Ambiguity',2017))

# But now we can also do:
a = AuthorC()
a.authorName = 'Sam Sneed'
a.journal = 'Journal of Alliteration'
a.date = 2020

authorList.append(a)

print(list(asdict(a).keys()))

# Sigh... this doesn't seem to work.. complains AuthorC is not iterable. 
df = pd.DataFrame.from_records(authorList,columns=list(asdict(a).keys()))

print(df)


# The straightforward but ugly way...
#df = pd.DataFrame(columns=['authorName', 'journal', 'date'])
#df = df.append({'authorName':'Bob Smith','journal':'Journal of Witchcraft','date':2018},ignore_index=True)
#df = df.append({'authorName':'Mary Elizabeth','journal':'Duck Duck Goose Transactions','date':2019},ignore_index=True)
#df = df.append({'authorName':'Cris Jane','journal':'Journal of Ambiguity','date':2017},ignore_index=True)