import tensorflow_hub as hub
import tensorflow_text as text
import json
import os
from multiprocessing import Pool

input_dir = 'BERT/DataAsJsons'
output_dir = 'BERT/EncodedJsons'

encoder_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4'
preprocessing_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'

encoder_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4'
preprocessing_url = 'https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3'
preprocessing_model = hub.KerasLayer(preprocessing_url)
bert_model = hub.KerasLayer(encoder_url)

def process_file(filename):
    if filename.endswith('.json'):
        input_filepath = os.path.join(input_dir, filename)
        output_filepath = os.path.join(output_dir, filename)

        with open(input_filepath, 'r') as file:
            data = json.load(file)

        batch_of_strings = []
        for item in data:
            for review in item['reviews']:
                batch_of_strings.append(review['text'])

        preprocessed_text = preprocessing_model(batch_of_strings)
        bert_results = bert_model(preprocessed_text)

        # Extracting the pooled_output which will serve as our encoding
        encodings = bert_results['pooled_output'].numpy().tolist()

        # Adding business details to the output data
        business_details = data[0]['business_details']
        
        output_data = {
            'business_details': business_details,
            'encodings': encodings
        }
        
        # Save the encodings to a new JSON file in the output folder
        with open(output_filepath, 'w') as file:
            json.dump(output_data, file)

if __name__ == "__main__":
    with Pool(8) as p:
        p.map(process_file, os.listdir(input_dir))
