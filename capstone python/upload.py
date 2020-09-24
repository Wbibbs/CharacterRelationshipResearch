import os
from google.cloud import storage


def upload_blob():
	"""Uploads a file to the bucket."""
	bucket_name = "capstone-store"
	source_file_name = "F:\\nov5\\"
	folder = "FullProcessedSet/"
	
	storage_client = storage.Client()
	bucket = storage_client.bucket(bucket_name)
	
	
	blob = bucket.blob(bucket_name + folder)
	
	for file in os.listdir(source_file_name):
		blob = bucket.blob(folder + file)
		blob.upload_from_filename(source_file_name + file)
		
	print('Finished upload')
	
upload_blob()
thread.sleep(5000)