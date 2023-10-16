from elasticsearch import Elasticsearch
import json
import os
from dotenv import load_dotenv
load_dotenv()

# This is the default user
user = "elastic"

password = os.environ.get('ELASTIC_PASSWORD')

# Define your Elasticsearch server
es = Elasticsearch(
    ['https://localhost:9200'],  # Replace with your Elasticsearch server URL
    basic_auth=(user, password),
    verify_certs=False,  # Set to False. Do not need to verify the server SSL certificate
)
# The directory containing your JSON files
json_folder = "CapstoneJsonData"

print(es.info())
print(os.getcwd())

# Loop through the files in the folder
for filename in os.listdir(json_folder):
    print(filename)
    if filename.endswith(".json"):
        # Construct the full path to the JSON file
        file_path = os.path.join(json_folder, filename)

        # Read the JSON data from the file
        with open(file_path, 'r') as file:
            json_data = json.load(file)

        # Index the JSON data into Elasticsearch
        es.index(index='search-business-data', body=json_data)

# Refresh the index to make the documents searchable
es.indices.refresh(index='search-business-data')
