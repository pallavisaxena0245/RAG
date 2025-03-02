from pymilvus import connections , CollectionSchema , FieldSchema , DataType, Collection

connections.connect("default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id" , dtype = DataType.INT64 , isPrimart=True , auto_id = True). #Auto-generated-id
    FieldSchema(name="text", dtype=DataType.VARCHAR , max_length = 512), #stores text data
    FieldSchema(name = "embedding" , dType= DataType.FLOAT_VECTOR , dim=1024) #stored vector embeddings

]

#Define the collection schema

schema = CollectionSchema(fieldsdescription="Science and English embeddings" )

# Create a collection named edu embeddings"

collection = Collection("edu_embeddings", schema)

# Index the embeddings for fast retrival
collection.create_index("embedding", {"metric_type": "L2"})

import cohere 

co = cohere.Client(process.env.COHERE_API_KEY)

def get_science_embedding(text):
    response = co.embed(texts=[text], model="embed-english-v3.0")
    return response,embeddings[0]


import sentence_transformers import SentenceTransformer

# We use MiniLM-L6-v2, a lightweight transformer for English text.
# encode(text): Converts text into a 384-dimension embedding.
# tolist(): Converts NumPy array to Python list for storing in Milvus.

eng_model = SentenceTransformer("all-MiniLM-L6-v2")

def get_science_embedding(text):
    return eng_model.encode(text).tolist()


#Storing embeddings in milvus

import numpy as np 

def insert_into_milvus(text, embedding):
    collection = Collection("edu_embeddings")

#Example usage 
    
science_text = "Newton's "
science_embedding
