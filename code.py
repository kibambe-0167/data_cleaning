import pandas as pd
import re
import io

data = pd.read_csv("./emoji_tweets_202207231326.csv");
# data = data[ : 40]
# print( data )

# extract hash tags in the sentence
def extractHashTags( sentence ):
    hash_tags = []
    for word in sentence.split():
        if word.startswith('#'):
            hash_tags.append(word)
    return hash_tags  

# clean the sentence data, put text to lower case
def cleanData( col ):
    col = col.lower()
    col = ' '.join( col.split() )
    # remove all links/url in the sentence
    col = [ i for i in col.split(' ') if not re.search("^http", i ) ]
    col = ' '.join( col )
    col = re.sub("[.\":?@#_]", " ", col)
    # remove all non-alphanumeric characters
    col = re.sub("[^a-zA-Z0-9]", " ", col)
    col = ' '.join( col.split() )
    # print( col )
    return col

# make series or column of hash tags
def makeHashTagsSeries( data ):
    data['hash_tags'] = data['sentence'].apply( extractHashTags )
    data['hash_tags'] = data['hash_tags'].apply( lambda x: ' '.join(x) )
    return data['hash_tags']

# add series to dataframe
def addHashTagsSeries( data ):
    data['hash_tags'] = makeHashTagsSeries( data )
    return data

# add cleaned sentence to dataframe
def addCleanedSentence( data ):
    data['clean_sentence'] = data['sentence'].apply( cleanData )
    return data
  
    
  
# 
# add hash tags to dataframe
newData = addHashTagsSeries( data )
# add cleaned sentence to dataframe
newData = addCleanedSentence( newData )
# 
# print( newData[['hash_tags','sentence', 'clean_sentence']] )
# newData.to_csv( "./emoji_tweets_cleaned.csv", index=False )



# get unique hash tags
def getUniqueTags( data ):
    unique_tags = []
    for tags in data['hash_tags']:
        if len( tags ) > 0:
            tags = ' '.join( tags.split() )
            # print( tags.split(' ') )
            for tag in tags.split(' '):
                if tag not in unique_tags:
                    unique_tags.append( tag )            
    # print( unique_tags )
    return unique_tags

u_tags = getUniqueTags( newData )
# write to file..
with io.open("uniqueHashTags.txt", mode="w", encoding="utf-8") as f:
    for tag in u_tags:
        f.write( tag + "\n" )
    
print("........ done ...........")