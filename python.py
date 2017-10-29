# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

import requests

def implicit():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)

# def explicit():
#     from google.cloud import storage

#     # Explicitly use service account credentials by specifying the private key
#     # file. All clients in google-cloud-python have this helper, see
#     # https://google-cloud-python.readthedocs.io/en/latest/core/modules.html
#     #   #google.cloud.client.Client.from_service_account_json
#     storage_client = storage.Client.from_service_account_json(
#         'service_account.json')

#     # Make an authenticated API request
#     buckets = list(storage_client.list_buckets())
#     print(buckets)


# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u'This is where the magic happens. My truck broke down.'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
docSentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(docSentiment.score, docSentiment.magnitude))

for sentence in client.analyze_sentiment(document=document).sentences:
	print (sentence.text.content)
	print ('Sentiment: {}, {}'.format(sentence.sentiment.score, sentence.sentiment.magnitude))



# METER ANALYSIS
myheaders={
    "X-Mashape-Key": "ghdyrk5qrEmshlQ4LTQ1yDLtFAuDp1GxyEtjsnuZJRUV8QSxJN",
    "Accept": "application/json"} 

input_sentence = "I got my first real six string"
total_syllables = 0;
for input_word in input_sentence.split():  
    response = requests.get("https://wordsapiv1.p.mashape.com/words/{}/syllables".format(input_word), headers = myheaders)
    print(response.text.syllables)
    #total_syllables += response.count


# myheaders={
#     "X-Mashape-Key": "ghdyrk5qrEmshlQ4LTQ1yDLtFAuDp1GxyEtjsnuZJRUV8QSxJN",
#     "Accept": "application/json"}   
# response = requests.get("https://wordsapiv1.p.mashape.com/words/{}/syllables".format(test), headers = myheaders)
# print(response.text)



# These code snippets use an open-source library. http://unirest.io/python
#print("https://wordsapiv1.p.mashape.com/words/{}".format(test))
# response = requests.get("https://wordsapiv1.p.mashape.com/words/{}".format(test),
#   headers={
#     "X-Mashape-Key": "ghdyrk5qrEmshlQ4LTQ1yDLtFAuDp1GxyEtjsnuZJRUV8QSxJN",
#     "Accept": "application/json"
#   }
# )