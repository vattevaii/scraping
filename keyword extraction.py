import re
import json
from nltk.corpus import stopwords
from rake_nltk import Rake
import nltk


# this line for download of nltk files here we dowmload stopwords and keyword etractons 
# nltk.download()

## read json file
data_json = json.load(open('data.json'))


## this will only work when you download stopwords from nltk to your local machine alternatively you can run this ode on colab or kaggle. process is automatic there
stop_words =stopwords.words('english')

## remove html tages and get pure text
def get_pure_text(temp):
    pure_text= ''
    for item in temp:
#         item = re.sub(r'[^\w\s]','',item) 
        pure_text+=re.sub(r'<.*?>', "", item)
    return pure_text


## stop words remove
def remove_stop_words(temp):
    pure_text = get_pure_text(temp)
    final=''
    for word in pure_text.split():
        if word.lower() not in stop_words:
#             text = re.sub(r'[^a-zA-Z0-9. ]','',word) # remove punctuations
            final += word+' '
    return final

## this will extract keywords from given text
def get_keywords(json_text):
    stop_words_removed_text = remove_stop_words(json_text)
    r= Rake()
    r.extract_keywords_from_text(stop_words_removed_text)
    keywords = r.get_ranked_phrases()
    # print(f'html text : {json_text} \n\n stopword removed text : {stop_words_removed_text}\n\n keywords : {set(keywords)}')
#     print(keywords)
#     print(len(keywords))
    return list(set(keywords))


## this will update json data by adding keywords to the file
def update_json_with_keywords(jsonData):
    for i in range(len(jsonData)):
        jsonData[i].update({
            'keywords' : get_keywords(jsonData[i]['data']),
            'data' : get_pure_text(jsonData[i]['data'])
        })
    return jsonData

## following is the driver code
new_json = json.dumps(update_json_with_keywords(data_json))
with open("datawithkeywords.json", "w") as outfile:
    outfile.write(new_json)
    