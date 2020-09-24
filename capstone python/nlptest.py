# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

# The text to analyze
text = u"""With what diligence did the poet write each day now! How lovingly he selected his superlatives!
Never in the history of the Press had such ardent care been lavished on a criticism--truly it was not until
 Thursday afternoon that he was satisfied that he could do no more. He put the pages in his pocket, and, too
 impatient even to be hungry, roamed about the quartier, reciting to himself the most hyperbolic of his periods."""
document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
#sentiment = client.analyze_sentiment(document=document).document_sentiment
objects = client.analyze_entities(document)

print('Text: {}'.format(text))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
print('Object: ',objects)