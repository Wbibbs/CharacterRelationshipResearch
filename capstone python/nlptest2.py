from google.cloud import language_v1
from google.cloud.language_v1 import enums
import time, os

num_of_processed_files = 0
def process_text(text_content, filename):
    """
    Analyzing Entities in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'California is a state.'

    # Available types: PLAIN_TEXT, HTML
    
    try:
        type_ = enums.Document.Type.PLAIN_TEXT
    except:
        return

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
	
	#Set output path for data files
    #outpath = "F:\\out data json\\"
    outpath = "F:\SmallSetTest\\split\\data\\"
	
	#Cut .txt from file
    filename = filename[:len(filename)-4]
    a = open(str(outpath + filename + ".json"), "w+", errors="replace")
    response = client.analyze_entities(document, encoding_type=encoding_type)
    a.write(str(response))
    # Loop through entitites returned from the API
    #for entity in response.entities:
	    #print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        #print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        #a.write(u"Entity type: {}".format(enums.Entity.Type(entity.type).name) + "\n")
        # Get the salience score associated with the entity in the [0, 1.0] range
        #print(u"Salience score: {}".format(entity.salience))
        #a.write(u"Salience score: {}".format(entity.salience) + "\n")
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        #for metadata_name, metadata_value in entity.metadata.items():
            #print(u"{}: {}".format(metadata_name, metadata_value))
            #a.write(u"{}: {}".format(metadata_name, metadata_value) + "\n")

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        #for mention in entity.mentions:
            #print(u"Mention text: {}".format(mention.text.content))
            #a.write(u"Mention text: {}".format(mention.text.content) + "\n")
            # Get the mention type, e.g. PROPER for proper noun
            #print(
                #u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            #)
            #a.write(u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name) + "\n")
    a.close()

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    #print(u"Language of the text: {}".format(response.language))
	

#Open books as string and pass

directory = "F:\SmallSetTest\\split\\"

start_time = time.time()
for file in os.listdir(directory):
	if not os.path.isdir(file):
		num_of_processed_files += 1
		text = open(str(directory + file), "r+", errors="ignore")
		texttext = text.read()
		process_text(texttext, file)
		text.close()


print('Time to process ', num_of_processed_files, ' files:', time.time() - start_time, ' s')