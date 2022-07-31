import pandas as pd
from numpy import NaN


_cat = {
  'politics': ["amalema","ramaphosa"],
  'tv_news':['skeemsaam', 'gomora'],
  'health': ['covid', 'virus'],
  'community': ['mzansi' ,'bbmzani'],
  'sport': ['soccer', 'football'],
}


data = pd.read_csv("./emoji_tweets_cleaned.csv");
data = data[: 100]
# print( data )


# point
def classify( tag ):
  class_ = "" 
  if type( tag ) == float:
    return "unspecified"
  else:
    for k, val in _cat.items():
      tag = tag.replace("#", " "); tag = ' '.join( tag.split())
      for v in val:
        if v.lower() in tag.lower():
          class_ += k
    if len( class_ ) == 0: return "unspecified"
    else: return class_
# print( classify() )

# get make classifications
data['classify'] = data['hash_tags'].apply( classify )
print( data)
# write data to file.
# newData.to_csv( "./emoji_tweets_classified.csv", index=False )

