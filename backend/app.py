from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
import os
from dotenv import load_dotenv
import tensorflow_hub as hub
import tensorflow_text as text
import json

load_dotenv()

app = Flask(__name__)

encoder_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4'
preprocessing_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'

preprocessing_model = hub.KerasLayer(preprocessing_url)
bert_model = hub.KerasLayer(encoder_url)

index_name = "search-business-data"

user = 'elastic'
password = os.environ.get('ELASTIC_PASSWORD')

# Configure Elasticsearch
es = Elasticsearch(
  "https://localhost:9200",
  basic_auth=(user, password),
  verify_certs=False
)

@app.route('/search', methods=['POST'])
def search():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    
    keywords =["indian", "italian", "chinese", "mexican", "japanese", 
    "thai", "french", "spanish", "greek", "lebanese", 
    "ethiopian", "vietnamese", "korean", "turkish", "brazilian", 
    "moroccan", "russian", "peruvian", "cuban", "german", 
    "filipino", "caribbean", "south african", "polish", 
    "egyptian", "hawaiian", "iranian", "portuguese", "argentine", "belgian", "danish", 
    "finnish", "dutch", "hungarian", "indonesian", 
    "malaysian", "nepalese", "pakistani", "romanian", "swiss", 
    "armenian", "mediterranean", "asian"]
    matched_keywords = [keyword for keyword in keywords if keyword in data['inputText'].lower()]

    preprocessed_text = preprocessing_model([data['inputText']])
    preprocessed_text['input_word_ids']

    bert_results = bert_model(preprocessed_text)

    input_vector = bert_results['pooled_output']
    input_vector = input_vector.numpy()
    input_vector = input_vector.tolist()[0]
    
    if matched_keywords: 
        filter_query = {
            "terms": {
                "business_details.categories": matched_keywords
            }
        }
    else:  
        filter_query = {
            "match_all": {}
        }

    query = {
        "size": 3,
        "query": {
            "bool": {
                "must": {
                    "script_score": {
                        "query": {
                            "bool": {
                                "filter": filter_query
                            }
                        },
                        "script": {
                            "source": "cosineSimilarity(params.query_vector, 'encoding') + 1.0",
                            "params": {"query_vector": input_vector}
                        }
                    }
                }
            }
        }
    }



    try:
        response = es.search(index=index_name, body=query)
        response_data = [hit['_source']['business_details'] for hit in response['hits']['hits']]

        return jsonify({'response': response_data}), 200

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)