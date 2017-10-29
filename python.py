# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

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
text = u'This is where the magic happens'
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(document=document).document_sentiment

print('Text: {}'.format(text))
print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))